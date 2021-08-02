# Robot-arm-for-Object-Specific-Pick-with-Computer-Vision-base-on-Kinect-sensor


## Software
**Object detection and localization:**

The computer vision algorithm is based on Yolov2. With Yolov2 the target can be detected and locolized with a rectangle in realtime.
The RGB camera of Kinect is used for object detection and localization.
Thanks to the open source library pylibfreenect the kinect can be run on Ubuntu system with libfreenect python functions.
https://github.com/r9y9/pylibfreenect2.git

The following diagramm shows the structure of the project.

![image](https://user-images.githubusercontent.com/38363960/127919027-79697872-2fc0-404a-b8ec-7d7463aaca59.png)

![QQ图片20210802232047](https://user-images.githubusercontent.com/38363960/127925409-1e488732-9ce6-43d9-a612-e02d76f45e7a.jpg)


**Calculate the 3D position of target in real world.**
1. Transfer the 2D position of target object from RGB camera coordinate into real worl coordinate with camera parameter
2. Allign the 2D position of depth camera with RGB camera
3. After step2 the depth position can be added to the 2d postion in RBG camera coordinate

Copy the python scrpits and put them on the folder of darkflow. Then run the main script. 
As the following picture shows, the 3D position of the center of detected target is presented in the middle of rectangle.

![image](https://user-images.githubusercontent.com/38363960/127788096-b8303176-fe89-4432-bbc6-ad6b63a56593.png)


**Camera calibration**

The Zhang Youzheng calibration method based on OpenCV is used for camera calibration.

**Instance segmentation**

In order to calculate the optimal pick position of the bottle, the object segmentation is necessary to estimate the object bundary. The the pick position can be calculated with different algorithum. The object segmentation is to be developed.

**ROS**

The ROS is used for coordinate the 3D position calculated in Jetson Nano boad, the robot arm position and motor control.
The code for ROS is under development.

**Communication between Jetson Nano board and Raspberry board**
The I2C bus is used to communicate between Jetson Nano board and Raspberry board.
To do



## Hardware
**1. Nvidia Jetson Nano Board**

NVIDIA Jetson Nano board is used as a controller. With the Jetson Nano and its 128 NVIDIA CUDA Cores the powerful machine learning applications can be easily implemented and realized.

Please refer to the website https://developer.nvidia.com/embedded/jetson-nano-developer-kit for information about the configuration.

**2. Kinect**

The Kinect v2 contains a Time-of-Flight (ToF) camera and determines the depth by measuring the time emitted light takes from the camera to the object and back. Therefore, it constantly emits infrared light with modulated waves and detects the shifted phase of the returning light.
The Kinect v2 also has a RGB camera. So with the 2D information and the depth information it is possible to calculate the 3D position in the real word coordinate.

**3. Robot arm**

![QQ图片20210802232432](https://user-images.githubusercontent.com/38363960/127925775-a15af2f4-d33e-4860-850a-9f18049abb05.jpg)


Hiwonder robot arm, bought from the following link
https://item.jd.com/54284760045.html
 
This robot arm with six dof is used to pick the bottle. 

**4. raspberry pi**

A raspberry pi board is needed to control the robot arm. So the robot arm is moved with six motors mounted on joints. Each motor is driven by PWM signal, which can be sent out by six GPIO ports in Raspberry Pi.
