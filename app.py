import subprocess
import sys

# Zabardasti moviepy aur edge-tts install karne ke liye
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from moviepy.editor import AudioFileClip, ColorClip
except ImportError:
    install('moviepy')
    from moviepy.editor import AudioFileClip, ColorClip

try:
    import edge_tts
except ImportError:
    install('edge-tts')

from flask import Flask, render_template, request, send_file
import os
import asyncio

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def make_video():
    text = request.form.get('text', 'Hello')
    audio_file = "voice.mp3"
    output_video = "finance_video.mp4"

    # AI Voice generate karna
    subprocess.run(f'edge-tts --text "{text}" --write-media {audio_file}', shell=True)
    
    # Video Visuals banana
    audio = AudioFileClip(audio_file)
    bg = ColorClip(size=(1080, 1920), color=(15, 23, 42), duration=audio.duration)
    
    final_video = bg.set_audio(audio)
    final_video.write_videofile(output_video, fps=24, codec="libx264")
    
    return send_file(output_video, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
