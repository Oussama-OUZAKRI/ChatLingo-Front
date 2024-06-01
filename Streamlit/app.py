import streamlit as st
from audiorecorder import audiorecorder
from pydub import AudioSegment
import io
import os
import json
import asyncio
import websockets
import threading

# Fonction pour envoyer et recevoir des messages via WebSocket
async def websocket_communication(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response

# Fonction pour gérer la communication WebSocket dans un thread séparé
def run_websocket_communication(message, response_container):
    uri = "ws://localhost:8765"
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(websocket_communication(uri, message))
    response_container.append(response)

def main():
    st.title("ChatLingo")
    st.subheader("Your Personal Language Learning Companion")
    st.markdown("Welcome to ChatLingo! Start chatting to practice your language skills.")

    with st.sidebar:
        st.header('🧭 Navigation')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link('pages/about_page.py', label='About our team', icon='🌟')
        st.page_link('pages/contact_page.py', label='Contact us', icon='📧')
        st.page_link('pages/help_page.py', label='Help', icon='❓')
        st.markdown('---')

    # Chat input
    prompt = st.chat_input("Say something")
    if prompt:
        st.write("You said: ", prompt)
        response_container = []
        thread = threading.Thread(target=run_websocket_communication, args=(json.dumps({"message": prompt}), response_container))
        thread.start()
        thread.join()
        if response_container:
            st.write("Bot response: ", response_container[0])

    # Upload image
    uploaded_img = st.file_uploader("Upload your image")
    if uploaded_img:
        st.image(uploaded_img, caption="Uploaded Image", use_column_width=True)
        # Here you can add your logic to handle the uploaded image

    # Record audio with a progress bar
    st.markdown("## Record your voice")
    audio = audiorecorder("Click to record", "Click to stop recording")

    if len(audio) > 0:
        # Simulate a progress bar for recording
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            progress_bar.progress(percent_complete + 1)

        # To play audio in frontend:
        st.audio(audio.export().read())

        # To save audio to a file, use pydub export method:
        audio_file = io.BytesIO()
        audio.export(audio_file, format="wav")
        audio_file.seek(0)
        with open("audio.wav", "wb") as f:
            f.write(audio_file.read())

        # Read the audio file properties
        audio_file.seek(0)
        try:
            audio_segment = AudioSegment.from_file(audio_file, format="wav")
            st.write(f"Frame rate: {audio_segment.frame_rate}, Frame width: {audio_segment.frame_width}, Duration: {audio_segment.duration_seconds} seconds")
        except Exception as e:
            st.error(f"Error processing audio file: {e}")
        
if __name__ == "__main__":
    # Set FFmpeg path if not added to environment variables
    os.environ["PATH"] += os.pathsep + "C:\\Users\\Oussama Ouzakri\\Desktop\\ffmpeg\\bin\\ffmpeg.exe"
    main()
