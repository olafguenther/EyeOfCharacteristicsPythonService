#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Eye Of Characteristics Analyzer.
# Copyright (C) 2019 IBM Deutschland
# Author: Lars Dittert <lars.dittert@de.ibm.com>
#
# This file is the main file which starts the programm and calls the elementary methods
#

import os
import argparse
import pandas as pd
import cv2

from analyze.visualization import Visualization
from analyze.analyze import Analysis
from input_management.input import Input

__version__ = "1.0.0"

# Create the top-lvl parser
parser = argparse.ArgumentParser()
# Adding the arguments to the parser
parser.add_argument("-i", "--image_path", help="if set, images in path are used instead of webcam")
parser.add_argument("-iv", "--image_video_path", help="if set, video in path are used instead of webcam")
parser.add_argument("-v", "--version", help="print the version number and exit", action="store_true")

args = parser.parse_args()

def main():
    if (args.image_path is None) and (args.image_video_path is None) and (args.version is False):
        input.record_webcam()
        # parser.print_usage()
        # parser._print_message("error: program expected arguments -s/--start and -p/--path")
    elif args.image_path:
        input.load_image(args.image_path)
    elif args.image_video_path:
        input.load_video(args.image_video_path)
    elif args.version:
        # Print the version number and exit
        print(__version__)
        
def start(xlsx):
    return True


if __name__ == '__main__':
    visualizer = Visualization()
    analyzer = Analysis()
    input = Input()
    main()