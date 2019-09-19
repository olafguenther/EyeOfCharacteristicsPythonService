#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Eye Of Characteristics Analyzer.
# Copyright (C) 2019 IBM Deutschland
# Author: Lars Dittert <lars.dittert@de.ibm.com>
#
# This file handles the communication between user and python webservice

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import json
import datetime
import time
import logging
import cv2
from pathlib import Path
import base64
import simplejson as json

import main
from preprocessing.format import Format
from input_management.input import Input

input = Input()
format = Format()

# create logger
logger = logging.getLogger('eoc')
logger.setLevel(logging.DEBUG)

# Also log debug messages
file_handler = logging.FileHandler('eoc.log')
file_handler.setLevel(logging.DEBUG)

# create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = Flask(__name__, static_url_path='',
            static_folder='frontend/static', template_folder='frontend/templates')
CORS(app)
port = int(os.getenv("PORT")) if os.getenv("PORT") else 5000
logger.info('set server port:' + str(port))


@app.route('/')
def root():
    print('REST-Call: GET: "/"')
    logger.info('REST-Call: GET: "/"')
    return render_template('index.html')


@app.route('/analyze-image', methods=['POST'])
def analyze():
    print('REST-Call: POST: "/analyze-image"')
    logger.info('REST-Call: POST: "/analyze-image"')
    jsonData = request.json
    uploaded_data = jsonData["image"]

    try:
        logger.info('decode uploaded image')
        format.base_to_file(uploaded_data, './upload/uploaded_image.jpg')
        logger.info('start analyzing image')
        input.load_image()
        logger.info('encode image')
        analyzed_image = format.file_to_base('./output/analyzed_output.jpg')
    except Exception as e:
        error = 'Error: ' + str(e)
        analyzed_image = error
        logger.error(error)

    logger.info('return result')
    return json.dumps({"image": analyzed_image})

@app.route('/analyze-video', methods=['POST'])
def analyze_video():
    print('REST-Call: POST: "/analyze-video"')
    logger.info('REST-Call: POST: "/analyze-video"')
    jsonData = request.json
    print(jsonData)
    uploaded_data = jsonData["video"]

    try:
        logger.info('decode uploaded video')
        format.base_to_file(uploaded_data,  './upload/uploaded_video.mov')
        logger.info('start analyzing video')
        input.load_video()
        logger.info('encode video')
        analyzed_video = format.file_to_base('./output/analyzed_output_video.avi')
    except Exception as e:
        error = 'Error: ' + str(e)
        analyzed_video = error
        logger.error(error)

    logger.info('return result')
    return json.dumps({"video": analyzed_video})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
