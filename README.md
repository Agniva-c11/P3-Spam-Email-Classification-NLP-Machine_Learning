# P3-Spam-Email-Classification-NLP-Machine_Learning
This project is a Spam Email Classifier built using Python and machine learning techniques. The goal is to classify email messages as either spam or not spam (ham).

Features:-
Dataset: Preprocessed email dataset with labels (ham and spam).
Text Vectorization: Used CountVectorizer to convert text into numerical features.
Model: Implemented a Naive Bayes classifier for fast and efficient text classification.
Evaluation: Achieved high accuracy on test data.
Real-world Testing: Predicts whether a new message is spam or not.
How It Works
Data Preprocessing:
Loaded the dataset (spam.csv) and mapped labels (ham → 0, spam → 1).
Converted email text into numerical feature vectors using CountVectorizer.
Model Training:
Used the MultinomialNB model from sklearn for training on the processed data.
Model Evaluation:
Split the data into training and testing sets.
Computed the accuracy on the test set.
Prediction:
Input a custom email message and predict whether it's spam.
