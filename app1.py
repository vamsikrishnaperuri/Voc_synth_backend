import io
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os
import speech_recognition as sr
import scipy.io.wavfile as wavfile
import wave
import base64


app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\vamsi\venv\New folder\flaskupload'

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    print("HI")
    
    if 'audiofile' not in request.files or 'text' not in request.form:
        print("Not file selected")
        return 'No file part'

    file = request.files['audiofile']
    text_data = request.form['text']
    print("audiofile Sucessfully recieved")
    
    if file and text_data:   
        with open("flaskupload/output_audio1.wav", "wb") as output_file:  # Open in binary write mode
            output_file.write(file.read())
        # recognizer = sr.Recognizer()
        # Convert the blob to an AudioFile
        # with sr.AudioFile(io.BytesIO(file.read())) as source:
        #     audio = recognizer.record(source)
        print("audio file uploaded successfully")

        # text_file_path = os.path.join('flaskuploads', text_data['text'])
        with open("flaskupload/outputtext1.txt", 'w') as text_file_handle:
            text_file_handle.write(text_data)
        print("Text file uploaded successfully")

        # try:
            # text = recognizer.recognize_google(audio)
            # print("Recognized text:", text)
        # except sr.UnknownValueError:
        #     print("Could not recognize audio.")
        return 'Files uploaded successfully'
    



if __name__ == '__main__':
    app.run(debug=True,)