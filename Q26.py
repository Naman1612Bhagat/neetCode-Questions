# Car Fleet
# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

from typing import List

target = 10
position = [4,1,0,7] 
speed = [2,2,1,1]
# output = 3

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  
        times = [(target - pos) / spd for pos, spd in cars]
        print(times)
        print(cars)

        fleets = 0
        stack = []

        for time in times:
            if not stack or time > stack[-1]:
                fleets += 1          # new fleet formed
                stack.append(time)  # this car leads a new fleet

        return fleets
        
    
solution = Solution()
print(solution.carFleet(target, position, speed))