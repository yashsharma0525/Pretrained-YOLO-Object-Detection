import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from ultralytics import YOLO

# ---------------- SETTINGS ----------------
MODEL_NAME = "yolov8m.pt"   # accuracy badhane ke liye (n < s < m < l < x). Slow PC ho to "yolov8s.pt"
DEFAULT_CONF = 0.50         # 0.5 se kam confidence wali detection ignore
IMG_SIZE = 640

# Sirf ye classes detect hongi (airplane jaisi galat cheezein hat jayengi).
# Saari classes detect karni ho to: ALLOWED_CLASSES = None
ALLOWED_CLASSES = [
    "person", "book", "bottle", "cup", "laptop", "cell phone",
    "chair", "tv", "keyboard", "mouse", "backpack", "clock",
]
# ------------------------------------------

model = YOLO(MODEL_NAME)

# class names -> ids
if ALLOWED_CLASSES:
    CLASS_IDS = [i for i, n in model.names.items() if n in ALLOWED_CLASSES]
else:
    CLASS_IDS = None


def run_realtime():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Webcam nahi khul rahi.")
        return

    win = "Realtime Detection (q = back)"
    cv2.namedWindow(win)
    # slider: 0-100 => confidence 0.00-1.00
    cv2.createTrackbar("Confidence %", win, int(DEFAULT_CONF * 100), 100, lambda x: None)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        conf = max(cv2.getTrackbarPos("Confidence %", win), 5) / 100
        results = model(frame, conf=conf, classes=CLASS_IDS,
                        imgsz=IMG_SIZE, verbose=False)
        annotated = results[0].plot()

        cv2.imshow(win, annotated)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        # window cross (X) se band kiya ho to bhi nikal jao
        if cv2.getWindowProperty(win, cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


def run_image():
    path = filedialog.askopenfilename(
        title="Image select karo",
        filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.webp")],
    )
    if not path:
        return

    img = cv2.imread(path)
    if img is None:
        messagebox.showerror("Error", "Image read nahi ho payi.")
        return

    results = model(img, conf=DEFAULT_CONF, classes=CLASS_IDS,
                    imgsz=IMG_SIZE, verbose=False)
    annotated = results[0].plot()

    # badi image ko screen ke hisaab se chhota karo
    h, w = annotated.shape[:2]
    scale = min(1000 / w, 700 / h, 1.0)
    if scale < 1.0:
        annotated = cv2.resize(annotated, (int(w * scale), int(h * scale)))

    # detected objects ka summary
    names = [model.names[int(c)] for c in results[0].boxes.cls]
    print("Detected:", names if names else "Kuch nahi mila")

    win = "Image Detection (s = save, q = back)"
    cv2.imshow(win, annotated)
    while True:
        key = cv2.waitKey(50) & 0xFF
        if key == ord("s"):
            out = path.rsplit(".", 1)[0] + "_detected.jpg"
            cv2.imwrite(out, results[0].plot())
            messagebox.showinfo("Saved", f"Saved: {out}")
        if key == ord("q"):
            break
        if cv2.getWindowProperty(win, cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()


def launch(func):
    root.withdraw()
    try:
        func()
    finally:
        root.deiconify()


# ---------------- MENU UI ----------------
root = tk.Tk()
root.title("YOLO Object Detection")
root.geometry("340x240")
root.resizable(False, False)

tk.Label(root, text="YOLO Object Detection", font=("Arial", 15, "bold")).pack(pady=15)
tk.Label(root, text="Mode select karo:", font=("Arial", 11)).pack()

tk.Button(root, text="📷  Realtime (Webcam)", font=("Arial", 12), width=24,
          command=lambda: launch(run_realtime)).pack(pady=8)
tk.Button(root, text="🖼️  Image Upload", font=("Arial", 12), width=24,
          command=lambda: launch(run_image)).pack(pady=8)
tk.Button(root, text="Exit", width=10, command=root.destroy).pack(pady=8)

root.mainloop()
