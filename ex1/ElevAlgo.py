import csv
import math
from ex1.Elevator import Elevator

callList_ans = []


def DivideToUpCallAndDownCalls(Callist):
    downCalls = []
    UpCalls = []
    for call in Callist :
        if(call._src < call._dest) :
            downCalls.append(call)
        else :
            UpCalls.append(call)
    return UpCalls + downCalls
            


def FoundMinSrc(Callist) :
    minimumSrc = 100000
    Index = 0
    for i in range(0,len(Callist)):
        if (int)(Callist[i]._src)< (minimumSrc):
            minimumSrc = (int)(Callist[i]._src)
            Index = i
    return  Index




def SortbySrc(Callist,elvelist):
    ans = []
    for i in range(0, len(Callist)):
        minindex = FoundMinSrc(Callist)
        ans.append(Callist[minindex])
        Callist.remove(Callist[minindex])
    if(len(Callist) < 200 or len(elvelist) <= 2  ):
        return ans
    else :
        ans = DivideToUpCallAndDownCalls(ans)
    return ans

















def DivisionIntoSections(elevList, callList):
    minFloor = Elevator.MIN_FLOOR
    maxFloor = Elevator.MAX_FLOOR
    numberOfFloors = math.fabs(maxFloor - minFloor)
    list_Of_areaslistsFinal = []
    list_Of_areaslists = []  # a list of lists
    elevList.sort(key=lambda Elevator: Elevator._speed)  # sort the elev by speed
    numberOfElev = len(elevList)
    numberOfAreas = numberOfElev
    if(numberOfElev > 2 ):
        areaSize = math.ceil(numberOfFloors / math.ceil(numberOfAreas/4))
    else :
        areaSize = math.ceil(numberOfFloors / math.ceil(numberOfAreas))
    for i in range(0, numberOfAreas):
        temp = []
        for oneCall in range(0, len(callList)):
            infimum = minFloor + areaSize * i
            suprimum = minFloor + areaSize * (i + 1)
            call = callList[oneCall]
            if (infimum <= int(call._src) <= suprimum) & (infimum <= int(call._dest) <= suprimum):
                if not call.isInListOfList:
                    call.isInListOfList = True
                    temp.append(call)  # todo reputation ?

        temp = SortbySrc(temp,elevList)
         #sortedBySrctemp = SortbySrc(temp)
        list_Of_areaslists.append(temp)
    for list in list_Of_areaslists :
           for c in list :
               list_Of_areaslistsFinal.append(c)
    return list_Of_areaslistsFinal








def AssignRestCalls_to_AllElevators(finalCallList, elevList, callList):
    for call in callList:
        if not call.isInListOfList:
            call.isInListOfList = True
            finalCallList.append(call)
    sum = 0
    for index in range(0, len(elevList)):
        sum += elevList[index]._speed

    ratio = (len(finalCallList)) / sum  # from the rest of calls
    print(len(finalCallList))


    dex = 0
    for index in range(0, len(elevList)):                      # from the rest of the elevator
        currentelev = elevList[index]
        for i in range(dex ,dex+ int(currentelev._speed * ratio)):  # number of calls to one elevator
            call = finalCallList[i]
            call._elevIndex = currentelev._index
            if not call.isMatched:
                call.isMatched = True
                callList_ans.append(call)
        dex = dex +int(currentelev._speed * ratio)
    fastestElev_index = elevList[len(elevList) -1]._index
    for call in finalCallList:
        if not call.isMatched :
            call._elevIndex = fastestElev_index
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
