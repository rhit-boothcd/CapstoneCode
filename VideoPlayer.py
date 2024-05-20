import tkinter as tk
import cv2
from PIL import Image, ImageTk


class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.root.geometry("640x480")
        self.cap = cv2.VideoCapture(video_path)
        self.label = tk.Label(root)
        self.label.pack()
        self.show_frame()

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame_image = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=frame_image)
            self.label.image = frame_image
            self.label.after(10, self.show_frame)


if __name__ == "__main__":
    video_path = "fish-spinning.mp4"  # Replace with your video file path
    root = tk.Tk()
    player = VideoPlayer(root, video_path)
    root.mainloop()