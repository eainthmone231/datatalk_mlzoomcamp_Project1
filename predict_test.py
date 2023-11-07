import requests
url = "http://localhost:8080/predict"
data = { "Pregnancies" : 6,
 "Glucose" : 148,
 "BloodPressure" : 72,
 "SkinThickness" :35,
 "Insulin" :0,
 "BMI":33.6,
 "DiabetesPedigreeFunction" :0.627,
 "Age":29}

response = requests.post(url, json=data)
print(response)