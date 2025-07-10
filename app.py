from flask import Flask, render_template, request
from speech.stt import listen
from speech.tts import speak
from brain.agent import ask_jarvis
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.form['query']
    response = ask_jarvis(query)
    speak(response)
    return response

def listen_and_respond():
    while True:
        query = listen()
        if query:
            response = ask_jarvis(query)
            speak(response)

if __name__ == "__main__":
    threading.Thread(target=listen_and_respond).start()
    app.run(debug=True, host='0.0.0.0', port=5000)