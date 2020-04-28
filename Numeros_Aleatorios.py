#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import String
from time import sleep

pub = rospy.Publisher('Aleatorio', String, queue_size=10)
rospy.init_node("Numeros_Aleatorios", anonymous=True)
i=3
while i <= 3:
	mensaje= "Aleatorio: " + str(random.randint(1,1000))
	rospy.loginfo(mensaje)
	pub.publish(mensaje)
	sleep(5)

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass






