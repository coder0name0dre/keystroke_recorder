from datetime import datetime

# Intructions To User
print("Keystroke Recorder")
print("===================")
print("Everything you type here will be saved to a file.")
print("Each entry will include the date and time")
print("Type QUIT and press Enter to stop.\n")


# Opening the .txt file in append mode
file = open("keystrokes_recording.txt", "a")

# Start if input loop
while True:
    user_input = input("Type something: ")

    # Checking for QUIT command
    if user_input == "QUIT":
        print("Stopping recorder. Goodbye!")
        break

    # datetime.now() gets the current time
    current_time = datetime.now()

    # Convert the time into a readable string
    timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")

    # Write timestamp + input to file
    file.write(timestamp + " - " + user_input + "\n")

# Close the file
file.close()