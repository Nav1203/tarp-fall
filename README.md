# YOLOv5 Fall Detection Model

This repository contains a YOLOv5 based fall detection model that is capable of sending a WhatsApp and Telegram message on detection of a fall event. The model is also integrated with a Firebase database to store the detection results.

## Requirements

To run the model, you need to have the following software installed on your system:

- Python 3.7 or later
- PyTorch 1.8 or later
- OpenCV 4.5 or later
- TensorFlow 2.4 or later
- Firebase Admin SDK
- twilio module (for WhatsApp message)
- telebot module (for Telegram message)

## Installation

1. Clone this repository using `git clone https://github.com/your-username/yolov5-fall-detection.git`
2. Install the required packages by running `pip install -r requirements.txt`
3. Download the YOLOv5 weights file from the official repository by running `python download_weights.py`. This will download the `yolov5s.pt` file to the `weights` directory.
4. Create a Firebase project and substitute the credentials to the test1.py file.

## Usage

To run the model on a video footage, use the following command:

```bash
python detect.py --weights <weights_path> --img 640 --conf 0.25 --source <video_path>
```

To run the model on a live footage like the one from the ESP-32 CAM module,
Run the test1.py, by adding your live footage IP address value to the following line

```bash
cap = cv2.VideoCapture("<IP_Address>")
```

