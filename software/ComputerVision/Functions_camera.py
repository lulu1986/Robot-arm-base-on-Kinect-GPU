import camera_parameter
#calculate the xyz camera position based on the depth data  
def Convert_PosCameraDepth_To_XYZ(x_d, y_d, z):   
    x = (x_d - camera_parameter.CameraParams['cx']) * z / camera_parameter.CameraParams['fx']
    y = (y_d - camera_parameter.CameraParams['cy']) * z / camera_parameter.CameraParams['fy']
    return x, y, z

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
