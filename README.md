# Python Arduino Commander

This Python script interacts with an Arduino board via a serial connection. It allows you to select a COM port, send commands to the Arduino, and manage the serial connection.

## Features

- **List Available COM Ports:** Detects and displays available COM ports for connecting to the Arduino.
- **Select COM Port:** Allows the user to choose the appropriate COM port for communication.
- **Send Commands:** Sends predefined commands or custom commands to the Arduino.
- **Command List:** Provides a list of available commands that can be sent to the Arduino.
- **Exit Command:** Closes the serial connection and exits the script.

## Code Overview

### Imports

- `serial.tools.list_ports`: Used to list available serial ports.

### Main Functionalities

1. **List COM Ports:**
   - Retrieves and prints available COM ports.
   
2. **Select COM Port:**
   - Prompts the user to select a COM port and opens the serial connection.

3. **Command Input:**
   - Allows the user to input commands to be sent to the Arduino.
   - Commands can be:
     - `"ON"`
     - `"OFF"`
     - `"ALEXIS"`
     - `"CUSTOM"` (for custom commands)
     - `"cmdList"` (to print available commands)
     - `"exit"` (to close the serial connection and exit the script)

4. **Command Processing:**
   - Sends the command to the Arduino or prints an error message for invalid commands.

## Features

- **Port Detection:** Automatically detects available COM ports and allows you to select the correct port for your Arduino.
- **Command Sending:** Sends various commands to the Arduino such as "ON", "OFF", "ALEXIS", and "CUSTOM".
- **Interactive Console:** Provides an interactive console for inputting commands and viewing results.

## Dependencies

- **pyserial:** Used for serial communication with the Arduino.

  Install the `pyserial` package via pip if it's not already installed:

  ```bash
  pip install pyserial
  
## Setup

1. Ensure the `pyserial` package is installed.
2. Connect your Arduino to your computer.
3. Run the script using a Python interpreter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out at tanner.davison95@gmail.com
