from threading import Thread
from main import app

# Function to keep the server running
def run():
    app.run(host='0.0.0.0', port=8080)

# Function to start a new thread to keep the server alive
def keep_alive():
    # Create a new thread targeting the run() function
    t = Thread(target=run)
    # Start the thread
    t.start()
