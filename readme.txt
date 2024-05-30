Motivation: Musicians often need instrumental versions of songs to practice or perform along with. Creating an application that automatically removes vocals from a song can save time and provide an essential tool for musicians.

Problem Statement: The project aims to develop a web application where users can upload a .wav file, and the application processes the audio to remove the vocals, generating a jam track.

Relevance: This project leverages both audio processing and web development techniques, showcasing the practical application of machine learning and signal processing in a user-friendly web application.

-----------------

Requirements:
Python 3.10.11
pip install spleeter
pip install streamlit
pip install protobuf==3.20.0
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

-----------------

Run application -> streamlit run jamwithme_streamlit.py

-----------------

Sample Data (.wav)

POP - Aloe Blacc - I Need A Dollar
Rock - Foo Fighters - The Pretender
Reggea - Gentleman - The Light Within
Soul - Jamie Lidell - Another Day
Electronica - Jamiroquai - Hot Tequila Brown
Rap - urassic 5 - Work It Out
Pop - Puggy - When You Know
Rock - The Black Keys - Lonely Boy

Sample Data (Youtube)

Jazz - Norah Jones - https://www.youtube.com/watch?v=fd02pGJx0s0
TriopHop - Massive Attack - https://www.youtube.com/watch?v=u7K72X4eo_s
Pop - Michael Jackson - https://www.youtube.com/watch?v=QNJL6nfu__Q
HipHop - Eminem - https://www.youtube.com/watch?v=eJO5HU_7_1w
Country - Chris Stableton - https://www.youtube.com/watch?v=4zAThXFOy2c
Punk - Sex Pistols - https://www.youtube.com/watch?v=yqrAPOZxgzU

-----------------

How does it work?

1. Pre-processing
Audio Loading: The input audio file is loaded and converted into a waveform.
Short-Time Fourier Transform (STFT): The waveform is transformed into a spectrogram using the STFT, which provides a time-frequency representation of the audio signal.

2. Model Architecture
Spleeter uses deep neural networks for source separation. The specific architecture used in Spleeter includes:
U-Net Architecture: This is a type of convolutional neural network (CNN) originally developed for biomedical image segmentation. The U-Net consists of an encoder and a decoder:
Encoder: The encoder consists of a series of convolutional layers that progressively reduce the spatial dimensions (time-frequency) while increasing the number of feature maps. This creates a compact representation of the input spectrogram.
Decoder: The decoder consists of a series of transposed convolutional layers that progressively increase the spatial dimensions while reducing the number of feature maps, effectively reconstructing the separated sources from the encoded representation.
Skip Connections: The U-Net architecture includes skip connections that directly connect corresponding layers in the encoder and decoder. This helps in preserving fine details during the reconstruction process.

3. Training
Dataset: Spleeter is trained on a large dataset of mixed audio tracks and their corresponding isolated sources. The training data includes various genres and styles of music to ensure generalization.
Loss Function: During training, the model minimizes a loss function that measures the difference between the predicted separated sources and the ground truth isolated sources. The loss function typically includes terms that measure reconstruction error in both time and frequency domains.
Optimization: The model is trained using stochastic gradient descent (SGD) or similar optimization algorithms to update the weights of the neural network.

4. Inference
Spectrogram Prediction: During inference, the input audio is transformed into a spectrogram, which is then passed through the trained neural network. The network outputs spectrograms for each separated source.
Inverse STFT: The predicted spectrograms for each source are transformed back into waveforms using the inverse STFT.
Post-processing: The separated waveforms may undergo additional post-processing steps to enhance quality, such as noise reduction or smoothing.

5. Output
The final output is a set of audio files corresponding to the separated sources (e.g., vocals and accompaniment).