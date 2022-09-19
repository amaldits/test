#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

arr_pos_x = []
arr_pos_y = []
arr_pos_z = []

arr_ori_x = []
arr_ori_y = []
arr_ori_z = []
arr_ori_w = []

new_pose = PoseStamped()
n = 0

offset = 0

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard [%f %f %f]", data.pose.position.x, data.pose.position.y, data.pose.position.z)
    # rospy.loginfo(rospy.get_caller_id() + "I heard [%f %f %f %f]", data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w)
    offset = data.header.seq
    arr_pos_x.append(data.pose.position.x)
    arr_pos_y.append(data.pose.position.y)
    arr_pos_z.append(data.pose.position.z)
    arr_ori_x.append(data.pose.orientation.x)
    arr_ori_y.append(data.pose.orientation.y)
    arr_ori_z.append(data.pose.orientation.z)
    arr_ori_w.append(data.pose.orientation.w)

    if len(arr_pos_x) == int(n):
        avg_pos_x = sum(arr_pos_x) / len(arr_pos_x)        
        new_pose.pose.position.x = avg_pos_x
        arr_pos_x.clear()

    if len(arr_pos_y) == int(n):
        avg_pos_y = sum(arr_pos_y) / len(arr_pos_y)        
        new_pose.pose.position.y = avg_pos_y
        arr_pos_y.clear()

    if len(arr_pos_z) == int(n):
        avg_pos_z = sum(arr_pos_z) / len(arr_pos_z)
        new_pose.pose.position.z = avg_pos_z
        arr_pos_z.clear()

    if len(arr_ori_x) == int():
        avg_ori_x = sum(arr_ori_x) / len(arr_ori_x)        
        new_pose.pose.orientation.x = avg_ori_x
        arr_ori_x.clear()

    if len(arr_ori_y) == int(n):
        avg_ori_y = sum(arr_ori_y) / len(arr_ori_y)        
        new_pose.pose.orientation.y = avg_ori_y
        arr_ori_y.clear()

    if len(arr_ori_z) == int(n):
        avg_ori_z = sum(arr_ori_z) / len(arr_ori_z)        
        new_pose.pose.orientation.z = avg_ori_z
        arr_ori_z.clear()

    if len(arr_ori_w) == int(n):
        avg_ori_w = sum(arr_ori_w) / len(arr_ori_w)        
        new_pose.pose.orientation.w = avg_ori_w
        arr_ori_w.clear()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("vslam2d_pose", PoseStamped, callback)

    pub = rospy.Publisher('vslam2d_newpose', PoseStamped, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        pub.publish(new_pose)
        rate.sleep()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    n = input("Enter your divider: ")
    listener()