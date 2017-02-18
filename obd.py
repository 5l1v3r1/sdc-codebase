import obd
import time
import datetime

ports = obd.scan_serial()      # return list of valid USB or RF ports
 # ['/dev/ttyUSB0', '/dev/ttyUSB1']
connection = obd.OBD(ports[0], baudrate=115200) # connect to the first port in the list

while(True):
    cmd = obd.commands.RPM # select an OBD command (sensor)
    cmd2 = obd.commands.THROTTLE_POS
    cmd3 = obd.commands.ENGINE_LOAD
    cmd4 = obd.commands.SPEED
    response = connection.query(cmd) # send the command, and parse the response
    response2 = connection.query(cmd2) # send the command, and parse the response
    response3 = connection.query(cmd3) # send the command, and parse the response
    response4 = connection.query(cmd4) # send the command, and parse the response

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(st)
    print(response.value) # returns unit-bearing values thanks to Pint
    print(response2.value) # returns unit-bearing values thanks to Pint
    print(response3.value) # returns unit-bearing values thanks to Pint
    print(response4.value) # returns unit-bearing values thanks to Pint

    #print(response.value.to("mph")) # user-friendly unit conversions
