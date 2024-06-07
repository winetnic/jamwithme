Nicolas Winet 
Stolzestrasse 3
8006 Zürich
079 567 37 39 
winetnic@stundets.zhaw.ch
TZDSb


Motivation: Musicians often need instrumental versions of songs to practice or perform along with. Creating an application that automatically removes vocals from a song can save time and provide an essential tool for musicians.

Problem Statement: The project aims to develop a web application where users can upload a .wav file, and the application processes the audio to remove the vocals, generating a jam track.

Relevance: This project leverages both audio processing and web development techniques, showcasing the practical application of machine learning and signal processing in a user-friendly web application.

-----------------

Requirements:
Python (env) 3.10.11
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
Reggae - Gentleman - The Light Within
Soul - Jamie Lidell - Another Day
Electronica - Jamiroquai - Hot Tequila Brown
Rap - Jurassic 5 - Work It Out
Pop - Puggy - When You Know
Rock - The Black Keys - Lonely Boy

Sample Data (Youtube)

Jazz - Norah Jones - https://www.youtube.com/watch?v=fd02pGJx0s0
Trip Hop - Massive Attack - https://www.youtube.com/watch?v=u7K72X4eo_s
Pop - Michael Jackson - https://www.youtube.com/watch?v=QNJL6nfu__Q
Hip Hop - Eminem - https://www.youtube.com/watch?v=eJO5HU_7_1w
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

-----------------

Validation of the Model
To ensure the robustness and reliability of the JamWithMe model for separating vocals from instrumental tracks, I conducted a comprehensive validation process. This involved both human evaluations and numerical analyses to compare the model's performance against benchmarks.

Human Evaluation

I designed a survey to gather qualitative feedback from users, including both musicians and non-musicians. The survey presented participants with original music tracks and their separated component (instrumental). Participants were asked to rate the the purity of the instrumental, and their overall satisfaction with the separation quality. This human-centered approach helps me understand how well the model meets user expectations and identify areas for improvement.

Example of Survey Questions:

Purity of Instrumentals:
How pure is the instrumental track? (1-5)
Overall Satisfaction:
How satisfied are you with the separation quality? (1-5)
Please provide any specific feedback or comments.

Numerical Methods

To complement the human evaluation, I employed numerical methods to quantitatively assess the model's performance. One key metric used was the Signal-to-Distortion Ratio (SDR), which measures the quality of the separated signals by comparing them to the original tracks. 

Comparative Analysis

I also compared the model's performance with state-of-the-art benchmarks such as Open-Unmix and Demucs. By running these benchmark models on the same dataset and comparing the results, I can objectively evaluate the relative performance of my model in terms of both numerical metrics and human satisfaction.

Results
By combining human evaluations with numerical analyses, I aim to provide a comprehensive validation of the JamWithMe model. This multi-faceted approach ensures that my model not only performs well in terms of metrics but also meets user expectations in real-world applications. The insights gained from this validation process will guide future improvements and help me achieve the highest possible quality in instrumental separation.