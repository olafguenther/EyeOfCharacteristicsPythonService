#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Eye Of Characteristics Analyzer.
# Copyright (C) 2019 IBM Deutschland
# Author: Lars Dittert <lars.dittert@de.ibm.com>
#
# Base64 decoding and encoding
#

import base64

class Format:
    def __init__(self):
        pass

    @classmethod
    def base_to_file(self, base_string, path):
        fh = open(path, "wb")
        fh.write(base64.b64decode((base_string)))
        fh.close()

    @classmethod
    def file_to_base(self, path):
        with open(path, "rb") as imageFile:
            encoded_file = base64.b64encode(imageFile.read())
        return encoded_file
