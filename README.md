# 🤖 AI-Based Fall Detection + ROS Communication System

This repository implements a real-time anomaly detection system using YOLOv10, integrated with a ROS1-based communication network for handling detection, alerts, and robot responses. Originally focused on fall detection, this system is modular and can be adapted to other anomalies such as slips, intrusions, or posture changes.

---

## 🚀 Key Features

- ⚙️ YOLOv10-based Anomaly Detection
- 🔔 ROS1-based multi-node architecture
- 📡 Server, Display, and Response nodes for real-time actions
- 🎧 Optional: Audio file triggers
- 📩 Optional: SMS/Email alerts via Twilio
- 🧠 Train your own model for different anomaly types

---

## 🧩 Project Structure

Anomaly_detection/
├── detection/ # YOLOv10 AI detection logic
│ ├── detector.py # Real-time webcam detection + message publishing
│ └── model/ # Trained weights and config files
│
├── ros_communication/ # ROS1-compatible nodes
│ ├── server_node.py # Listens for alerts and publishes ROS messages
│ ├── display_node.py # Visualizes/logs the anomaly
│ └── response_node.py # Triggers robot behavior or external alerts
│
├── alert_system/ # SMS/email alert integration via Twilio
├── audio_files/ # Optional sound input
└── README.md

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/siddhantrane31/Anomaly_detection.git
cd Anomaly_detection
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Ensure ROS1 (Melodic or Noetic) is installed and sourced properly.

🧠 Custom Training for Other Anomalies
The YOLOv10 model is flexible and can be trained on any anomaly type.

✅ Example Use Cases:
Detecting people loitering or trespassing

Fire, smoke, or hazardous materials

Sudden collapse or motionless states

Equipment malfunctions or breakages

🔧 How to Do It:
Collect and label your dataset using tools like Roboflow or CVAT.

Train YOLOv10 on your custom dataset.

Export the .pt or .onnx model and place it in detection/model/.

Update detector.py to use your classes.

Integrate your custom output with ROS by publishing the corresponding message.

The ROS server node will still receive and broadcast the new anomaly type — just ensure your message strings match across detector.py and server_node.py.

📡 ROS Node Pipeline
Node	Description
server_node.py	Receives alert from detection module and publishes ROS topic
display_node.py	Subscribes to topic, logs/displays alert info
response_node.py	Subscribes to topic, triggers robot alert/response action

Run in separate terminals:

bash
Copy
Edit
roscore
rosrun ros_communication server_node.py
rosrun ros_communication display_node.py
rosrun ros_communication response_node.py
🧪 Real-Time Workflow
detector.py detects anomaly via webcam or video feed

Sends "fall_detected" or any custom alert (e.g. "fire_alert")

ROS server_node.py receives and publishes

display_node.py logs, and response_node.py takes appropriate action

📨 Optional: SMS/Email Alerts
Enable Twilio in the alert_system/ module. You can trigger it from:

detector.py

response_node.py (recommended)

📝 Contribution Notes
Upload your own audio files into /audio_files/

Modify YOLO classes and message labels as needed

Keep ROS topic structure consistent when changing message types

📚 References
Rane, S. (2024). Automated Anomaly Detection and Reporting System for Mobile Robots

Group Project: Robot Swarm Communication using ROS in Public Spaces

📬 Contact
If you have questions, suggestions, or want to contribute, feel free to:

Open an issue on this repository

Connect via GitHub: @siddhantrane31
