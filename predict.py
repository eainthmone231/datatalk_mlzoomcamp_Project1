
from flask import Flask,request
import json
import pickle
import numpy as np

app = Flask(__name__)

model_name = "finalized_model.sav"

@app.get("/")
def homePage():
    return "hello this is homepage"

@app.post("/predict")
def predict():
    request_data = request.json
    feature_data =[]
    for feature in dict(request_data).values():
        feature_data.append(feature)
    response= {}
    # load the model from disk
    loaded_model = pickle.load(open(model_name, 'rb'))
    result = loaded_model.predict(np.array(feature_data).reshape(1, -1))
    response["Outcome"]=result
    dummped_json = json.dumps(response,ensure_ascii = False)
    return dummped_json

# To locally run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3000)