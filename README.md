<h1 align="center">🖼️ Image Compressor using Max Pooling</h1>


## Project Overview :

- This project is a Streamlit-based Image Compression Web Application that compresses images using the Max Pooling technique, a concept widely used in Computer Vision and Convolutional Neural Networks (CNNs).
- The application reduces image size while preserving important visual features by applying pooling operations separately on RGB channels.

## Features :

- Upload images directly from your device
- Image compression using Max Pooling
- Before vs After comparison
- Automatic size reduction display
- Interactive Web Interface

 ## Compression Technique :

The application uses:

**Max Pooling Algorithm :**

Max Pooling reduces image dimensions by selecting the maximum pixel value from a defined window.

**Steps:**

1. Image converted into NumPy array
2. RGB channels separated
3. Max pooling applied on each channel
4. Channels merged again
5. Compressed image generated

Main implementation available in: https://image-compreappr-by-max-pooling.streamlit.app/

## Tech Stack:

| Technology   | Purpose           |
| ------------ | ----------------- |
| Python       | Programming       |
| Streamlit    | Web App Interface |
| NumPy        | Matrix Operations |
| Pillow (PIL) | Image Processing  |



## Project Structure:

```
Image-Compressor-By-Max-Pooling/
│
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── img_compressor1.png
└── requirements.txt
```

## How It Works :

1. User uploads an image.
2. Image is converted into RGB arrays.
3. Max Pooling operation compresses image dimensions.
4. Compressed image is displayed.
5. Size comparison is shown instantly.
   

## Application Output :

- Original Image
- Compressed Image
- Storage Size Comparison
