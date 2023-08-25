# Import required libraries
from datetime import datetime
import numpy as np
import pandas as pd
from keras.layers import LSTM, Dense
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from PredictAI import db
from PredictAI.DatabaseClasses import Company

def PredictFuture(PredictTicker_Name):

    # Connect to database and select required data
    query_result = db.session.query(Company).filter(
        Company.Symbol == PredictTicker_Name, Company.Date <= datetime(2023, 2, 16)).all()

    # Create a pandas dataframe from the database result
    First_Query = pd.DataFrame([(q.Date, q.Close_)
                                for q in query_result], columns=['Date', 'Close_'])
    First_Query = First_Query.sort_values(by='Date', ascending=True)
    # Put the First_Query Data into Company_Train.csv so it be easy to reshape it and read it without datatype flaot64
    First_Query.to_csv('Company_Train.csv', index=False)
    Train_Data = pd.read_csv('Company_Train.csv')

    # Connect to database and select required data
    query_result2 = db.session.query(Company).filter(
        Company.Symbol == PredictTicker_Name, Company.Date >= datetime(
            2023, 2, 17),
        Company.Date <= datetime(2023, 6, 16)).all()

    # Create a pandas dataframe from the database result
    Second_Query = pd.DataFrame([(q.Date, q.Close_)
                                 for q in query_result2], columns=['Date', 'Close_'])
    Second_Query = Second_Query.sort_values(by='Date', ascending=False)

    print('----------Number of Days to validate and predict: ', len(Second_Query))

    # Put the Second_Query Data into Company_Validate.csv so it be easy to reshape it and read it without datatype flaot64
    Second_Query.to_csv('Company_Validate.csv', index=False)
    Validate_Data = pd.read_csv('Company_Validate.csv')

    # Get the closing prices from the dataframe
    data = First_Query.filter(['Close_']).values

    # Scale the data using MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # Define the number of time steps to use for training of LSTM model
    time_steps = 60

    # Create training data by adding the previous 60 days' closing prices as input
    X = []
    Y = []
    for i in range(time_steps, len(scaled_data)):
        X.append(scaled_data[i - time_steps:i, 0])
        Y.append(scaled_data[i, 0])
    X, Y = np.array(X), np.array(Y)

    # Reshape the input data to be compatible with LSTM model
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Define and Build the LSTM model
    model = Sequential()
    model = Sequential()
    model.add(LSTM(units=100, return_sequences=True,
                   input_shape=(X.shape[1], 1)))
    model.add(LSTM(units=100))
    model.add(Dense(units=1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(X, Y, epochs=7, batch_size=4)

    # concate train data and test data to dataset total then reshape them
    dataset_total = pd.concat(
        (Train_Data['Close_'], Validate_Data['Close_']), axis=0)

    # Get the input data for future predictions
    inputs_future = dataset_total[len(dataset_total) - len(Validate_Data) - 60:].values

    # Reshape input data to 2D array
    inputs_future = inputs_future.reshape(-1, 1)

    # Scale the input data
    inputs_future = scaler.transform(inputs_future)

    # Create an empty list to store predicted values
    Predicted_Values_ValidateAndTrain = []

    # Loop through the input data and append values to the list
    for i in range(time_steps, time_steps+len(Second_Query)-1):
        Predicted_Values_ValidateAndTrain.append(inputs_future[i-time_steps:i, 0])

    # Convert the list to a numpy array
    Predicted_Values_ValidateAndTrain = np.array(Predicted_Values_ValidateAndTrain)

    # Reshape the numpy array to 3D
    Predicted_Values_ValidateAndTrain = np.reshape(Predicted_Values_ValidateAndTrain, (
        Predicted_Values_ValidateAndTrain.shape[0], Predicted_Values_ValidateAndTrain.shape[1], 1))

    # Use the model to predict the stock prices
    predicted_stock_price = model.predict(Predicted_Values_ValidateAndTrain)

    # Inverse transform the predicted stock prices
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price)

    # Create an empty list to store the predicted days
    DaysOutput = []

    # Flatten and convert the predicted stock prices to float type
    PredicitonResult = predicted_stock_price.flatten().astype(float)

    # Create an empty list to store the rounded predicted prices
    PredictionResultRounded = []

    # Loop through the predicted prices and round each value to two decimal places
    for i in PredicitonResult:
        PredictionResultRounded.append(round(i, 3))

    # Initialize a variable to keep track of the days
    x = 0
    # Loop through the predicted days and add the values to the DaysOutput list
    for i in range(time_steps, time_steps+len(Second_Query)-1):
        DaysOutput.append(x)
        x = x + 1

    print(PredictionResultRounded)

    # Return the predicted prices and the corresponding days
    return DaysOutput, PredictionResultRounded