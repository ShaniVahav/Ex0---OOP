import csv

from ex1 import ElevAlgo, Create
from ex1.ElevAlgo import AssignRestCalls_to_AllElevators

strBuilding = "B4.json"
strCall = "Calls_c.csv"

elevList = Create.elevator(strBuilding)
callList = Create.call(strCall)


"""
ll = SortbySrc(callList)
print(len(ll))
print("sssss")
for call in ll :
    print(call.toString())
"""








if len(elevList) == 1:
    callList_ans = []
    for call in callList:
        call._elevIndex = 0
        callList_ans.append(call)
else:
    # crate a list of lists (each sublist represents a section)
    """"
       Create a list that contains several lists
       Half of the number of lifts will respond to calls according to
       the sections designated for them, this function sorts sections.
       Each sublist is a section.
    """

    list_Of_areaslistsFinal = ElevAlgo.DivisionIntoSections(elevList, callList)

    callList_ans = AssignRestCalls_to_AllElevators( list_Of_areaslistsFinal, elevList, callList)
    Counter1 = 0
    Counter2 = 0
    for call in callList_ans :
        if call._elevIndex == 0 :
            Counter1 = Counter1 +1
        else:
            Counter2 = Counter2 +1
    print(Counter2)
    print(Counter1)



ElevAlgo.callsToCsv(callList_ans)

