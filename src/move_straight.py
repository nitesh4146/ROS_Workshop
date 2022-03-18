#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    ### Initialize your node here ###


    ### Create your publisher here ###


    # Declare the Twist message 
    vel_msg = Twist()

    # Receiveing the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    isForward = input("Foward?: ") # True or False

    # Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    ### Since we are moving just in x-axis, ###
    ### set all other fields to zero here ####


    while not rospy.is_shutdown():

        # Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        # Loop to move the turtle in an specified distance
        while(current_distance < distance):

            ### Publish the velocity message here ###

            
            # Takes actual time to velocity calculus
            t1 = rospy.Time.now().to_sec()

            # Calculates distancePoseStamped
            current_distance = speed*(t1-t0)
        
        ### After the loop, stop the robot ###
        ### Publish a zero velocity here ###


        ### Publish the zero velocity message here ###



if __name__ == '__main__':
    try:
        move()
        # Testing our function
    except rospy.ROSInterruptException: 
        pass
