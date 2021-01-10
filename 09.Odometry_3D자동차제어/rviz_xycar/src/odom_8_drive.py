#!/usr/bin/env python

import rospy
import time
from xycar_motor.msg import xycar_motor
from std_msgs.msg import Header



rospy.init_node('auto_driver')

pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

def motor_pub(angle, speed):
    # global pub
    motor_control = xycar_motor()
    motor_control.header = Header()
    motor_control.header.stamp = rospy.Time.now()
    motor_control.angle = angle
    motor_control.speed = speed

    pub.publish(motor_control)

speed = 6
turn_angle = 10
straight_angle = 0
rate = rospy.Rate(10)

while not rospy.is_shutdown():

    # 좌회전 또는 우회전
    for _ in range(0,250):
        motor_pub(turn_angle,speed)
        rate.sleep()
    
    for _ in range(0,75):
        motor_pub(straight_angle,speed)
        rate.sleep()
    
    # 좌회전 방향이면 우회전으로, 우회전 방향이면 좌회전으로 변경
    turn_angle *= -1

    

