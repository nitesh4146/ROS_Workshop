#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def mover():
    pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    rospy.init_node('moveturtlefwd')
    straight_twist=Twist()
    straight_twist.linear.x=1
    turn_twist=Twist()
    turn_twist.angular.z=0.5
    rate=rospy.Rate(10)
    change_time=rospy.Time.now()
    turning=False

    while not rospy.is_shutdown():
        if turning:
            pub.publish(turn_twist)
        else:
            pub.publish(straight_twist)
        if rospy.Time.now() > change_time:
            turning = not turning
            change_time=rospy.Time.now() + rospy.Duration(3)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
