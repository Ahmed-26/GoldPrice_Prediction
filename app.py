import streamlit as st  # Import Streamlit for building the web app UI
import pickle  # Import pickle for loading the pre-trained model
import pandas as pd  # Import pandas for data manipulation with DataFrames
from pathlib import Path  # Import Path for platform-independent file handling

class DataHandler:
    """Handles loading and validation of historical data from a CSV file."""
    
    def __init__(self, file_path, required_columns):
        """
        Initialize with file path and required columns.

        Parameters:
        - file_path (str): Path to the CSV file containing historical data.
        - required_columns (set): Set of column names required in the CSV.

        Raises:
        - FileNotFoundError: If the specified CSV file does not exist.
        - ValueError: If the CSV file lacks any required columns.
        """
        self.file_path = Path(file_path)  # Convert file path to Path object for robust handling
        self.required_columns = required_columns  # Store the set of required columns
        self.df = self._load_data()  # Load and validate the CSV data

    def _load_data(self):
        """Load and validate CSV data into a pandas DataFrame."""
        # Check if the CSV file exists
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(self.file_path)
        # Validate that all required columns are present in the DataFrame
        if not self.required_columns.issubset(df.columns):
            raise ValueError(f"CSV file must contain these columns: {self.required_columns}")
        return df  # Return the validated DataFrame

    def get_head(self, n=4):
        """
        Return the first n rows of specified columns.

        Parameters:
        - n (int, optional): Number of rows to return (default is 4).

        Returns:
        - pd.DataFrame: First n rows of the DataFrame with required columns.
        """
        return self.df[list(self.required_columns)].head(n)  # Select required columns and get first n rows

class Predictor:
    """Handles loading a pre-trained model and making predictions."""
    
    def __init__(self, model_path):
        """
        Initialize with model file path.

        Parameters:
        - model_path (str): Path to the pickled model file (e.g., .pkl).

        Raises:
        - FileNotFoundError: If the model file does not exist.
        - pickle.PickleError: If the model cannot be loaded due to deserialization issues.
        """
        self.model_path = Path(model_path)  # Convert model path to Path object
        self.model = self._load_model()  # Load the pre-trained model

    def _load_model(self):
        """Load the pre-trained model from a pickle file."""
        # Check if the model file exists
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        
        # Attempt to load the model from the pickle file
        try:
            with open(self.model_path, 'rb') as file:  # Open file in binary read mode
                return pickle.load(file)  # Deserialize and return the model
        except pickle.PickleError as e:
            raise pickle.PickleError(f"Failed to load model: {str(e)}")  # Raise error if loading fails

    def predict(self, input_data):
        """
        Make a prediction using the loaded model.

        Parameters:
        - input_data (pd.DataFrame): Input data with features for prediction.

        Returns:
        - float: Predicted value (e.g., closing price).
        """
        return self.model.predict(input_data)[0]  # Return the first predicted value from the model

class GoldPriceApp:
    """Manages the Streamlit app for gold price prediction, integrating data and model."""
    
    def __init__(self, data_path='Gold_Price.csv', model_path='svm_model.pkl', 
                 required_columns={'Open', 'High', 'Low'}):
        """
        Initialize the app with data and model paths.

        Parameters:
        - data_path (str, optional): Path to the CSV file (default: 'Gold_Price.csv').
        - model_path (str, optional): Path to the model file (default: 'svm_model.pkl').
        - required_columns (set, optional): Required columns in the data (default: {'Open', 'High', 'Low'}).

        Raises:
        - Displays error in Streamlit UI and stops if initialization fails.
        """
        try:
            # Initialize DataHandler with the CSV path and required columns
            self.data_handler = DataHandler(data_path, required_columns)
            # Initialize Predictor with the model path
            self.predictor = Predictor(model_path)
            # Store required columns for reference
            self.required_columns = required_columns
        except (FileNotFoundError, ValueError, pickle.PickleError) as e:
            st.error(str(e))  # Display any initialization errors in the Streamlit UI
            st.stop()  # Stop execution if initialization fails

    def run(self):
        """Run the Streamlit app, creating the UI and handling predictions."""
        # Set the main title of the app
        st.title('Gold Price Prediction')
        
        # Display historical data section
        st.subheader("Last 4 Open, High, Low Prices")
        # Show the first 4 rows of historical data in a table
        st.table(self.data_handler.get_head(4))

        # Input section for user to enter price data
        st.subheader("Enter Price Data")
        # Create numeric input fields for Open, High, and Low prices
        open_price = st.number_input('Open Price', min_value=0.0, step=0.01)  # Note: Label might be a typo; should be 'Open Price'
        high_price = st.number_input('High Price', min_value=0.0, step=0.01)  # Note: Label might be a typo; should be 'High Price'
        low_price = st.number_input('Low Price', min_value=0.0, step=0.01)

        # Handle prediction when the user clicks the 'Predict' button
        if st.button('Predict'):
            # Validate that all input prices are positive
            if open_price <= 0 or high_price <= 0 or low_price <= 0:
                st.error("All prices must be positive values.")  # Display error if inputs are invalid
            else:
                # Create a DataFrame with user inputs, matching the required column order
                input_df = pd.DataFrame(
                    [[open_price, high_price, low_price]], 
                    columns=['Open', 'High', 'Low'] 
                )
                try:
                    # Make a prediction using the Predictor class
                    prediction = self.predictor.predict(input_df)
                    # Display the predicted closing price, formatted to 2 decimal places
                    st.write(f'The predicted closing price is: {prediction:.2f}')
                except Exception as e:
                    # Display any prediction errors in the Streamlit UI
                    st.error(f"Prediction failed: {str(e)}")
