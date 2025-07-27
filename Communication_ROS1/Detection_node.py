#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import json
import pytz
from datetime import datetime
import time
def talker():
pub = rospy.Publisher('anomaly_topic', String, queue_size=10)
rospy.init_node('anomaly_publisher', anonymous=True)
rate = rospy.Rate(1) # 1hz
# Loop to get user input and publish for a specific duration
while not rospy.is_shutdown():
# Geting anomaly type from user input
anomaly_type = input("Enter anomaly type: ")
start_time = time.time()
while (time.time() - start_time) < 1:
uk_timezone = pytz.timezone('Europe/London')
    current_time = datetime.now(uk_timezone).strftime('%Y-%m-%d %H:%M:%S')
%dT%H:%M:%S%z')
# Creating JSON data for publishing
anomaly_data = json.dumps({"type": anomaly_type, "location":
"X=11.4,Y=8", "timestamp": current_time})
rospy.loginfo(anomaly_data)
pub.publish(anomaly_data)
57
rate.sleep()
if name == ' main ':
try:
talker()
except rospy.ROSInterruptException:
pass
