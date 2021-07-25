# coding: utf-8

# An example using startStreams

import numpy as np
import cv2
import sys
import time
import tensorflow as tf
from pylibfreenect2 import Freenect2, SyncMultiFrameListener
from pylibfreenect2 import FrameType, Registration, Frame


with tf.Session(config=config) as sess:
    options = {
            'model': 'cfg/yolov2-tiny-voc.cfg',
            'load': 'bin/yolov2-tiny-voc.weights',
            'threshold': 0.2,
            'gpu': 1.0
                    }
    tfnet = TFNet(options)

colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]


    while(!protonect_shutdown)
    {
        listener.waitForNewFrame(frames);
        libfreenect2::Frame *rgb = frames[libfreenect2::Frame::Color];
        libfreenect2::Frame *depth = frames[libfreenect2::Frame::Depth];
 
        cv::Mat(rgb->height, rgb->width, CV_8UC4, rgb->data).copyTo(rgbmat);
        cv::Mat(depth->height, depth->width, CV_32FC1, depth->data).copyTo(depthmat);
        cv::Mat(registered.height, registered.width, CV_8UC4, registered.data).copyTo(rgbd);
 
        registration->apply(rgb, depth, &undistorted, &registered, true, &depth2rgb);
        cv::Mat(registered.height, registered.width, CV_8UC4, registered.data).copyTo(rgbd);
 
        //resize(rgbmat, dst1, Size(), c, d, INTER_NEAREST);
        inRange(depthmat,Scalar(a),Scalar(b),dst);
        //morphologyEx(dst,dst,MORPH_OPEN,kernel);
        findContours(dst,contours,hireachy,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE,Point(0,0));
        if (contours.size() > 0)
        {
            double maxArea=0;
            for (int i = 0; i < contours.size(); i++)
            {
                double area = contourArea(contours[static_cast<int>(i)]);
                if (area > maxArea)
                {
                    maxArea = area;
                    rect = boundingRect(contours[static_cast<int>(i)]);
                    minEnclosingCircle(contours[static_cast<int>(i)], center, radius);
                }
            }
        }
 
 
        setMouseCallback("main",on_MouseHandle);     // ????
        registration->getPointXYZ(&undistorted, pt11.y, pt11.x,x1, y1, z1);  // ???????????
        registration->getPointXYZ(&undistorted,pt21.y,pt21.x,x2, y2, z2);
 
        //rectangle(rgbd, rect, Scalar(0,255,0),2);
        line(rgbd, pt11, pt21, Scalar(0,255,0));   //  ??
        l = sqrt(pow((x1-x2),2) + pow((y1-y2),2) + pow((z1-z2),2));
        cout << "length:" << l << "m" <<endl;   // ????
        sprintf(str, "%.4lf", l);
        putText(rgbd, str1, pt21, FONT_HERSHEY_COMPLEX, 1,Scalar(0, 0, 255), 1);
        putText(rgbd, str, pt21, FONT_HERSHEY_COMPLEX, 1,Scalar(0, 0, 255), 1);
 
        circle(rgbd, pt11, 1, Scalar(255,255,0), 2);
        circle(rgbd, pt21, 1, Scalar(255,255,0), 2);
        cv::imshow("catch",dst);
        cv::imshow("depth", depthmat /4500.0);
        cv::imshow("main", rgbd);
 
        int key = cv::waitKey(1);
        protonect_shutdown = protonect_shutdown || (key > 0 && ((key & 0xFF) == 27)); // shutdown on escape
 
        listener.release(frames);
    }
 
    dev->stop();
    dev->close();
 
    delete registration;
 
#endif
 
    std::cout << "stop!" << std::endl;
    return 0;
}
 
void on_MouseHandle(int event, int x, int y, int flags, void* ustc)
{
    if (event == EVENT_LBUTTONDOWN)
    {
        Point pt1 = Point(x, y);
        pt11 = pt1;
    }
    else if (event == EVENT_LBUTTONUP)
    {
 
        Point pt2 = Point(x, y);
        pt21 = pt2;
    }
}

device.stop()
device.close()

sys.exit(0)
