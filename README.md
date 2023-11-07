# Diabetes Predictor

### Problem

The problem for a diabetes predictor is to develop a model that can predict whether an individual is likely to have diabetes based on certain input features such as age, body mass index (BMI), blood pressure, and other relevant medical and lifestyle factors. This predictor aims to assist in early detection of diabetes, allowing for timely intervention and better healthcare management.

he data folder consists of the original dataset, as well as the cleaned dataset.

The code folder consists of:

- Data Cleaning & EDA - part of the notebook

- train.ipynb -Training of model & Hyperparameter Tuning 

- train.py - to train the  final model + saving it using pickle

- predict.py - to load the model and serve it via a web service

- predict-test.py  to test the output of the model, depending on where you want to use it

- Dockerfile for using a Docker container

  

### Steps

First , you need to clone my repository. Go to the project directory .

If you choose to build a docker file locally instead, here are the steps to do so:

1. In your command line, run: `**docker build . -t [your image name]** to create a docker image.

2.  Run **docker run [your image_name]** to run the docker image

   
