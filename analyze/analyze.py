#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Eye Of Characteristics Analyzer.
# Copyright (C) 2019 IBM Deutschland
# Author: Lars Dittert <lars.dittert@de.ibm.com>
#
# This file is the main file to analyze images and predict them.
#

import dlib
import numpy as np
import cv2

import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.models import load_model

class Analysis:

    GENDER_MODEL_PATH = './saved_models/gender_model.h5'
    AGE_MODEL_PATH = './saved_models/age_model.h5'
    DEEPFASHION_MODEL_PATH = './saved_models/deepfashion_model.h5'
    FACIAL_EXPRESSION_MODEL_PATH = './saved_models/facial_expression_model.h5'

    GENDER_MODEL = load_model(GENDER_MODEL_PATH)
    AGE_MODEL = load_model(AGE_MODEL_PATH)
    DEEPFASHION_MODEL = load_model(DEEPFASHION_MODEL_PATH)
    FACIAL_EXPRESSION_MODEL = load_model(FACIAL_EXPRESSION_MODEL_PATH)

    GENDER_DICT = {0: "female", 1: "male"}
    AGE_DICT = {0: "0-9", 1: "10-19", 2: "20-29", 3: "30-39", 4: "40-49", 5: "50-59", 6: "60+"}
    LABEL_DICT = {1: "short sleeve top", 2: "long sleeve top", 3: "short sleeve outwear", 4: "long sleeve outwear", 5: "vest", 6: "sling", 7: "shorts", 8: "trousers", 9: "skirt", 10: "short sleeve dress", 11: "long sleeve dress", 12: "vest dress", 13: "sling dress"}
    EMOTION_DICT = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}

    HOG_FACE_DETECTOR = dlib.get_frontal_face_detector()

    def __init__(self):
        pass

    @classmethod
    def detect_faces(self, grayscale_image):
        return Analysis.HOG_FACE_DETECTOR(grayscale_image)

    @classmethod
    def crop_image_gray(self, image, width, height):
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(image, (width, height)), -1), 0)
        return cropped_img

    @classmethod
    def crop_image(self, image, width, height):
        cropped_img = np.expand_dims(cv2.resize(image, (width, height)), 0)
        return cropped_img

    @classmethod
    def predict_gender(self, roi_gray):
        cv2.normalize(roi_gray, roi_gray, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = Analysis.GENDER_MODEL.predict(roi_gray)
        label = Analysis.GENDER_DICT[int(np.argmax(prediction))]
        return label

    @classmethod
    def predict_age(self, roi_gray):
        cv2.normalize(roi_gray, roi_gray, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = Analysis.AGE_MODEL.predict(roi_gray)
        label = Analysis.AGE_DICT[int(np.argmax(prediction))]
        return label

    @classmethod
    def predict_fashion(self, frame):
        cv2.normalize(frame, frame, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = Analysis.DEEPFASHION_MODEL.predict(frame)
        label = Analysis.LABEL_DICT[int(np.argmax(prediction))]
        return label

    @classmethod
    def predict_facial_expression(self, roi_gray):
        cv2.normalize(roi_gray, roi_gray, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = Analysis.FACIAL_EXPRESSION_MODEL.predict(roi_gray)
        label = Analysis.EMOTION_DICT[int(np.argmax(prediction))]
        return label
