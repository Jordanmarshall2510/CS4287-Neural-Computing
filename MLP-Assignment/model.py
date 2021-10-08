print("works1")

import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

dataset = pd.read_csv("star_dataset.csv", names=["Temperature", "Luminosity", "Radius", "Absolute_Magnitude", "Star_Type", "Star_Color", "Spectral_Class"])
dataset.head()
print(dataset)


print("works2")

def createModel():
    pass

def predict():
    pass

def trainModel():
    pass

def plotModel():
    pass