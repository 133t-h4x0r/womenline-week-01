# -*- coding: utf-8 -*-
"""Women Line-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uNv2LkitoAob4OitDMbRFPfrGhkWrEKW
"""

!pip install pandas scikit-learn

from google.colab import files
uploaded = files.upload()

import pandas as pd

data = pd.read_csv("cleaned_multilingual_prompts.csv")
print(data.head())

import pandas as pd

data = pd.read_csv('cleaned_multilingual_prompts.csv')
print(data.head())

print(data.columns)

print(data.head())

X = data['Prompt']
y = data['Intent']

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

user_input = ["How to handle teenage anxiety?"]
input_vector = vectorizer.transform(user_input)
prediction = model.predict(input_vector)
print("Predicted Intent:", prediction[0])

user_input = input("Ask your question: ")

# Check if question is relevant
if any(word in user_input.lower() for word in ["stress", "diet", "anxiety", "self-care"]):
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)
    print("Predicted Intent:", prediction[0])
else:
    print("Can you please provide more specific details?")

# Feedback
feedback = input("Was this response helpful? (yes/no): ")
print("Thanks for your feedback!")