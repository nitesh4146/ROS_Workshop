#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate():
    ### Initialize your node here ###


    ### Create your publisher here ###


    ### Initialize the Twist msg ###


    # Receiveing the user's input
    print("Let's rotate your robot")
    speed = input("Input your speed (degrees/sec):")
    angle = input("Type your distance (degrees):")
    clockwise = input("Clockwise?: ") #True or false

    # Converting from angles to radians
    angular_speed = speed * 2*PI/360
    relative_angle = angle * 2*PI/360


    #### Since we are rotating in z-axis, ####
    ### set all other fields to zero here ####



    ###### Initialize your angular velocity along #####
    ### z-axis here. Check if movement is CW or CCW ###

    
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        ### Publish the velocity message here ###


        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed * (t1-t0)


    ### Publish the zero velocity message here ###


if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass