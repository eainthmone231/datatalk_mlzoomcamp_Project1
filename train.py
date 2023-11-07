import pandas as pd
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import pickle

data_dir = "disease_dataset/"
data = pd.read_csv(data_dir+"preprocessed_data.csv")

X = data.iloc[:,:-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size = 0.2, random_state = 24)
#X_val ,X_test, y_val,y_test = train_test_split(X_test,y_test, test_size=0.5,random_state = 24)

# As features are measured using different unit of measurements, we can normalize or scale them.


st =MinMaxScaler()
X_train = st.fit_transform(X_train)
X_test = st.fit_transform(X_test)
print(f"Train: {X_train.shape}, {y_train.shape}")
#print(f"Val: {X_val.shape}, {y_val.shape}")
print(f"Test: {X_test.shape}, {y_test.shape}")

lgst = LogisticRegression(C=0.5, max_iter=1000)
lgst = lgst.fit(X_train,y_train)

filename = 'finalized_model.sav'
pickle.dump(lgst, open(filename, 'wb'))