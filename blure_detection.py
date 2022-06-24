import numpy as np
from tensorflow import keras
from keras import layers
from keras.models import load_model
from PIL import Image

def pred_num(pred_val):
  for i in range(10):
    if (pred_val[i] <0.5):
      pred_val[i]=0
    else:
      pred_val[i]=1
      num=i
  return num


def prediction(file):
  model = load_model("new_model.h5")
  image= np.asarray(Image.open(file)).astype(np.float32)/ 255.0
  image = np.expand_dims(image, -1)
  image = np.expand_dims(image, 0)
  pred = model.predict(image)
  predicted_class=(((pred[0])[1])[0])[0]
  if (predicted_class>0.5):
    predicted_class=1.0
  else:
    predicted_class=0.0
  return predicted_class