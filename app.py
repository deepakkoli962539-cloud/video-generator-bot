from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Ye line aapke index.html design ko load karegi
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def make_video():
    text = request.form.get('text', 'Hello')
    output_file = "voice.mp3"
    # AI Voice banane ki command
    subprocess.run(f'edge-tts --text "{text}" --write-media {output_file}', shell=True)
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
