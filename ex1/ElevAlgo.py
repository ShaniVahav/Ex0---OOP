import csv
import math
from ex1.Elevator import Elevator

callList_ans = []


def FoundMinSrc(Callist):
    minimumSrc = 100000
    Index = 0
    for i in range(0, len(Callist)):
        if (int)(Callist[i]._src) < (minimumSrc):
            minimumSrc = (int)(Callist[i]._src)
            Index = i
    return Index


def SortbySrc(Callist):
    ans = []
    for i in range(0, len(Callist)):
        minindex = FoundMinSrc(Callist)
        ans.append(Callist[minindex])
        Callist.remove(Callist[minindex])
    return ans


def DivisionIntoSections(elevList, callList):
    minFloor = Elevator.MIN_FLOOR
    maxFloor = Elevator.MAX_FLOOR
    numberOfFloors = math.fabs(maxFloor - minFloor)
    list_Of_areaslists = []  # a list of lists
    elevList.sort(key=lambda Elevator: Elevator._speed)  # sort the elev by speed
    numberOfElev = len(elevList)
    numberOfAreas = math.ceil(numberOfElev / 2)
    areaSize = math.ceil(numberOfFloors / numberOfAreas)

    for i in range(0, numberOfAreas):
        temp = []
        for oneCall in range(0, len(callList)):
            infimum = minFloor + areaSize * i
            suprimum = minFloor + areaSize * (i + 1)
            call = callList[oneCall]
            if (infimum <= int(call._src) <= suprimum) & (infimum <= int(call._dest) <= suprimum):
                temp.append(call)

        temp = SortbySrc(temp)
        list_Of_areaslists.append(temp)

    return list_Of_areaslists


def mergeTo_one(list_Of_areaslists):
    mergeList = []
    for list in list_Of_areaslists:
        for call in list:
            mergeList.append(call)
    return mergeList


def AssignCalls_FromEachSection_to_SlowElevators(list_Of_areaslists, elevList, callList):
    sum = 0
    for elev in elevList:
        sum += elev._speed

    ratio = len(callList) / sum

    j = -1
    for subList in list_Of_areaslists:
        j += 1
        currentelev = elevList[j]  # a slow elevator
        for i in range(0, int(currentelev._speed * ratio)):  # number of calls for current elevator
            if i < len(subList):
                call = subList[i]
                if not call.isDelete:
                    call._elevIndex = currentelev._index
                    call.isDelete = True
                    callList_ans.append(call)

    return callList


def AssignRestCalls_to_FastElevators(list_Of_areaslists, elevList, callList):
    sum = 0
    for index in range(len(list_Of_areaslists), len(elevList)):
        sum += elevList[index]._speed

    ratio = len(callList) / sum  # from the rest of calls

    for index in range(len(list_Of_areaslists), len(elevList)):  # from the rest of the elevator
        filter(lambda call: (not callList[call].isDelete), callList)
        currentelev = elevList[index]
        for i in range(0, int(currentelev._speed * ratio)):  # number of calls to one elevator
            call = callList[i]
            if not callList[i].isDelete:
                call._elevIndex = currentelev._index
                call.isDelete = True
                callList_ans.append(call)

    filter(lambda x: callList[x].isDelete, callList)
    fastestElev_index = elevList[len(elevList) - 1]._index

    for call in callList:
        if not call.isDelete:
            call._elevIndex = fastestElev_index
            call.isDelete = True
            callList_ans.append(call)

    return callList_ans


def callsToCsv(arrayofCalls):
    filename = 'output.csv'
    newArrayofCalls = []
    for i in arrayofCalls:
        newArrayofCalls.append(i.__dict__.values())
    with open(filename, 'w', newline="") as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(newArrayofCalls)
