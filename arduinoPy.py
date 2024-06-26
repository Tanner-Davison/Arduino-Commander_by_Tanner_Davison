import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

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
    command = input("Arduino Command (ON/OFF/exit)")
    serialInst.write(command.encode('utf-8'))

    if command == 'exit':
        exit()