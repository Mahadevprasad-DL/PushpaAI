# PushpaAI
# 🌸 Flower Identification using CNN

A web-based Flower Recognition project using a **Convolutional Neural Network (CNN)**. Users can upload an image of a flower, and the model predicts the flower type and provides detailed information about it.

---

## Project Overview

This project aims to build an AI-powered flower identification system using CNNs. The main objective is to accurately classify flower images and display relevant details such as colors, types, scientific names, and best-growing regions.

---

## Project Structure
├── app.py # Flask application
├── train.py # Script to train CNN model
├── models/ # Saved CNN model
├── data/ # Folder containing flower dataset (link provided)
├── static/
│ ├── css/ # CSS files
│ ├── images/ # Sample images for website
│ └── js/ # JavaScript files
├── templates/ # HTML templates for web pages
│ ├── index.html # Upload & prediction page
│ ├── home.html # Home page
│ ├── model.html # Model architecture & details
│ ├── dataset.html # Dataset overview
│ ├── about.html # About flowers page
│ ├── results.html # Accuracy and results
│ └── contact.html # Contact form
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## Features

### Home
- Introduction to the project
- Purpose and overview

### Upload / Identify Flower
- Users can upload an image
- CNN model predicts the flower
- Displays flower information including:
  - Name
  - Scientific name
  - Colors
  - Best-growing regions
  - Uses

### Dataset
- Uses the [Flowers Recognition Dataset](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition)
- Contains images of various flowers
- Sample images are displayed in the `dataset.html` page

### Model
- CNN-based image classification model
- Architecture includes:
  - Multiple Convolutional layers
  - ReLU activations
  - MaxPooling layers
  - Dropout for regularization
  - Dense layers for classification
- Achieved high accuracy on training and validation data

### About Flowers 🌸
- Provides detailed information for each flower category
- Includes scientific names, descriptions, and common uses

### Results / Accuracy
- Shows training vs validation accuracy graphs
- Confusion matrix for model evaluation

### Contact / About Us
- Provides project details
- Contact form for reaching out
- GitHub/LinkedIn links

---

## Dataset
Dataset Link

Since the dataset is too large to include, you can download it from Kaggle:
https://www.kaggle.com/datasets/alxmamaev/flowers-recognition





