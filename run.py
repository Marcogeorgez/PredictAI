from PredictAI import app
# The if statement checks if the current module is the main module being executed.
# This ensures that the app.run() command is only executed if this module is run directly, rather than imported as a module in another script.
if __name__ == '__main__':
    # The app.run() command is used to run the Flask application.
    # The debug parameter is set to True to enable debug mode, which provides detailed error messages.
    app.run(debug=True)
