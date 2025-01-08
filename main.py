import rsk
import math
import time
import pygame
from rsk import constants
from pythonosc import udp_client

pygame.init()
pygame.joystick.init()

joysticks = []

OSCip = '127.0.0.1'
OSCport = 12346

RSKip = '192.168.100.1'
RSKkey = ''

Type = "RSK" # RSK or SSL
Team = 'green' # green or blue
No_Bots = "2" # number from 1 to 6

OSCclient = udp_client.SimpleUDPClient(OSCip, OSCport)
RSKclient = rsk.Client(host=RSKip, key=RSKkey)

def scan_controller():
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            print(event)
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)

def coordone(team, num):
    xR, yR, rad = RSKclient.robots[team][num].pose  # Position + orientation (x [m], y [m],angle [rad])
    degR = math.degrees(rad)
    print(round(xR, 2), round(yR, 2), round(degR, 2))
    return xR, yR, degR

def get_controller():
    global x, y, rads, kicks
    for joystick in joysticks:
        if joystick.get_axis(1) > 0.1:
            x = round(joystick.get_axis(1), 3)
        elif joystick.get_axis(1) < 0.1:
            x = round(joystick.get_axis(1), 3)
        else:
            x = 0

        if joystick.get_axis(0) > 0.1:
            y = round(joystick.get_axis(0), 3)
        elif joystick.get_axis(0) < 0.1:
            y = round(joystick.get_axis(0), 3)
        else:
            y = 0

        rads = round(joystick.get_axis(3), 3)
        kicks = joystick.get_button(5)
    return x, y, rads, kicks

def send_data_RSK(xSpeed, ySpeed, Rads):
    RSKclient.robots[Team][No_Bots].control(xSpeed, ySpeed, Rads)

def main():
    try:
        while True:
            scan_controller()

            x, y, rads, kicks = get_controller()
            xR, yR, degR = coordone('green', 2)
            xB, yB = RSKclient.ball

            # RSKclient.robots['green'][2].control(-x * constants.max_linear_acceleration,
            #                                     -y * constants.max_linear_acceleration,
            #                                     -rads * constants.max_angular_accceleration / 3)
            if kicks:
                RSKclient.robots['green'][2].kick()

            OSCclient.send_message(f"/RSK/BallX", xB)
            OSCclient.send_message(f"/RSK/BallY", yB)

            OSCclient.send_message(f"/RSK/RobotX", xR)
            OSCclient.send_message(f"/RSK/RobotY", yR)
            OSCclient.send_message(f"/RSK/RobotDeg", degR)
            OSCclient.send_message(f"/RSK/RobotType", Type)

    except rsk.ClientError:
        print('Error during a command!')


if __name__ == "__main__":
    main()