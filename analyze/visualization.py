#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Eye Of Characteristics Analyzer.
# Copyright (C) 2019 IBM Deutschland
# Author: Lars Dittert <lars.dittert@de.ibm.com>
#
# This file contains the functions which are necessary to visualize the prediction results.
#

import cv2

class Visualization:

    BBOX_COLOR = (0, 255, 0)
    BBOX_COLOR_DARK = (0, 0, 0)    
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    POSITION_FASHION_TEXT = (25, 25)

    def __init__(self):
        pass

    @classmethod
    def draw_face_bounding_box(self, x1, y1, x2, y2, image):
        cv2.rectangle(image, (x1, y1), (x2, y2), Visualization.BBOX_COLOR, 1)

    @classmethod
    def write_facial_results(self, x, y, image, age, gender, emotion):
        result = gender + ", " + age + ", " + emotion
        cv2.putText(image, result, (x, y), Visualization.FONT, 0.8, Visualization.BBOX_COLOR, 1, cv2.LINE_AA)

    @classmethod
    def write_fashion_results(self, image, fashion):
        cv2.putText(image, fashion, Visualization.POSITION_FASHION_TEXT, Visualization.FONT, 0.8, Visualization.BBOX_COLOR_DARK, 1, cv2.LINE_AA)