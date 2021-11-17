import Create
from ex1 import ElevAlgo

strBuilding = "B5.json"  # input()   # todo
strCall = "Calls_b.csv"  # input()       # todo

elevList = Create.elevator(strBuilding)
callList = Create.call(strCall)

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
    list_Of_areaslists = ElevAlgo.DivisionIntoSections(elevList, callList)

    # Merge the lists into one
    mergeList = ElevAlgo.mergeTo_one(list_Of_areaslists)

    # Distribution the calls to slow lifts
    callList = ElevAlgo.AssignCalls_FromEachSection_to_SlowElevators(list_Of_areaslists, elevList, callList)

    # Distribution the calls to flow lifts
    callList_ans = ElevAlgo.AssignRestCalls_to_FastElevators(list_Of_areaslists, elevList, callList)

    callList_ans.sort(key=lambda Call: Call._id)

ElevAlgo.callsToCsv(callList_ans)
