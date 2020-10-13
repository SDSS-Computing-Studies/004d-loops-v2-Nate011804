#! python3
"""
##### Task 3
Given a typle that contains a series of numbers, list all the ones that are
divisible by 5
(2 points)

inputs:
none

outputs:
list of numbers
25
10
30
75
20
"""

numList = (25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99)
ChickenTendies = (5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100)
a = input( "number")
a = int(a)

answer = a / 5
if answer == int(answer):
     print("That number is divisible by 5")
