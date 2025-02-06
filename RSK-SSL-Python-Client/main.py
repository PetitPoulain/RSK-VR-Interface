import rsk
import math
import time
import pygame
from rsk import constants
from pythonosc import udp_client

#*****************************************************************************#

joysticks = []

OSCip = '127.0.0.1'
OSCport = 12346

RSKip = '127.0.0.1'  # 192.168.100.1
RSKkey = ''

Type = "RSK"  # RSK/SSL
Team = 'green'  # green/blue
No_Bots = 2  # number from 1 to 6

deadzone = 0.2

#*****************************************************************************#

pygame.init()
pygame.joystick.init()

#*****************************************************************************#

time.sleep(2)


#*****************************************************************************#

def scan_controller():
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            print(event)
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)


#*****************************************************************************#

def coordone(team, numBot):
    # Position + orientation (x [m], y [m],angle [rad])
    xR, yR, rad = RSKclient.robots[team][numBot].pose
    degR = math.degrees(rad)
    return round(xR, 2), round(yR, 2), round(degR, 2)


#*****************************************************************************#

def send_data(team, numBot, xSpeed, ySpeed, Rads):
    RSKclient.robots[team][numBot].control(xSpeed, ySpeed, Rads)
    if kicks:
        RSKclient.robots[team][numBot].kick()


#*****************************************************************************#

def get_controller():
    global x, y, rads, kicks, deadzone
    for joystick in joysticks:
        x = round(joystick.get_axis(1), 3) if (joystick.get_axis(1) > deadzone or joystick.get_axis(
            1)) < deadzone else x = 0

        y = round(joystick.get_axis(0), 3) if (joystick.get_axis(0) > deadzone or joystick.get_axis(
            1)) < deadzone else y = 0

        rads = round(joystick.get_axis(3), 3)
        kicks = joystick.get_button(5)
    return x, y, rads, kicks


#*****************************************************************************#

def OSC(xB, yB, xR, yR, degR, team, numBot):
    OSCclient.send_message(f"/RSK/BallX", xB)
    OSCclient.send_message(f"/RSK/BallY", yB)

    OSCclient.send_message(f"/RSK/RobotX", xR)
    OSCclient.send_message(f"/RSK/RobotY", yR)
    OSCclient.send_message(f"/RSK/RobotDeg", degR)
    OSCclient.send_message(f"/RSK/RobotTeam", team)
    OSCclient.send_message(f"/RSK/RobotNo", numBot)


#*****************************************************************************#

OSCclient = udp_client.SimpleUDPClient(OSCip, OSCport)
if Type == "RSK":
    RSKclient = rsk.Client(host=RSKip, key=RSKkey)
    OSCclient.send_message(f"/RSK/RobotType", Type)
elif Type == "SSL":
    pass
else:
    print("Type error")
    exit()


#*****************************************************************************#

#constants.max_linear_acceleration, constants.max_angular_accceleration

def main():
    try:
        scan_controller()
        while True:
            x, y, rads, kicks = get_controller()
            xR, yR, degR = coordone(Team, No_Bots)
            xB, yB = RSKclient.ball

    except rsk.ClientError:
        print(rsk.ClientError)


#*****************************************************************************#

if __name__ == "__main__":
    main()
