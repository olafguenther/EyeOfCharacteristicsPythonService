#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Eye Of Characteristics Analyzer.
# Copyright (C) 2019 IBM Deutschland
# Author: Lars Dittert <lars.dittert@de.ibm.com>
#
# This file load  images, or starts the webcam
#

from analyze.analyze import Analysis
from analyze.visualization import Visualization

import cv2

visualizer = Visualization()
analyzer = Analysis()

class Input:

    UI_TITLE = 'Eye Of Characteristics'
    BASEPATH_OUTPUT = './output/'
    OUTPUT_IMAGE_PATH = BASEPATH_OUTPUT + 'analyzed_output.jpg'
    OUTPUT_VIDEO_PATH = BASEPATH_OUTPUT + 'analyzed_output_video.avi'

    def __init__(self):
        pass

    def load_image(self, image_path='./upload/uploaded_image.jpg'):
        img = cv2.imread(str(image_path), 1)
        if img is not None:
            gray_frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            faces = analyzer.detect_faces(gray_frame)
            for face in faces:
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()
                h = y2 - y1
                w = x2 - x1
                x_neu = round(x1 - w*0.5)
                y_neu = round(y1 - h*0.5)
                h_neu = y2 - y_neu
                w_neu = x2 - x_neu

                visualizer.draw_face_bounding_box(x1, y1, x2, y2, img)
                roi_gray = gray_frame[y_neu:y1 + h_neu, x_neu:x1 + w_neu]

                try:
                    cropped_small = analyzer.crop_image_gray(roi_gray, 48, 48)
                    cropped_fashion = analyzer.crop_image(img, 200, 200)
                    cropped_gender = analyzer.crop_image_gray(roi_gray, 300, 300)

                    gender_prediction = analyzer.predict_gender(cropped_gender)
                    age_prediction = analyzer.predict_age(cropped_small)
                    fashion_prediction = analyzer.predict_fashion(cropped_fashion)
                    emotion_prediction = analyzer.predict_facial_expression(cropped_small)

                    visualizer.write_facial_results(x1, y1, img, age_prediction, gender_prediction, emotion_prediction)
                    visualizer.write_fashion_results(img, fashion_prediction)

                    cv2.imwrite(Input.OUTPUT_IMAGE_PATH, img)
                except Exception as e:
                    print('Error: ' + str(e))
        else:
            print('Cannot load image')

    @classmethod
    def load_video(self, video_path='./upload/uploaded_video.mov'):
        cap = cv2.VideoCapture(video_path)
 
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        out = cv2.VideoWriter(Input.OUTPUT_VIDEO_PATH, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
        while(cap.isOpened()):
            ret, frame = cap.read()
            try:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                faces = analyzer.detect_faces(gray_frame)
                for face in faces:
                    x1 = face.left()
                    y1 = face.top()
                    x2 = face.right()
                    y2 = face.bottom()
                    h = y2 - y1
                    w = x2 - x1
                    x_neu = round(x1 - w*0.5)
                    y_neu = round(y1 - h*0.5)
                    h_neu = y2 - y_neu
                    w_neu = x2 - x_neu

                    visualizer.draw_face_bounding_box(x1, y1, x2, y2, frame)
                    roi_gray = gray_frame[y_neu:y1 + h_neu, x_neu:x1 + w_neu]

                    try:
                        cropped_small = analyzer.crop_image_gray(roi_gray, 48, 48)
                        cropped_fashion = analyzer.crop_image(frame, 200, 200)
                        cropped_gender = analyzer.crop_image_gray(roi_gray, 300, 300)

                        gender_prediction = analyzer.predict_gender(cropped_gender)
                        age_prediction = analyzer.predict_age(cropped_small)
                        fashion_prediction = analyzer.predict_fashion(cropped_fashion)
                        emotion_prediction = analyzer.predict_facial_expression(cropped_small)

                        visualizer.write_facial_results(x1, y1, frame, age_prediction, gender_prediction, emotion_prediction)
                        visualizer.write_fashion_results(frame, fashion_prediction)
                        out.write(frame)
                    except Exception as e:
                        print('Error: ' + str(e))
            except:
                pass
        cap.release()
        out.release()
        
        

    @classmethod
    def record_webcam(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = analyzer.detect_faces(gray_frame)
            for face in faces:
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()
                h = y2 - y1
                w = x2 - x1
                x_neu = round(x1 - w*0.5)
                y_neu = round(y1 - h*0.5)
                h_neu = y2 - y_neu
                w_neu = x2 - x_neu

                visualizer.draw_face_bounding_box(x1, y1, x2, y2, frame)
                roi_gray = gray_frame[y_neu:y1 + h_neu, x_neu:x1 + w_neu]

                try:
                    cropped_small = analyzer.crop_image_gray(roi_gray, 48, 48)
                    cropped_fashion = analyzer.crop_image(frame, 200, 200)
                    cropped_gender = analyzer.crop_image_gray(roi_gray, 300, 300)

                    gender_prediction = analyzer.predict_gender(cropped_gender)
                    age_prediction = analyzer.predict_age(cropped_small)
                    fashion_prediction = analyzer.predict_fashion(cropped_fashion)
                    emotion_prediction = analyzer.predict_facial_expression(cropped_small)

                    visualizer.write_facial_results(x1, y1, frame, age_prediction, gender_prediction, emotion_prediction)
                    visualizer.write_fashion_results(frame, fashion_prediction)
                except Exception as e:
                    print(str(e))

            cv2.imshow(Input.UI_TITLE, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break