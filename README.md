# 💎 Diamond Price Prediction

## 📖 Overview
Diamond Price Prediction is a **Machine Learning Web Application** built using **Flask, Scikit-Learn, Pandas, NumPy, and Matplotlib**. It predicts diamond prices based on various attributes like **carat, cut, color, clarity, etc.**

![image](https://github.com/alokkaushalm51/Diamond-Price-Prediction/blob/main/static/images/Screenshot%20(39).png)

This project follows a **modular approach**, including:
- **Data Ingestion**
- **Data Transformation**
- **Model Training**
- **Model Evaluation**
- **Web UI for Predictions** (Flask)

---

## 🚀 Features
- 📊 **Data Processing & Cleaning**
- 🤖 **Machine Learning Model for Price Prediction**
- 🌐 **Flask Web App**
- 📈 **Model Evaluation & Performance Metrics**
- 📝 **Logging & Exception Handling**
- 📂 **Structured Code with Pipelines**

---

## 🛠️ Installation Guide
Follow these steps to set up the project on your local machine.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/alokkaushalm51/DiamondPricePredictionProject
cd DiamondPricePrediction
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **MacOS/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables (Optional)**
Create a `.env` file for storing sensitive credentials like API keys (if needed).

---

## 📌 Usage Instructions

### **1️⃣ Run the Flask Application**
```bash
python app.py
```
The app will start on **`http://127.0.0.1:8080/`**.

### **2️⃣ Open the Web Application**
Open your browser and go to:  
👉 [http://127.0.0.1:8080/](http://127.0.0.1:8080/)  

Now, you can **input diamond attributes** and get price predictions.

---

## 📂 Project Structure
```bash
DiamondPricePrediction/
│── src/
│   ├── components/         # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   ├── pipelines/          # Training and prediction pipelines
│   ├── logger.py           # Logging setup
│   ├── exception.py        # Custom exception handling
│   ├── utils.py            # Helper functions
│── static/
│   ├── css/                # Custom CSS styles
│   │   ├── style.css       # Main stylesheet
│   ├── images/             # Image assets
│── templates/
│   ├── form.html          # Main prediction interface
│   ├── results.html       # Prediction results page
│── app.py                 # Flask app entry point
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── setup.py               # Package setup
```

---

## 🤖 Model Training & Evaluation
### **1️⃣ Train the Model**
Run the **training pipeline** to train the machine learning model:
```bash
python src/pipelines/training_pipeline.py
```

### **2️⃣ Evaluate the Model**
To evaluate the model performance:
```bash
python src/components/model_evaluation.py
```
This will generate metrics like **R² Score, RMSE, MAE, etc.**.

---

## 🚀 Deployment Guide
### **1️⃣ Deploy on Heroku**
```bash
pip install heroku
heroku login
heroku create diamond-price-predictor
git push heroku main
heroku open
```

---

## 🎯 Contributing
We welcome contributions! Follow these steps:
```bash
git checkout -b feature-branch
git commit -m "Added new feature"
git push origin main
```
Then create a Pull Request on GitHub.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📧 Contact
For any issues or suggestions, feel free to reach out:  
📧 Email: `alokkaushal777@gmail.com`  
🔗 GitHub: [https://github.com/alokkaushalm51/Diamond-Price-Prediction]

---

## ⭐ Acknowledgements
Special thanks to **Scikit-Learn, Pandas, NumPy, Flask, and Matplotlib** for providing powerful tools for machine learning & data science.

---

📌 **Next Steps:**
```bash
git add README.md
git commit -m "Added README documentation"
git push origin main
```
```

