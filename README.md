 🌸 Flower Classifier

A deep learning web app that classifies flower images into one of five categories: **Daisy**, **Dandelion**, **Rose**, **Sunflower**, and **Tulip**.  
Built using TensorFlow + Streamlit and deployed for public use.

---

🚀 Live Demo

👉 [Click to Use the App](https://ai-flower-classifier.streamlit.app)

---

 🧠 Model Details

- **Architecture**: MobileNetV2 (pre-trained on ImageNet)
- **Fine-Tuned On**: TensorFlow Flowers Dataset (5 classes)
- **Input Size**: 224 x 224 pixels
- **Framework**: TensorFlow/Keras
- **Prediction Output**: Top-1 class with confidence percentage

---

📸 App Features

- Upload a `.jpg` or `.png` flower image
- Get a real-time classification result
- Displays model's predicted flower type and confidence
- Simple and clean UI built with Streamlit
- Fully responsive and easy to use

---

 📂 Project Structure

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app |
| `flower_classifier.h5` | Pre-trained Keras model |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |


---

 📦 Installation (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/jawadhameedbaloch/flower-image-classifier.git
   cd flower-classifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:
   ```bash
   streamlit run app.py
   ```

---

 ✅ Dependencies

- Python 3.9+
- TensorFlow
- NumPy
- Pillow
- Streamlit

All are listed in `requirements.txt`.

---

## 👨‍💻 Developed By

**Jawad Hameed Baloch**  
Generative AI Engineer | BSCS | AI Enthusiast  

---

 📚 Dataset Source

- [TensorFlow Flowers Dataset](https://www.tensorflow.org/datasets/catalog/tf_flowers)

---

 🌐 Deployed Using

- [Streamlit Cloud](https://streamlit.io/cloud)

---

🛡️ License

This project is for educational/demo purposes only.
