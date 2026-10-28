# Object Detection with a Pretrained YOLO Model

Object detection using a pretrained YOLOv8 model (Python, OpenCV, Ultralytics). Choose between **realtime webcam detection** and **image upload detection** from a simple menu.

## Team Formation

| Field | Details |
|---|---|
| **Program** | BTech Deep Learning |
| **Semester** | V |
| **Section** | C |
| **Group ID** | BT_DL_17 |
| **Project ID** | DL-017 |
| **Project Title** | Object Detection with a Pretrained YOLO Model |
| **Mentor** | Tanish Rastogi |

### Team Members

| Sr. No. | Student ID | Roll No. | Student Name |
|:---:|:---:|:---:|---|
| 1 | BCS2024214 | 2410303240 | Kushagra Saxena |
| 2 | BCS2024216 | 2410303439 | Satyam Gupta |
| 3 | BCS2024217 | 2410303433 | Sangam Pathak |
| 4 | BCS2024219 | 2410303357 | Prince Kumar Maurya |
| 5 | BCS2024220 | 2410303262 | Mayuri Singh |
| 6 | BCS2024221 | 2410303571 | Yash Sharma (Team Lead) |
| 7 | BCS2024223 | 2410303297 | Monu Rathour |
| 8 | BCS2024224 | 2410303267 | Mohammad Anas Usmani |
| 9 | BCS2024225 | 2410303033 | Aditya Sagar |
| 10 | BCS2024226 | 2410303425 | Saket Sharma |
| 11 | BCS2024227 | 2410303362 | Priyanshu Yadav |
| 12 | BCS2024228 | 2410303247 | Lovely |
| 13 | BCS2024229 | 2410303112 | Arpit Shakya |
| 14 | BCS2024230 | 2410303462 | Shiva Singh |

## About the Project

This project detects objects using a pretrained YOLO (You Only Look Once) model from the Ultralytics library, so no training is needed. The model is trained on the COCO dataset and can detect 80 common objects such as person, phone, bottle, book, laptop, chair and car.

When the app starts, the user can select a mode:

- **Realtime (Webcam):** live detection with an adjustable confidence slider
- **Image Upload:** pick any image from the computer, view the detections and optionally save the result

## How It Works

Input (Webcam frame / Uploaded image) -> YOLO model -> Confidence + class filter -> Bounding box + Label + Confidence -> Display on screen

## Project Structure

```
.
├── detect.py           # main script (menu + webcam + image detection)
├── requirements.txt    # libraries needed
├── README.md           # project documentation
├── LICENSE
└── .gitignore
```

## Requirements

- Python 3.8 or higher
- A working webcam (for realtime mode)
- Internet connection (only for the first run, to download the model)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Pretrained-YOLO-Object-Detection.git
cd Pretrained-YOLO-Object-Detection
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Install the libraries

```bash
pip install -r requirements.txt
```

> `tkinter` comes with standard Python on Windows and Mac. On Ubuntu/Debian run: `sudo apt install python3-tk`

## Run

```bash
python detect.py
```

A menu window opens with two options:

| Mode | How to use | Keys |
|---|---|---|
| Realtime (Webcam) | Click the button, then adjust the **Confidence %** slider | **q** = back to menu |
| Image Upload | Choose an image in the file dialog | **s** = save result, **q** = back to menu |

Saved images are stored next to the original image as `<name>_detected.jpg`.

## Improving Accuracy

YOLOv8 is pretrained on the COCO dataset, which has **no "ceiling fan" class**. Because of this, the model sometimes labels a fan as the closest looking class (for example, airplane). We reduced such false detections by:

1. **Using a larger model:** `yolov8m.pt` instead of `yolov8n.pt`
2. **Higher confidence threshold:** default 0.50, adjustable live with the slider
3. **Class filtering:** only the classes listed in `ALLOWED_CLASSES` are detected

## Settings

Change these at the top of `detect.py`:

| Setting | Default | Description |
|---|---|---|
| `MODEL_NAME` | `yolov8m.pt` | `yolov8n` (fastest) < `s` < `m` < `l` < `x` (most accurate) |
| `DEFAULT_CONF` | `0.50` | Minimum confidence to show a detection |
| `IMG_SIZE` | `640` | Image size used for detection |
| `ALLOWED_CLASSES` | person, book, bottle, ... | Classes to detect. Set to `None` to detect all 80 classes |

Use an external camera by changing the camera index in `run_realtime()`:

```python
cap = cv2.VideoCapture(1)
```

## Troubleshooting

| Problem | Solution |
|---|---|
| Camera does not open | Close other apps using the camera, or try `VideoCapture(1)` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| `No module named tkinter` | Install it: `sudo apt install python3-tk` (Linux) |
| Slow / laggy video | Set `MODEL_NAME = "yolov8n.pt"` or `"yolov8s.pt"` and close other heavy apps |
| Object not detected | Lower the confidence slider, or add the class to `ALLOWED_CLASSES` |
| Model download fails | Check your internet connection and run again |

## Tools Used

- Python
- OpenCV (camera access and display)
- Ultralytics YOLOv8 (pretrained detection model)
- Tkinter (mode selection menu and file dialog)

## Limitations

- Accuracy drops in low light
- Detects only the 80 COCO classes (new objects like a ceiling fan need custom training)
- Speed depends on the laptop hardware

## Mentor

Tanish Rastogi
