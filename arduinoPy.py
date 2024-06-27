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
    elif command != 'exit':  
        serialInst.write(command.encode('utf-8'))
    else:
        print("Invalid command. Please try again.")