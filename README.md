# Serverless MNIST Digit Recognizer

![Visitor Count](https://komarev.com/ghpvc/?username=07subhadip-CNN-Project-MNIST-TFJS&label=Views&color=0e75b6&style=flat)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/07subhadip/CNN_Project_MNIST_TFJS/blob/main/LICENSE)
![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-Powered-orange)

This project demonstrates **Edge AI** by deploying trained Deep Learning models directly to the web using TensorFlow.js. It features a unique **Dual-Model Architecture**, allowing users to switch between a Convolutional Neural Network (CNN) and a classic Multi-Layer Perceptron (MLP) in real-time to compare performance outcomes.

All inference happens client-side, ensuring **zero latency** and **complete privacy** as user data never leaves the browser.

### [🔴 Click Here to Try the Live Demo](https://07subhadip.github.io/CNN_Project_MNIST_TFJS/)

---

## ⚡ Key Features

- **Dual-Model Support:** Instantly toggle between CNN and MLP models via the UI.
- **Edge AI:** Inference runs strictly on the client CPU/GPU using WebGL acceleration.
- **Privacy-First:** No backend API calls; drawings are processed locally.
- **Interactive Canvas:** Custom HTML5 drawing board with preprocessing logic (grayscale, resizing, normalization) that matches the training pipeline.

---

## ⚔️ Model Comparison

This application allows you to compare two different neural network architectures side-by-side. Below are the actual performance metrics captured during training on the MNIST dataset:

| Metric                | CNN Model (SOTA) | MLP Model (Simple) |
| :-------------------- | :--------------- | :----------------- |
| **Training Accuracy** | **99.59%**       | 97.47%             |
| **Testing Accuracy**  | **98.88%**       | 96.64%             |
| **Training Loss**     | 0.0113           | 0.1765             |
| **Testing Loss**      | 0.0384           | 0.1944             |

The CNN model achieves ~98.9% accuracy compared to the MLP's ~96.6%, showing better generalization on unseen data.

---

## 🛠️ Tech Stack

- **Model Training:** Python, Keras, TensorFlow
- **Conversion:** TensorFlow.js Converter (SavedModel format)
- **Frontend:** HTML5 Canvas, CSS3, Vanilla JavaScript
- **Inference Engine:** TensorFlow.js (`tfjs-graph-model` & `tfjs-layers-model`)

---

## 🏃‍♂️ How to Run Locally

To test or modify this project on your local machine:

1.  **Clone the repository**

    ```bash
    git clone https://github.com/07subhadip/CNN_Project_MNIST_TFJS.git
    cd CNN_Project_MNIST_TFJS
    ```

2.  **Start a Local Server**
    Due to browser CORS policies, you cannot open `index.html` directly.

    - **Python:**
      ```bash
      python -m http.server
      ```
    - **Node.js:**
      ```bash
      npx http-server
      ```

3.  **Access the App**
    Open your browser and navigate to `http://localhost:8000`.

---

<div align="center">
  <strong>Developed by Subhadip Hensh</strong><br>
  &copy; 2026 All Rights Reserved.
</div>
