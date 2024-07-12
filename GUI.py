# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:30:21 2024

@author: jayth
"""

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os

count = 0

def takeImage():
    global count
    if not os.path.isdir("webcamImages"):
        os.mkdir("webcamImages")
    _, frame = webcam.read()
    cv2.imwrite(f"webcamImages/{count}.jpg", frame)
    count+=1

def getVideo():
    _, frame = webcam.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    image = Image.fromarray(image)
    
    image = ImageTk.PhotoImage(image)
    
    webcamVideo.image = image
    webcamVideo.configure(image=image)
    webcamVideo.after(1, getVideo)
    
    
    
webcam = cv2.VideoCapture(0)

window = tk.Tk()

window.title("Image Taker")
imageTakeButton = tk.Button(window, text = "Take Image", command= lambda:takeImage())
webcamVideo = tk.Label(window)

getVideo()

imageTakeButton.pack()
webcamVideo.pack()

window.mainloop()

webcam.release()