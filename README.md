# 🚗 Car Price Prediction

A machine learning project to predict the price of used cars based on features like **brand, model, year, fuel type, and kilometers driven**. The model is trained using a cleaned dataset from Quikr Cars and deployed with **Streamlit** for an interactive user interface.

---

## 📌 Project Overview
- **Dataset**: `quikr_car.csv`  
- **Goal**: Predict car resale prices  
- **Libraries used**: `pandas`, `numpy`, `scikit-learn`, `streamlit`, `pickle`  
- **Model used**: Linear Regression with OneHotEncoding (Pipeline)  

---

## 🧹 Data Cleaning
The raw dataset contained inconsistencies, which were fixed:
- Removed non-numeric values in `year` and converted to `int`.
- Removed entries with `"Ask For Price"` and converted `Price` to `int`.
- Cleaned `kms_driven` by removing text like `"kms"`, commas, and converting to `int`.
- Dropped rows with missing `fuel_type`.
- Simplified `name` column to first 3 words (brand + model).
- Removed extreme outliers (`Price > 6,000,000`).

Final cleaned dataset saved as **`cleaned_car.csv`**.

---

## 🤖 Model Training
- **Features**: `name`, `company`, `year`, `kms_driven`, `fuel_type`  
- **Target**: `Price`  
- **Pipeline**:
  1. OneHotEncoder for categorical variables (`name`, `company`, `fuel_type`).
  2. Linear Regression model.  

- Best R² score after tuning random state: **~0.82**  

The trained pipeline is saved as **`LinearRegressionModel.pkl`** using `pickle`.

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### 2️⃣ Install dependencies
Make sure you have Python 3.8+ installed. Then run:
```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
numpy
scikit-learn
streamlit
```

### 3️⃣ Run the Streamlit app
```bash
streamlit run Stream_lit_interface.py
```

### 4️⃣ Predict car prices
The app will open in your browser where you can input:
- Car Name (e.g., *Maruti Suzuki Swift*)  
- Company (e.g., *Maruti*)  
- Year (e.g., *2019*)  
- Kilometers Driven (e.g., *50000*)  
- Fuel Type (e.g., *Petrol*)  

Click **Predict** to see the estimated price.

---

## 📊 Example Prediction
```python
pipe.predict(pd.DataFrame([[
    'Maruti Suzuki Swift', 'Maruti', 2019, 100, 'Petrol'
]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
```

Output:
```
array([XXXXXX])  # Predicted price
```

---

## 📂 Project Structure
```
car-price-prediction/
│── quikr_car.csv                # Raw dataset
│── cleaned_car.csv              # Cleaned dataset
│── LinearRegressionModel.pkl    # Trained ML model
│── Stream_lit_interface.py      # Streamlit UI
│── requirements.txt             # Dependencies
│── README.md                    # Project documentation
```

---

## 🔮 Future Improvements
- Try other models (Random Forest, XGBoost).
- Add more features (transmission, owner type, city).
- Deploy app on **Streamlit Cloud / Heroku**.
- Integrate with a real-time dataset.

---

🙌 Built with Python, Pandas, Scikit-learn & Streamlit  
