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

### Script

```python
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []
cmdList = ["ON", "OFF", "ALEXIS","CUSTOM"]

for one in ports:
    portList.append(str(one))
    print(str(one))

com = input("Select Com Port for Arduino #: ")

for i in range(len(portList)):
    if portList[i].startswith(str(com)):
        use = com  
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

while True:
    command = input("Arduino Command ex:(ON/OFF/ALEXIS/Custom/exit)")

    if command == 'CUSTOM':
        if command is not None and command != "cmdList":
            serialInst.write(command.encode('utf-8'))
    elif command == 'exit':
        serialInst.close()
        exit()
    elif command == 'cmdList': 
        for i in range(len(cmdList)):
            print(cmdList[i])

# Arduino Serial Command Sender

## Dependencies

- **pyserial:** Used for serial communication with the Arduino.

  Install the `pyserial` package via pip if it's not already installed:

  ```bash
  pip install pyserial
    elif command != 'exit':  
        serialInst.write(command.encode('utf-8'))
    else:
        print("Invalid command. Please try again.")
## Setup

1. Ensure the `pyserial` package is installed.
2. Connect your Arduino to your computer.
3. Run the script using a Python interpreter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out at tanner.davison95@gmail.com
