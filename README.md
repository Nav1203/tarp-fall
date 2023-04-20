# YOLOv5 Fall Detection Model

This repository contains a YOLOv5 based fall detection model that is capable of sending a WhatsApp and Telegram message on detection of a fall event. The model is also integrated with a Firebase database to store the detection results.
## Video Demo Link
Here is the link showing the live video demo of the working of the project

Link: https://youtu.be/OPHAdy2K1EI

## About Us
This project was built by our team (Aayush Krishna, Lakshmi Rajeev, Renil Augustine Baby and Navaneeth Amarnath) as part of our J component for the course Technical Answers to Real World Problems. We have built it to address the safety of the elderly in our homes especially at night time which when they are highly exposed to falling and hurting themselves. We intend to shorten the response time taken by people to get to the victim by alerting all nearby guardians as well as health authorities once a fall has been detected. This model can easily be integrated to existing surveilance systems or can work well with budget camera surveilance model built by us using an ESP32 CAM module.

## About the Model
The model was trained on the fall dataset from kaggle which includes about 500 different images and does a ternary classification, that is classifies into sitting, walking and fall detected with a confidence level also to ensure better results.

Dataset Link

https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset

## Requirements

To run the model, you need to have the following software installed on your system:

- Python 3.7 or later
- PyTorch 1.8 or later
- OpenCV 4.5 or later
- TensorFlow 2.4 or later
- Pyrebase4
- heyoo (Whatsapp API)
- requesrs (to send requests to Telegram API)

## Installation

1. Clone this repository using `git clone https://github.com/Nav1203/tarp-fall.git`
2. Install the required packages by running `pip install -r requirements.txt`
3. Create a Firebase project and substitute the credentials to the test1.py file.

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

## Credits

The fall detection model is based on the YOLOv5 implementation by Ultralytics LLC.
