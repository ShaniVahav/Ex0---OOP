class Elevator:
    INDEX = -1
    MIN_FLOOR = 0
    MAX_FLOOR = 0

    def __init__(self, _id, _speed, _closeTime, _openTime, _startTime, _stopTime):
        Elevator.INDEX += 1
        self._index = Elevator.INDEX
        self._id = _id
        self._speed = _speed
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime

    def toString(self):
        ans = "index = " + str(self._index) + ", id = " + str(self._id) + ", speed = " + str(
            self._speed) + ", closeTime = " + str(self._closeTime)
        ans += ", openTime = " + str(self._openTime) + ", startTime = " + str(self._startTime)
        ans += ", stopTime = " + str(self._stopTime) + ", callList = " + str(self._listOfCalls)
        return ans
