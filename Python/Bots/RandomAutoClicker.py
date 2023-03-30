import threading
import time
import os
import sys
import random
import tkinter as tk
from pynput import keyboard, mouse

class AutoClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random Auto Clicker")
        self.root.geometry("400x400")  # Increase the size of the window
        font = ("Montserrat", 12)
        self.root.resizable(False, False)
        self.start_time = 0
        icon_path = ''
        if hasattr(sys, '_MEIPASS'):
            try:
                self.root.iconbitmap(os.path.join(sys._MEIPASS, 'rac.ico'))
            except Exception:
                pass

        # Create variables
        self.delay_from = tk.StringVar(value="0.5")
        self.delay_to = tk.StringVar(value="1.0")
        self.mouse_button = tk.StringVar(value="left")

        # Create widgets
        tk.Label(self.root, text="Random Auto Clicker", font=("Montserrat", 24)).pack(pady=10)

        delay_frame = tk.Frame(self.root)
        delay_frame.pack()
        tk.Label(delay_frame, text="Click Delay (from - to):", font=font).pack(padx=5)
        tk.Label(delay_frame, text="From:", font=font).pack(side=tk.LEFT, padx=5)
        tk.Entry(delay_frame, textvariable=self.delay_from, width=6, font=font).pack(side=tk.LEFT)
        tk.Label(delay_frame, text="To:", font=font).pack(side=tk.LEFT, padx=5)
        tk.Entry(delay_frame, textvariable=self.delay_to, width=6, font=font).pack(side=tk.LEFT)

        tk.Frame(self.root).pack()
        tk.Label(self.root, text="Mouse Button:", font=font).pack(pady=6)
        tk.Radiobutton(self.root, text="Left", variable=self.mouse_button, value="left", font=font).pack(padx=30,
                                                                                                         pady=6)
        tk.Radiobutton(self.root, text="Right", variable=self.mouse_button, value="right", font=font).pack(padx=30,
                                                                                                           pady=6)

        self.status_label = tk.Label(self.root, text="Press F10 to start/stop", font=("Montserrat", 14, "bold"))
        self.status_label.pack(pady=20)
        self.timer_label = tk.Label(self.root, text="", font=("Montserrat", 16, "italic"))
        self.timer_label.pack(pady=10)
        # Create listener for F10 key
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        # Create thread for autoclicker
        self.auto_click_thread = threading.Thread(target=self.auto_click)
        self.auto_click_thread.daemon = True

    def run(self):
        self.root.mainloop()

    def on_press(self, key):
        if key == keyboard.Key.f10:
            if not self.auto_click_thread.is_alive():
                self.start_time = time.time()
                self.status_label.config(text="RAC running...", font=("Montserrat", 14,  "bold"))
                self.auto_click_thread = threading.Thread(target=self.auto_click)
                self.auto_click_thread.daemon = True
                self.auto_click_thread.start()
            else:
                self.auto_click_thread.do_run = False
                elapsed_time = time.time() - self.start_time
                hours = int(elapsed_time / 3600)
                minutes = int((elapsed_time - hours * 3600) / 60)
                seconds = int(elapsed_time - hours * 3600 - minutes * 60)
                time_str = f"Ran for: {hours:02d}h:{minutes:02d}m:{seconds:02d}s"
                self.timer_label.config(text=time_str)
                self.status_label.config(text="RAC stopped.", font=("Montserrat", 14, "bold"))

    def auto_click(self):
        with mouse.Controller() as controller:
            while getattr(threading.current_thread(), "do_run", True):
                delay = random.uniform(float(self.delay_from.get()), float(self.delay_to.get()))
                time.sleep(delay)
                if self.mouse_button.get() == "left":
                    controller.click(mouse.Button.left)
                else:
                    controller.click(mouse.Button.right)


if __name__ == "__main__":
    autoclicker = AutoClicker()
    autoclicker.run()
