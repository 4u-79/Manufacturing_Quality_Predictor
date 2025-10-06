# Manufacturing Quality Prediction System

Web application that predicts manufacturing quality ratings based on sensor parameters using machine learning.

**Live Demo:** manufacturequalitypredictor-fhcgbta0hkgrgkeu.southeastasia-01.azurewebsites.net

## Features
- Real-time quality prediction from manufacturing parameters
- Color-coded quality status (Green/Orange/Red)
- Interactive web interface

## Technologies
- Python, Scikit-learn, Pandas
- Streamlit
- Microsoft Azure App Service
- GitHub CI/CD

## Model Details
- Algorithm: Random Forest Regressor
- Metrics: MSE, R² score
- Dataset: Kaggle manufacturing data

## Limitations
The dataset leans towards high quality ratings. The model performs well on predicting those but would benefit from more low-quality samples for real-world use cases.

## Installation
1. Clone this repository:
   ```bash
     git clone https://github.com/4u-79/Manufacturing_Quality_Predictor.git
     cd Manufacturing_Quality_Predictor
  
2. Install dependencies:
  pip install -r requirements.txt

3. Train the model (optional):
  python train_model.py

4. Run the Streamlit app:
  streamlit run app.py

## Author
Project by Marcus Andrei Guinto
