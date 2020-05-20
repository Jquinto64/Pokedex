# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:18:27 2019

@author: jquin
"""

import tensorflow as tf
import numpy as np

#converter = tf.lite.TFLiteConverter.from_keras_model_file("C:\\users\\jquin\\desktop\\Pokedex_App_keras\\keras_to_tensorflow\\pokedex.h5")
#tflite_model = converter.convert()
#open("pokedex.tflite", "wb").write(tflite_model)


path = "C:\\Users\\jquin\\Desktop\\ObjectDetector\\models\\research\\object_detection\\inference_graph\\saved_model"
converter = tf.lite.TFLiteConverter.from_saved_model(path)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)


#interpreter = tf.lite.Interpreter("C:\\Users\\jquin\\desktop\\detect.tflite")
#interpreter.allocate_tensors()
#
#print(interpreter.get_input_details()[0]['shape'])  
#print(interpreter.get_input_details()[0]['dtype']) 
#
#
#print(interpreter.get_output_details()[0]['shape'])  
#print(interpreter.get_output_details()[0]['dtype']) 