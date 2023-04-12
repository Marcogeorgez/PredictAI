import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.callbacks import ModelCheckpoint
from PredictAI import db
from PredictAI.DatabaseClasses import Company
from datetime import timedelta, date, datetime


# This code assumes that you have a StockData model in your Flask app with a timestamp and stock_price column. You may need to modify the code to match your specific use case.


def PredictFuture(PredictTicker_Name):

    query_result = db.session.query(Company).filter(
        Company.Symbol == PredictTicker_Name, Company.Date >= datetime(2020, 3, 3)).all()
    df = pd.DataFrame([(q.Date, q.Close_)
                       for q in query_result], columns=['Date', 'Close_'])
    # Extract the 'Close' column as the target variable
    data = df.filter(['Close_']).values

    # Scale the data using MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # Define the number of time steps for the LSTM model
    time_steps = 120

    # Create a new dataset with time steps
    X = []
    y = []
    for i in range(time_steps, len(scaled_data)):
        X.append(scaled_data[i - time_steps:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
# Reshape the data for LSTM
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Split the data into training and testing sets
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(units=100, return_sequences=True,
                   input_shape=(time_steps, 1)))
    model.add(LSTM(units=100))

    model.add(Dense(units=1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    checkpoint = ModelCheckpoint('bestweights.h5', save_best_only=True,
                                 save_weights_only=True, monitor='val_loss', mode='min', verbose=1)
    history = model.fit(X_train, y_train, epochs=3, batch_size=100,
                        validation_data=(X_test, y_test), callbacks=[checkpoint])

    # Load the weights of the best epoch
    model.load_weights('bestweights.h5')

    # Make predictions on the testing data
    predictions = model.predict(X_test)

    # Inverse scale the predictions
    predictions = scaler.inverse_transform(predictions)

    # Inverse scale the test data
    y_test = scaler.inverse_transform([y_test])

    # Calculate the mean squared error
    mse = np.mean((y_test[0] - predictions[:, 0])**2)
    print('Mean Squared Error: {:.2f}'.format(mse))

    # Predict the next 30 days of stock prices
    last30days = scaled_data[-time_steps:]
    last30days = np.reshape(last30days, (1, last30days.shape[0], 1))
    forecast = []
    for i in range(90):
        prediction = model.predict(last30days)
        forecast.append(prediction)
        last30days = np.concatenate(
            (last30days[:, 1:, :], prediction.reshape(1, 1, 1)), axis=1)

        # Inverse scale the predicted prices

    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))

    # Print the predicted prices for the next 30 days
    # print(f'Predicted prices for the next {len(forecast)} days:')
    # for i in range(len(forecast)):
    #     data[(date.today() + timedelta(days=i+1)
    #           ).strftime('%Y-%m-%d')] = forecast[i][0]
    # print(f'Predicted prices for the next {len(forecast)} days:')
    for i in range(len(forecast)):
        print('Day {}: ${:.2f}'.format(
            (date.today() + timedelta(days=i+1)).strftime('%Y-%m-%d'), forecast[i, 0]))
