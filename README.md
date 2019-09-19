# EyeOfCharacteristicsPythonService

EyeOfCharacteristics Python Webservice to analyze images/videos.

[Demo Webservice](http://eoc-webservice-impressive-numbat.eu-de.mybluemix.net)  
[Demo Frontend](http://eye-of-characteristics.eu-de.mybluemix.net/#/)

## Setup
1. Clone or download this repository to your local computer and unpack the archive if necessary
2. Open your console and change (`cd`) to the new directory
3. Type on your command line `pip3 install -r requirements.txt` and press enter 

## How to run script locally

To analyze the live video of your webcam use the following command:
`python3 main.py`

Also you are able to analyze a single image or video:

`python3 main.py -i testing/test.jpg`

`python3 main.py -iv testing/test.mov`

## How to run local python server
1. Complete the setup tutorial
2. Type on your command line `python3 connect.py`
3. Your server will be running on *http://0.0.0.0:5000*

## Setup for deploying in IBM Cloud
1. Clone or download this repository to your local computer and unpack the archive if necessary
2. Open your console and change (`cd`) to the new directory
3. Login to your IBM Cloud account `bx login -sso`
4. Set your target space `bx target --cf -s {SPACE}`
5. Push your application `bx cf push eoc-webservice`

### Basic
1. Open your console
2. Navigate into the directory EyeOfCharacteristicsPythonService
3. Type `python3 main.py`  
**Be sure to use Python 3.x** (Requirements)

### Additional Arguments
Also you can use the following parameter to specialize your request-

usage: `main.py [-h] [-i PATH | -iv PATH] [-v]`

optional arguments:  

| Short       | Long               | Description                             |
| ----------- | ------------------ | --------------------------------------- |
| -h          | --help             | show this help message and exit         |
| -i          | --image_path       | if set, images in path are used instead of webcam |
| -iv         | --image_video_path | if set, video in path are used instead of webcam |
| -v          | --version          | print the version number and exit       |

## Requirements
* Python 3.x
* Console like Linux/macOS Terminal or Windows PowerShell

### Additional Requirement IBM Cloud Setup
* IBM Cloud CLI

## Contributors
* Lars Dittert <lars.dittert@de.ibm.com>

Copyright (C) 2019 IBM Deutschland
