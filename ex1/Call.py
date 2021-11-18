class Call:
    ID = 0

    def __init__(self, _time, _src, _dest):
        self.str = "Elevator Call"
        self._time = _time
        self._src = _src
        self._dest = _dest
        self._zero = 0
        self._elevIndex = -1
        self.isMatched = False
        self.isInListOfList = False
        self._id = Call.ID
        Call.ID += 1

    def toString(self):
        ans = self.str + "," + str(self._time) + "," + str(self._src) + ","
        ans += str(self._dest) + ",0," + str(self._elevIndex)
        return ans
