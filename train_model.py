import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

data = pd.read_csv("data/manufacturing.csv")
X = data.drop('Quality Rating', axis=1)
y = data['Quality Rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
Model_R = RandomForestRegressor(n_estimators=100, random_state=42)
Model_R.fit(X_train, y_train)

y_pred = Model_R.predict(X_test)
mean_sq = mean_squared_error(y_test, y_pred)
r2_score = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mean_sq:.2f}")
print(f"R² Score: {r2_score:.2f}")
print(data.columns)

joblib.dump(Model_R, 'models/manufacturing_model.pkl')
print(data['Quality Rating'].describe())
print(data['Quality Rating'].unique()[:20]) 
