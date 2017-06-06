from __future__ import print_function
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageService:
    def __init__(self):

        self.bridge = CvBridge()
        self.topImage = None
        self.bottomImage = None

        self.image_top_sub = rospy.Subscriber("/nao_robot/camera/top/camera/image_raw", Image, self.topCallback, queue_size=1)
        self.image_bottom_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw", Image, self.bottomCallback, queue_size=1)
        rospy.sleep(20)


    def topCallback(self, data):

        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        self.topImage = cv_image

        rospy.loginfo("image top got")

    def bottomCallback(self, data):

        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        self.bottomImage = cv_image

        rospy.loginfo("image bottom got")

    def getTopImage(self):
        return self.topImage

    def getBottomImage(self):
        return self.bottomImage

if __name__ == '__main__':

    rospy.init_node('take_photo', anonymous=False)
    camera = ImageService()


    cv2.imwrite("top.jpg", camera.getTopImage())
    cv2.imwrite("bottom.jpg", camera.getBottomImage())
    #rospy.spin()
    rospy.sleep(1)