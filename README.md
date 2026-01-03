# Gesture Bridge

## Overview

**Gesture Bridge** is an AI-powered application designed to assist communication between hearing and speech-impaired individuals and others. Using computer vision and deep learning, it recognizes and translates American Sign Language (ASL) gestures into text or voice in real-time. The application captures hand landmarks via the device's camera, processes them with a deep learning model, and outputs the corresponding ASL character or phrase.



## Features

* **Real-time ASL gesture recognition** using the device camera.
* **Live translation** from ASL gestures to text and/or voice.
* **Hand landmark tracking** for accurate gesture detection.
* **Support for complete ASL alphabet** and common phrases.
* **User-friendly interface** with live feedback.

## Requirements

* Python 3.10+
* OpenCV
* MediaPipe
* Pillow
* NumPy
* Pandas
* Seaborn
* Scikit-learn
* Matplotlib
* TensorFlow

> **Important:** For converting models to TFLite, use TensorFlow v2.16.1 to avoid compatibility issues.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Bhavya0420/Gesture_Bridge.git
cd Gesture_Bridge
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the application:**

```bash
python app.py
```

## Usage

* The app starts in inference mode by default.
* You can interact with the GUI to choose between **Live Voice Recognition** and **Stop**.
* The system listens to your voice and converts recognized words into ASL gestures displayed on the screen.

## Model Training

### Data Collection

1. **Manual Key Points Capturing**

   * Press `k` to log key points.
   * Press uppercase letters `A-Z` to record gestures in `model/keypoint_classifier/keypoint.csv`.

2. **Automated Key Points Capturing**

   * Press `d` to start automated key point logging.
   * Ensure the dataset directory is correctly set in `app.py`.

### Training

* Open `keypoint_classification.ipynb` and run all cells sequentially.
* Update `NUM_CLASSES` and `keypoint_classifier_label.csv` if you change the number of gesture classes.



