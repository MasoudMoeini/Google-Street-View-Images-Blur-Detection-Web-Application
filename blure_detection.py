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
  image = Image.open(file)
  image = image.resize((224,224))
  image= np.asarray(image).astype(np.float32)/ 255.0
  #image= np.asarray(Image.open(file)).astype(np.float32)/ 255.0
  image = np.expand_dims(image, -1)
  image = np.expand_dims(image, 0)
  pred = model.predict(image)
  predicted_class = ((pred[1])[0])[0]
  predicted_label = (((pred[0])[0])*255.0).astype(np.uint8)
  #predicted_label = np.where(predicted_label==255, img_cyan, img)
  predicted_label = Image.fromarray(predicted_label)
  print(predicted_class)
  if (predicted_class>0.5):
    predicted_class = 'CLASS 1.0 NO BLUR image'
  else:
    predicted_class= 'CLASS 0.0 BLUR image' 
  return predicted_class , predicted_label