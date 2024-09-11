# Sentiment Analysis Using LSTM Recurrent Neural Networks (RNN)

This project implements a Sentiment Analysis model using LSTM RNN (Recurrent Neural Networks) to classify text into positive, negative, or neutral sentiments.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Sentiment analysis is a common Natural Language Processing (NLP) task where a machine learning model is used to identify and categorize the sentiment expressed in a given text. In this project, we use a Recurrent Neural Network (RNN) to perform sentiment analysis on a dataset of text reviews.

The goal is to build a model that can predict the sentiment (positive, negative, neutral) of a given input text.

## Technologies Used

- **Python 3.10**
- **TensorFlow/Keras** for building the LSTM RNN model
- **NumPy** for data manipulation
- **Pandas** for data preprocessing
- **NLTK** for text preprocessing
- **Scikit-learn** for evaluation metrics
- **Matplotlib/Seaborn** for visualization

## Dataset

We use a publicly available dataset of text reviews (such as the [twitter dataset](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)) that contains labeled reviews classified as positive, negative, or neutral.

Alternatively, you can use any dataset of your choice by following the format:

- **Text**: The actual review text.
- **Label**: The sentiment label (0 for negative, 1 for neutral, 2 for positive).



