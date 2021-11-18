# Ex1_OOP
###### An Off-line Elevator Algorithm

## About the project.
Given a `building`, with a maximum floor and a minimum floor, and with smart elevators (ie: [https://www.designingbuildings.co.uk/wiki/Smart_elevators]())
where each `elevator` has its own characteristics: (speed per floor, door opening time, stopping time, etc.)
Using a `list of future readings` (ie, an offline algorithm),
we created an algorithm Which mainly takes into account the speed of the elevators
and places each call to a particular elevator so that **the aggregate total waiting time
of all requests is as minimal as possible**

## Literature review.

In our project we used several sources, some of which are:
1. _The Science Behind Elevators -_ https://www.youtube.com/watch?v=xOayymoIl8U
2. _Elevator System Design -_ https://youtu.be/siqiJAJWUVg?t=1236
3. _The Hidden Science of Elevators -_ -https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden
/science-of-elevators

## Pseudo Code.
    building <- input(json)
    calls <- input(csv)
    
    listOf_Elevators <- A list from building.json file
    listOf_Calls <- A list from calls.csv file
    
    listOf_Elevators.sort(bySpeed)  # The first elevator ia the slowest and the last is the fastest 
    listOf_Calls.sort(bySrc then by_absoluteValue(src-dest) then by_upCalls)
    
    for all the elevator[i] in listOf_Elevators:
        sumSpeed += elevator[i].speed  # The sum of the speeds of all the elevators
        
    ratio <- ((number of calls) / sumSpeed) # Number of calls given to an elevator, per speed
    
    for all the elevator[i] in listOf_Elevators:
        # The number of calls the current elevator will receive
        numberOfCalls <- elevator[i].speed*ratio 
        
        # Match for elevator[i] _numberOfCalls_ call from listOf_Calls, in order
        for i in range(0, numberOfCalls):
            for call in ListOf_Calls who doesn't match yet:
                call.matchedTo(elevator[i])
                
    listOf_Calls --> output.csv

## Class diagram.
    
![image](https://user-images.githubusercontent.com/92265738/142400751-f390dcf2-1d10-4920-8487-da49a4444246.png)
