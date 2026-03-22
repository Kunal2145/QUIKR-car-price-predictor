# 🚗 Quikr Car Price Predictor

A Machine Learning-powered web application that predicts the resale price of used cars based on user inputs such as car model, company, year, kilometers driven, and fuel type.

---

## 📌 Project Overview

The **Quikr Car Price Predictor** is an end-to-end machine learning project that leverages regression techniques to estimate the market value of used cars. The application is built using **Streamlit** for an interactive user interface and deployed for real-time predictions.

This project demonstrates the complete ML lifecycle:

* Data preprocessing
* Feature engineering
* Model building
* Deployment using a web framework

---

## 🎯 Problem Statement

Estimating the resale price of used cars can be challenging due to multiple influencing factors. This project aims to build a predictive model that helps users:

* Get a quick estimate of car value
* Make informed buying/selling decisions
* Reduce dependency on manual price evaluation

---

## 🚀 Features

* 🔍 Predict car prices instantly
* 📊 User-friendly web interface
* ⚡ Real-time predictions using trained ML model
* 🧠 Automated handling of categorical features using pipeline
* 📱 Responsive and clean UI with Streamlit

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Model:** Linear Regression (with Pipeline)
* **Web Framework:** Streamlit
* **Version Control:** Git & GitHub

---

## 📊 Input Parameters

The model takes the following inputs:

* 🚘 Car Model
* 🏢 Company
* 📅 Manufacturing Year
* 🛣️ Kilometers Driven
* ⛽ Fuel Type

---

## 🧠 Machine Learning Approach

* Data Cleaning & Preprocessing
* Handling Missing Values
* One-Hot Encoding for categorical variables
* Feature selection
* Model training using Linear Regression
* Pipeline used to ensure consistency during deployment

---

## 📂 Project Structure

```
car-price-predictor/
│
├── app.py                      # Streamlit web app
├── LinearRegressionModel.pkl   # Trained ML model
├── car_price_model.ipynb       # Jupyter Notebook (model building)
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Kunal2145/car-price-predictor.git

# Navigate to project folder
cd car-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🌐 Live Demo

👉 (Add your deployed Streamlit link here)

---

## 📸 Screenshot

<img width="1174" height="629" alt="Screenshot 2026-03-22 at 9 13 27 PM" src="https://github.com/user-attachments/assets/3b1ad2ac-77aa-48f9-b675-793d9ccc1d57" />
<img width="1119" height="623" alt="Screenshot 2026-03-22 at 9 13 41 PM" src="https://github.com/user-attachments/assets/76c37c52-c006-4a24-834c-2a687a4db4f9" />

---

## 💡 Future Improvements

* Add more advanced models (Random Forest, XGBoost)
* Improve UI/UX with better design
* Add location-based price prediction
* Deploy using Docker for scalability

---

## 🙌 Acknowledgements

* Dataset inspired from real-world used car listings
* Built as part of Machine Learning portfolio project

---

⭐ If you found this project useful, consider giving it a star on GitHub!
