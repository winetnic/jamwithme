import os
import shutil
import streamlit as st
from spleeter.separator import Separator
from pytube import YouTube

def separate_vocals(input_file_path, output_dir):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_file_path, output_dir)

def download_audio_from_youtube(youtube_link, output_dir):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = os.path.join(output_dir, "temp.wav")
    downloaded_file_path = audio_stream.download(output_path=output_dir)
    os.rename(downloaded_file_path, audio_file_path)
    return audio_file_path

def main():
    
    logo_path = "jamwithme.png"
    st.image(logo_path)
    
    st.write("Drop a WAV file and jam on, or share a YouTube link to groove!")

    output_dir = "output/temp"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    uploaded_file = st.file_uploader("WAV file", type="wav")
    youtube_link = st.text_input("Or paste a YouTube link")

    if uploaded_file is not None:
        with st.spinner('Uploading and processing the file...'):
            input_file_path = os.path.join(output_dir, "temp.wav")
            with open(input_file_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            separate_vocals(input_file_path, output_dir)

        st.success('File uploaded and processed successfully!')
        accompaniment_path = os.path.join(output_dir, "temp", "accompaniment.wav")
        if os.path.exists(accompaniment_path):
            st.audio(accompaniment_path, format="audio/wav")
        else:
            st.write("Accompaniment file not found.")

    if youtube_link:
        with st.spinner('Downloading and processing the audio from YouTube...'):
            audio_file_path = download_audio_from_youtube(youtube_link, output_dir)
            separate_vocals(audio_file_path, output_dir)

        st.success('YouTube audio downloaded and processed successfully!')
        accompaniment_path = os.path.join(output_dir, "temp", "accompaniment.wav")
        if os.path.exists(accompaniment_path):
            st.audio(accompaniment_path, format="audio/wav")
        else:
            st.write("Accompaniment file not found.")

if __name__ == "__main__":
    main()
