import csv
import json

from ex1.Call import Call
from ex1.Elevator import Elevator


def elevator(build):
    # create a list of elevators
    elevList = []

    with open(build, "r") as f:
        data = json.load(f)

    Elevator.MIN_FLOOR = data['_minFloor']
    Elevator.MAX_FLOOR = data['_maxFloor']

    ourList = data['_elevators']
    for i in range(0, len(ourList)):
        _id = ourList[i]["_id"]
        _speed = ourList[i]["_speed"]
        _closeTime = ourList[i]["_closeTime"]
        _openTime = ourList[i]["_openTime"]
        _startTime = ourList[i]["_startTime"]
        _stopTime = ourList[i]["_stopTime"]
        currentElev = Elevator(_id, _speed, _closeTime, _openTime, _startTime, _stopTime)
        elevList.append(currentElev)

    return elevList


def call(c):
    # create a list of calls
    callList = []
    with open(c, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            _time = row[1]
            _src = row[2]
            _dest = row[3]
            currentCall = Call(_time, _src, _dest)
            callList.append(currentCall)

        return callList
