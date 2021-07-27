# Robot-arm-for-Object-Specific-Pick-with-Computer-Vision-base-on-Kinect-sensor


## Software
**Object detection and localization:**

The computer vision algorithm is based on Yolov2. With Yolov2 the bottle can be detected and locolized with a rectangle.
The RGB camera of Kinect is used for object detection and localization
Thanks to the open source library pylibfreenect the kinect can be run on Ubuntu system with libfreenect python functions.
https://github.com/r9y9/pylibfreenect2.git

**Calculate the 3D position of target in real world.**
1. Transfer the 2D position of target object from RGB camera coordinate into real worl coordinate with camera parameter
2. Allign the 2D position in depth camera with RGB camera
3. After step2 the depth position can be added to the 2d postion in RBG camera coordinate

The following picture shows that the 3D position of the center of detected target is shown in the middle of rectangle.

**Camera calibration**

The Zhang Youzheng calibration method based on OpenCV is used for camera calibration.

**Object segmentation**

In order to calculate the optimal pick position of the bottle, the object segmentation is necessary to estimate the object bundary. The the pick position can be calculated with different algorithum. The object segmentation is to be developed.

**ROS**

The ROS is used for coordinate the 3D position calculated in Jetson Nano boad, the robot arm position and motor control.
The code for ROS is under development.

**Communication between Jetson Nano board and Raspberry board**

To do



## Hardware
**1. Nvidia Jetson Nano Board**

NVIDIA Jetson Nano board is used as a controller. With the Jetson Nano and its 128 NVIDIA CUDA Cores the powerful machine learning applications can be easily implemented and realized.

Please refer to the website https://developer.nvidia.com/embedded/jetson-nano-developer-kit for information about the configuration.

**2. Kinect**

The Kinect v2 contains a Time-of-Flight (ToF) camera and determines the depth by measuring the time emitted light takes from the camera to the object and back. Therefore, it constantly emits infrared light with modulated waves and detects the shifted phase of the returning light.
The Kinect v2 also has a RGB camera. So with the 2D information and the depth information it is possible to calculate the 3D position in the real word coordinate.

**3. Robot arm**

![image](https://user-images.githubusercontent.com/38363960/127217896-ca75742f-6026-482c-a416-6b4200888383.png)

Hiwonder robot arm, bought from the following link
https://item.jd.com/54284760045.html
 
This robot arm with six dof is used to pick the bottle. 

**4. raspberry pi**

A raspberry pi board is needed to control the robot arm. So the robot arm is moved with six motors mounted on joints. Each motor is driven by PWM signal, which can be sent out by six GPIO ports in Raspberry Pi.
