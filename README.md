# Gold Price Prediction Application

## Table of Contents

- [Gold Price Prediction Application](#gold-price-prediction-application)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [How to Run the Code](#how-to-run-the-code)
  - [Project Components](#project-components)
    - [Data Handling](#data-handling)
    - [Model Prediction](#model-prediction)
    - [User Interface](#user-interface)
    - [Error Handling](#error-handling)
  - [Steps Performed in the Jupyter Notebook](#steps-performed-in-the-jupyter-notebook)
    - [Step 1: Data Loading and Inspection](#step-1-data-loading-and-inspection)
    - [Step 2: Data Preprocessing](#step-2-data-preprocessing)
    - [Step 3: Feature and Label Extraction](#step-3-feature-and-label-extraction)
    - [Step 4: Model Training and Evaluation](#step-4-model-training-and-evaluation)
    - [Step 5: Visualization](#step-5-visualization)
    - [Step 6: Application Deployment](#step-6-application-deployment)
    - [Conclusion](#conclusion)

## Project Overview

The Gold Price Prediction application is a web-based tool designed to predict the closing price of gold based on historical price data. By utilizing a pre-trained Support Vector Regression (SVR) model, the application provides users with an intuitive interface to input relevant price data and receive accurate predictions. The application is built using Streamlit, which allows for an interactive and user-friendly experience.

## How to Run the Code

To run the Gold Price Prediction application, follow these steps:

1.  **Download the Project Files**:

    - Download the **main.py** file and the **Gold_Price.csv** dataset.
    - Ensure the **svm_model.pkl** file (the pre-trained model) is also available in the same directory.

2.  **Install Required Libraries**:  
    Make sure you have Python installed on your system.  
    Instead of installing individual libraries manually, you can install all required packages listed in the `requirements.txt` file by running this command in your terminal or command prompt:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit Application**: Open a terminal or command prompt, navigate to the directory where the files are located, and run the following command:

```bash
  streamlit run main.py
```

1.  **Access the Application**: After running the command, a new tab will open in your default web browser displaying the Gold Price Prediction application. You can now input the Open, High, and Low prices to get predictions.

## Project Components

### Data Handling

The application includes a **DataHandler** class that manages the loading and validation of historical data from a CSV file. This class ensures that the necessary data is present and correctly formatted for analysis.

### Model Prediction

The **Predictor** class is responsible for loading the pre-trained SVR model and making predictions based on user input. It encapsulates the model loading and prediction logic, allowing users to obtain predictions easily.

### User Interface

The application is built using Streamlit, providing an interactive web interface that includes:

- A title indicating the purpose of the application.
- A section displaying the last four open, high, and low prices from the dataset.
- Input fields for users to enter the Open, High, and Low prices.
- A button to trigger the prediction process.
- An output area that displays the predicted closing price based on the user inputs.

### Error Handling

Robust error handling is integrated throughout the application to ensure a smooth user experience. The application checks for:

- The existence of the CSV and model files.
- The presence of required columns in the data.
- Validity of user inputs, ensuring that all price values are positive.

## Steps Performed in the Jupyter Notebook

### Step 1: Data Loading and Inspection

- The notebook begins by loading the historical gold price data from a CSV file using the **DataHandler** class.
- It retrieves and displays the first few rows of the dataset to give users an overview of the data structure.

### Step 2: Data Preprocessing

- The notebook includes a data preprocessing step where the data is cleaned and transformed for analysis.
- This involves removing any unnecessary characters, handling missing values, and converting data types to ensure compatibility with the model.

### Step 3: Feature and Label Extraction

- The features (Open, High, Low prices) and the target variable (closing price) are extracted from the cleaned dataset.
- This prepares the data for training and testing the predictive model.

### Step 4: Model Training and Evaluation

- The notebook demonstrates how to split the dataset into training and testing sets.
- It trains the SVR model using the training data and evaluates its performance using metrics such as Mean Squared Error (MSE).

### Step 5: Visualization

- Various visualizations are generated to analyze the historical price trends and the model's predictions.
- This includes plots for price distributions, moving averages, and other relevant financial metrics.

### Step 6: Application Deployment

- Finally, the notebook outlines how to deploy the application using Streamlit, allowing users to interact with the model through a web interface.

### Conclusion

---

The Gold Price Prediction application effectively integrates data management, machine learning, and user interaction into a cohesive tool. It serves as a practical solution for users interested in predicting gold prices based on historical trends. The application leverages the capabilities of Streamlit for a user-friendly experience and employs robust error handling to ensure reliability.
