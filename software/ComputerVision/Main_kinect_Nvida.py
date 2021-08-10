####################################################################
##########################import####################################

import numpy as np
import cv2
import sys
import time
import tensorflow as tf
import camera_parameter
import Functions_camera
from pylibfreenect2 import Freenect2, SyncMultiFrameListener
from pylibfreenect2 import FrameType, Registration, Frame
import Init

####################################################################
#########################yolov2#####################################


# import TFNet from darkflow net
# use yolov2-tiny-voc.cfg as configuration file
# use yolov2-tiny-voc.weights as weight file
# use gpu support
from darkflow.net.build import TFNet
config = tf.ConfigProto(log_device_placement=True)
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    options = {
            'model': 'cfg/yolov2-tiny-voc.cfg',
            'load': 'bin/yolov2-tiny-voc.weights',
            'threshold': 0.2,
            'gpu': 1.0
                    }
    tfnet = TFNet(options)


####################################################################
######################3d coordinate of target#######################


colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

while True:
    stime = time.time()
    frames = Init.listener.waitForNewFrame()
    color = frames[FrameType.Color]
    ir = frames[FrameType.Ir]
    depth = frames[FrameType.Depth]
    Init.registration.apply(color, depth, Init.undistorted, Init.registered)


# get the rgb frames
    if Init.enable_rgb:
        frame = frames["color"]
        frame = cv2.resize(frame.asarray(),(int(1920 / 2), int(1080 / 2)))
        frame = cv2.cvtColor(frame,cv2.COLOR_RGBA2RGB)
# get the depth frames
    if Init.enable_depth:
        framed = frames["depth"]
        frame_Depth = framed.asarray()
        frameDepth = framed.asarray()
        frameDepth = np.reshape(frameDepth,(424, 512))
        frame_Depth = frame_Depth.astype(np.uint8)
        frame_Depth = cv2.cvtColor(frame_Depth,cv2.COLOR_GRAY2RGB)


    results = tfnet.return_predict(frame)

    # calculate the x,y,z coordinate of the center point in the world coordinate of the detected target from the camera coordinate
    for color1, result in zip(colors, results):

            # calculate the center coordinate of rectangle resulted from yolov2
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            x_Center = int((((result['topleft']['x']) + (result['bottomright']['x']))/2))
            y_Center = int((((result['topleft']['y']) + (result['bottomright']['y']))/2))

            #Tweek on 'x_Center /1.42) -115' to adjust alignment between RGB camera and depth camera
            Center = (int(x_Center /1.42) -115, int(y_Center *.8))
            CenterC = int(x_Center), int(y_Center)
            Pixel = frameDepth[int(y_Center * .8)]
            Pixel_Depth = Pixel[Functions_camera.clamp(int(x_Center /1.42)-115,0,511)]

            # calculate the x,y,z coordinate of the center point in the world coordinate of the detected target from the camera coordinate
            x, y, z = Functions_camera.Convert_PosCameraDepth_To_XYZ(x_Center,y_Center,Pixel_Depth)
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            textD = '({},{},{})'.format(int(x),int(y),int(z))
            frame = cv2.rectangle(frame, tl, br, color1, 5)
            frame_Depth = cv2.circle(frame_Depth, Center, 10, color1, -1)
            frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            frame = cv2.putText(frame, textD,CenterC, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


    # Show the RGB image and depth image in OpenCv
    cv2.imshow('frame', frame)
    cv2.imshow('frame_Depth', frame_Depth) 

    # print the FPS information
    print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    Init.listener.release(frames)
    key = cv2.waitKey(delay=1)
    if key == ord('q'):
        break



device.stop()
device.close()

sys.exit(0)
