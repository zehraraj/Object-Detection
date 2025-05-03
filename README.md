# Object-Detection

This project uses the **YOLO** (You Only Look Once) algorithm for **real-time object detection**. YOLO is a state-of-the-art object detection algorithm that identifies objects in images and videos with high speed and accuracy. This module was used for a hardware-based proctoring tool **designed to reduce cheating during online exams**. It used an external USB camera placed on a rotating mount to capture the student’s surroundings beyond the laptop screen. The system tracked motion and raised alerts if unusual activity was detected. It helped invigilators get a wider view during remote exams, improving the reliability of online assessments. I worked on the system integration, camera logic, and overall testing.



---

## Features
- **Real-Time Detection:** Detect objects in real-time using YOLO.
- **Jupyter Notebook Integration:** Run the implementation easily in a Jupyter Notebook environment.
- **Customizable:** Adapt the YOLO model to work with custom datasets and detection scenarios.

---

## Getting Started

### Prerequisites
- Python (version 3.6 or above)
- Jupyter Notebook
- Required Python libraries: `pip install -r requirements.txt` (add a `requirements.txt` file listing necessary libraries)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/zehraraj/Object-Detection.git
   cd Object-Detection


2. Set up the environment:
   ```bash
   pip install -r requirements.txt



**### How to Use**
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
2. Open the YOLO.ipynb notebook within the repository.
3. Run the cells sequentially as per the instructions to detect objects in images or videos.
