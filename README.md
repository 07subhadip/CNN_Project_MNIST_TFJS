# Serverless MNIST Digit Recognizer

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=07subhadip.CNN_Project_MNIST_TFJS)
[![GitHub license](https://img.shields.io/github/license/07subhadip/CNN_Project_MNIST_TFJS)](https://github.com/07subhadip/CNN_Project_MNIST_TFJS)
![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-Powered-orange)

A deep learning project that deploys a trained CNN model to the web using TensorFlow.js, enabling client-side digit recognition directly in the browser.

### [View Live Demo](https://07subhadip.github.io/CNN_Project_MNIST_TFJS/)

---

## Project Overview

This application serves as a demonstration of **Edge AI**, where machine learning inference occurs locally on the user's device rather than a remote server.

We trained a Convolutional Neural Network (CNN) on the MNIST dataset using Python and Keras, achieving ~96% accuracy. The model was then converted into a web-optimized format to run efficiently in JavaScript.

**Key Features:**

- **Client-Side Inference:** No backend servers are used. The model runs entirely within the user's browser, ensuring zero latency after the initial load.
- **Privacy:** Since processed data never leaves the device, user input remains private.
- **Interactive Interface:** Features a custom HTML5 canvas implementation to capture and preprocess drawing inputs (resizing, grayscale conversion, and normalization) to match the model's expected input tensor.

## Technical Architecture

- **Model Training:** Python, Keras, TensorFlow
- **Web Conversion:** TensorFlow.js Converter (SavedModel format)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** GitHub Pages

## Running Locally

To run this project on your local machine:

1.  **Clone the repository**

    ```bash
    git clone https://github.com/07subhadip/CNN_Project_MNIST_TFJS.git
    ```

2.  **Serve the files**
    Due to browser CORS policies regarding loading local files, you cannot open `index.html` directly. You must use a local web server.

    - **Python:** Run `python -m http.server` in the project directory.
    - **VS Code:** Use the "Live Server" extension.

3.  **Access**
    Open your browser to `http://localhost:8000`.

---

**Developed by Subhadip Hensh**
