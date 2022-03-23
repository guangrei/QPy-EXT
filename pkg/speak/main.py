# -*-coding:utf8;-*-
"""
QPy CMD extension
name: speak
description: Speak user generated text.
version: v0.1
author: Damon Kohler
require: ""
"""
__author__ = 'Damon Kohler <damonkohler@gmail.com>'
__copyright__ = 'Copyright (c) 2009, Google Inc.'
__license__ = 'Apache License, Version 2.0'

try:
    import sl4a as android helper
except ImportErorr:
    import androidhelper

droid = androidhelper.Android()
message = droid.dialogGetInput('TTS', 'What would you like to say?').result
droid.ttsSpeak(message)
