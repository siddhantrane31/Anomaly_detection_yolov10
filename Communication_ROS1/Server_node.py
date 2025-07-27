import rospy
from std_msgs.msg import String
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(subject, message, recipient_email):
sender_email = 'your-email@example.com'
sender_password = 'YourEmailPassword' # Securely store and use
credentials
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login(sender_email, sender_password)
58
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
server.sendmail(sender_email, recipient_email, msg.as_string())
server.quit()
rospy.loginfo("Email sent to %s regarding %s", recipient_email, subject)
def callback(data):
rospy.loginfo("Received data: %s", data.data)
anomaly_info = json.loads(data.data)
# Email addresses and priorities based on anomaly type
anomaly_details = {
'fire': {'priority': 1, 'email': 'fire-alerts@example.com'},
'unidentified': {'priority': 1, 'email': 'security@example.com'},
'garbage': {'priority': 2, 'email': 'waste-management@example.com'}
}
# Retrieve details based on anomaly type
if anomaly_info['type'] in anomaly_details:
59
details = anomaly_details[anomaly_info['type']]
priority = details['priority']
recipient_email = details['email']
# Compose email subject and body
subject = f"Priority {priority} Alert: {anomaly_info['type']} detected!"
    message = f"An anomaly of type {anomaly_info['type']} was detected at {timestamp}"
{anomaly_info['location']} on {anomaly_info['timestamp']}."
# Send email if recipient email is defined
send_email(subject, message, recipient_email)
def listener():
rospy.init_node('anomaly_processor', anonymous=True)
rospy.Subscriber("anomaly_topic", String, callback)
rospy.spin()
if name == ' main ':
listener()