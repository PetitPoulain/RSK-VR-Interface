# RSK-VR-Interface
[Resonite Homepage](https://resonite.com/)

[NAMeC X](https://x.com/namecteam)

[RSK Project page](https://robot-soccer-kit.github.io/)

[RSK Github page](https://github.com/robot-soccer-kit/robot-soccer-kit)


- [x] Make a basic map of what to do
- [x] Make a "universal" interface to comunicate between te robot and the 3D interface
- [ ] Manage to control more than one robot at the same time ( Partially working )
- [x] Make a basic usb controller interface to control the robot
/**********************************************************************************************************/
- Resonite ( Single player / Multiplayers )
- [x] Manage to be able to chose a specific robot in Resonite
- [x] Manage to control the robot from Resonite
- [x] Manage to get a 3D model of the robot move acordingly to the position of the IRL robots in Resonite
- [ ] Manage to have a first person view of the robot in Resonite ( Partially working )
/**********************************************************************************************************/
- Unity ( Single Player Only )
- [ ] Manage to be able to chose a specific robot in Unity
- [ ] Manage to control the robot from Unity
- [ ] Manage to get a 3D model of the robot move acordingly to the position of the IRL robots in Unity
- [ ] Manage to have a first person view of the robot in Unity

![alt text](https://github.com/PetitPoulain/RSK-VR-Interface/blob/main/Diagram.png?raw=true)

During the years 2023-2024 I worked on making a VR interface for the named team for there RoboCup SSL division robot. 
Unfortunately, due to a lack of time and issue with the actual robot I wasn't able to accomplish my goal.
A couple of months ago, back in October we asked me to take back that original project but instead of making the interface for the SSL robot we charged
Me of doing it for the RSK robots, which are smaller and easier to program and work with.

During the first couple of classes, I did a small basic list of what I should do, once I did that I started working on programming some sort of "universal layer".
The way the project was originally intended to work was to have the robot connected to its usual control interface and then directly make the VR interface communicate with the normal control interface. Instead of doing this I opted to have a small piece of software in between call an OSC interface.
Now the VR interface we want to use connect to the OSC and the OSC is doing the link with the control interface of the robot.
In this way, it is way easier to use different VR interface or even 2D interface as OSC is widely use in VR to communicate with the device.
Using OSC also allows us to easily switch software in the future without to remake the entire code, instead only a small code of a few lines is all would be needed to adapt the new software to the OSC layer.

After doing so, I started working on the VR side of the thing. First, I needed some 3D model of the field and the robot. The dimension of the field and model of the robot is publicly available so it only took less than an hour to get every model ready.

I did not start working with unity yet, I wanted to first get a good view of how to make things right and what could I do to embellish the project, so I started implementing the robot inside of Resonite VR. Resonate is some sort of a sandbox VR game where you can create everything you want directly in-game, last years I had connected my lawn mower to the game and a Swiss person ended up driving my mower in my garden from his home hundreds of kilometers away from my house.
I wanted to reuse the knowledge I gained doing this and apply the concept to the RSK and be able to have people from all around the world be able to assist a match in VR and be able to play a match by controlling those robots.

#Part 2
#Part 3
