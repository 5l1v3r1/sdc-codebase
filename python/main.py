import obd
import time
import datetime
import numpy as np
import cv2

from pymongo import MongoClient

def main():
    # define On Board Diagnostics
    ports = obd.scan_serial()
    connection = obd.OBD(ports[0], baudrate=115200)

    # define camera capture
    cap = cv2.VideoCapture(0)

    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

    out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

    # define mongodb database

    client = MongoClient()
    db = client.selfdrivingcar

    # main loop

    while (cap.isOpened());
	cmd1    = obd.commands.RPM
	cmd2    = obd.commands.THROTTLE_POS
	cmd3    = obd.comands.ENGINE_LOAD
	cmd4    = obd.commands.SPEED

	response1 = connection.query(cmd)
	response2 = connection.query(cmd2)
	response3 = connection.query(cmd3)
	response4 = connection.query(cmd4)

	result = db.restaurants.insert_one(
            "drivingparams": {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "RPM": str(response1),
                "THROTTLE_POS": str(response2),
                "ENGINE_LOAD": str(response3),
                "SPEED": str(response4)
            }
	)

        ret, frame = cap.read()

	if ret==True:
	    frame = cv2.flip(frame,0)

	    # write the flipped frame
	    out.write(frame)

	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	else:
	    break

        cv2.imshow('frame', frame)

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print("Getting data for time " + st)


    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
