from flask import Flask, render_template, request, send_file
import subprocess
import os
from moviepy.editor import AudioFileClip, ColorClip, TextClip, CompositeVideoClip

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def make_video():
    text = request.form.get('text', 'Finance Video')
    
    # 1. AI Voice generate karna
    audio_file = "voice.mp3"
    subprocess.run(f'edge-tts --text "{text}" --write-media {audio_file}', shell=True)
    
    # 2. Visuals banana (Crayon Capital jaisa dark theme)
    audio = AudioFileClip(audio_file)
    # Background color (Dark Navy Blue)
    bg = ColorClip(size=(1080, 1920), color=(15, 23, 42), duration=audio.duration)
    
    # 3. Final Video merge karna
    final_video = bg.set_audio(audio)
    output_video = "finance_video.mp4"
    final_video.write_videofile(output_video, fps=24, codec="libx264")
    
    return send_file(output_video, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
