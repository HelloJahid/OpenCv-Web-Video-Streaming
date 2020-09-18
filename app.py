# importing modules 
from flask import Flask, render_template, Response
from camera import VideoCamera
  
# declaring app name 
app = Flask(__name__) 
  

# defining home page 
@app.route('/') 
def homepage():
    return render_template("index.html") 


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__': 
    app.run(use_reloader = True, debug = True) 
