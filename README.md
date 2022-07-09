# Google Street View Images Blur Detection Web Application 
<img width="999" alt="Screenshot 2022-06-30 at 21 23 20" src="https://user-images.githubusercontent.com/43514418/176760922-8a66e9f2-d444-453f-a081-ada8644de074.png"> <br>
<img width="1019" alt="Screenshot 2022-06-29 at 22 11 41" src="https://user-images.githubusercontent.com/43514418/176536257-e6b5123c-88f1-43bb-9a09-be0e1e267ddc.png">
<img width="1077" alt="Screenshot 2022-06-29 at 21 39 16" src="https://user-images.githubusercontent.com/43514418/176536319-ce4e30da-eefb-47d2-a69f-c23e5f391148.png">
**Steps** 
clone repository and copy  **model.h5**  file from previous [steps](https://github.com/MasoudMoeini/Google-Street-View-Images-Blur-Detection) into cloned repository folder <br/>
**RUN following commands:**  <br/>
```
cd tensorflow-flask-web-application
```
```
python3 -m venv venv 
```
```
. venv/bin/activate 
``` 
```
pip install --upgrade pip 
pip install Flask 
pip install numpy 
pip install tensorflow 
pip install pillow 
pip3 install opencv-python 
```
**Run the application**  <br/>
```
python main.py
```
**Access to the Application on browser**  <br/>
copy http://localhost:7000 on your browser<br/>
**To stop running app use CTRL+C**  <br/>
**To deativate python virtual environmet:**  <br/>
```
deactivate 
```
