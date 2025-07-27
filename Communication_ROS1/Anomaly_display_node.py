import rospy
from std_msgs.msg import String
import json
import tkinter as tk
import pygame
def init_audio():
pygame.mixer.init()
sounds = {
63
'Fire':
pygame.mixer.Sound("/home/tejas/catkin_ws/src/display_node/scripts/fire.wav")
,
'garbage':
    pygame.mixer.Sound("/home/tejas/catkin_ws/src/display_node/scripts/garbage.wav")
wav"),
'unidentified':
pygame.mixer.Sound("/home/tejas/catkin_ws/src/display_node/scripts/object.wa
v") # Ensure correct file path
}
return sounds
def callback(data, label, sounds):
rospy.loginfo(rospy.get_caller_id() + " I received %s", data.data)
msg = json.loads(data.data.split(':', 1)[1]) # Remove the priority prefix
# Set the color based on the type of anomaly
if msg['type'] == 'Fire':
color = 'red'
elif msg['type'] == 'garbage':
color = 'green'
elif msg['type'] == 'unidentified':
color = 'yellow' # Change the color for unidentified objects to yellow
else:
color = 'grey' # Default color if none of the types match
label.config(bg=color)
64
label.config(text=msg['type'])
sound = sounds.get(msg['type'], None)
if sound:
sound.play()
def main():
# Initialize the ROS node and audio
rospy.init_node('anomaly_display', anonymous=True)
sounds = init_audio()
# Set up the GUI
root = tk.Tk()
root.title("Anomaly Display")
label = tk.Label(root, text="", font=('Helvetica', 200), width=200)
label.pack(padx=150, pady=150, fill=tk.BOTH, expand=True)
# Subscribe to the ROS topic
rospy.Subscriber("display_topic", String, lambda data: callback(data, label,
sounds))
# Start the Tkinter main-loop
tk.mainloop(if name == ' main ':
main()