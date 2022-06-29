import numpy as np
from tensorflow import keras
from keras import layers
from keras.models import load_model
from PIL import Image
import cv2

def prediction(file):
  model = load_model("new_model.h5")
  image = Image.open(file)
  image = image.resize((224,224))
  img= np.asarray(image)
  #img= cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
  image= np.asarray(image).astype(np.float32)/ 255.0
  image = np.expand_dims(image, -1)
  image = np.expand_dims(image, 0)
  pred = model.predict(image)
  predicted_class = ((pred[1])[0])[0]
  predicted_label = (((pred[0])[0])*255.0).astype(np.uint8)
  blackFrame = np.zeros((224,224, 3), dtype = "uint8")
  whiteFrame = 255 * np.ones((224,224,3), np.uint8)
  predicted_label=np.where(predicted_label>=210,whiteFrame,blackFrame)
  #generating mask from predicted label
  cyan = np.full_like(img,(80, 229, 235))
  blend = 0.5
  img_cyan = cv2.addWeighted(img, blend, cyan, 1-blend, 0)
  predicted_label = np.where(predicted_label==255, img_cyan, img)
  #predicted_label =cv2.cvtColor(predicted_label , cv2.COLOR_BGR2RGB)
  predicted_label = Image.fromarray(predicted_label)
  print(predicted_class)
  if (predicted_class>0.5):
    predicted_class = 'CLASS 1.0 ->NO BLUR image'
  else:
    predicted_class= 'CLASS 0.0 ->BLUR image' 
  return predicted_class , predicted_label