import obd
import time
import datetime

from pymongo import MongoClient

def main():
    # define On Board Diagnostics
    ports = obd.scan_serial()
    connection = obd.OBD(ports[0], baudrate=115200)

    # define

    client = MongoClient()
    db = client.selfdrivingcar

    # main loop

    while (True);
	cmd1    = obd.commands.RPM
	cmd2    = obd.commands.THROTTLE_POS
	cmd3    = obd.comands.ENGINE_LOAD
	cmd4    = obd.commands.SPEED

	response1 = connection.query(cmd)
	response2 = connection.query(cmd2)
	response3 = connection.query(cmd3)
	response4 = connection.query(cmd4)

	#ts = time.time()
	#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	result = db.restaurants.insert_one(
            "drivingparams": {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "RPM": str(response1),
                "THROTTLE_POS": str(response2),
                "ENGINE_LOAD": str(response3),
                "SPEED": str(response4)
            }
	)

if __name__=='__main__':
    main()
