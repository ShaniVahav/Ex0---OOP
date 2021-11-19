import math
import unittest

import Create
from Call import Call
from ElevAlgo import DivideToUpCallAndDownCalls, Sortbyabc, DivisionIntoSections, AssignRestCalls_to_AllElevators


class testSortByabs(unittest.TestCase):

    def testSortbyabc(self):
        strBuilding = "B5.json"
        strCall = "Calls_d.csv"

        elevList = Create.elevator(strBuilding)
        callList = Create.call(strCall)

        callList =Sortbyabc(callList,elevList)
        d = math.fabs((int)(callList[0]._src) - (int)(callList[0]._dest))
        for i in range(1,len(callList)):
            dr =  math.fabs((int)(callList[i]._src) - (int)(callList[i]._dest))
            self.assertTrue(d<=dr )
            d= dr

    def testDivisionIntoSections(self):
        strBuilding = "B5.json"
        strCall = "Calls_d.csv"
        elevList = Create.elevator(strBuilding)
        callList = Create.call(strCall)
        listf = DivisionIntoSections(elevList,callList)
        print((len(listf)))
        counter = 0
        for call in listf :
            if(call.isInListOfList):
                counter +=1
        self.assertTrue(counter > 0)


    def testAssignRestCalls_to_AllElevators(self):
        strBuilding = "B5.json"
        strCall = "Calls_d.csv"
        elevList = Create.elevator(strBuilding)
        callList = Create.call(strCall)
        newlist = []
        callList = AssignRestCalls_to_AllElevators(newlist,elevList,callList)
        for call in callList :
            self.assertTrue(call.isInListOfList,True)




