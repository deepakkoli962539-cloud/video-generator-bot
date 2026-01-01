from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

@app.route('/make_video', methods=['POST'])
def make_video():
    data = request.json
    script = data.get('script', 'Hello')
    # Voice banane ki command
    subprocess.run(f'edge-tts --text "{script}" --write-media voice.mp3', shell=True)
    return send_file("voice.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
