import csv
import sys

import Create
import ElevAlgo
from ElevAlgo import AssignRestCalls_to_AllElevators

strBuilding = sys.argv[1]
strCall = sys.argv[2]
output = sys.argv[3]

elevList = Create.elevator(strBuilding)
callList = Create.call(strCall)

if __name__ == "__main__":

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




 ElevAlgo.callsToCsv(callList_ans)

