import tensorflow as tf
import tensorflow.keras as keras


import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


IMG_HEIGHT = 128
IMG_WIDTH = 128
ORIG_HEIGHT = 360
ORIG_WIDTH = 640


def load_model(path: str):
    return keras.models.load_model(path)


def capture_frames(stream_path: str, callback: function):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))  # added this line
        success, image = vidcap.read()
        if success:
            cv2.imwrite(
                pathOut + "\\frame%d.jpg" % count, image
            )  # save frame as JPEG file
        count = count + 1


if __name__ == "__main__":
    prediction_model = tf.keras.models.load_model("mobilenet_v3_transferred.h5")
