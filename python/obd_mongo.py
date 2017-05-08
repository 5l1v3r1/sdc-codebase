import time
import datetime
import numpy as np
import cv2
import obd

from pymongo import MongoClient

def main():
    # define On Board Diagnostics

    ports = obd.scan_serial()
    connection = obd.OBD(ports[0], baudrate=115200)

    client = MongoClient()
    db = client.selfdrivingcar

    while (True):

	cmd1    = obd.commands.RPM
	cmd2    = obd.commands.THROTTLE_POS
	cmd3    = obd.commands.ENGINE_LOAD
        cmd4    = obd.commands.SPEED

	response1 = connection.query(cmd1)
	response2 = connection.query(cmd2)
	response3 = connection.query(cmd3)
	response4 = connection.query(cmd4)

        print(response1)
        print(response2)
        print(response3)
        print(response4)

        ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	result = db.selfdrivingcar.insert_one({
                "drivingparams": {
                    "timestamp": st,
                    "RPM": str(response1.value),
                    "THROTTLE_POS": str(response2.value),
                    "ENGINE_LOAD": str(response3.value),
                    "SPEED": str(response4.value)
                }
            }
	)

	print(st + ' ' + str(result))


    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
