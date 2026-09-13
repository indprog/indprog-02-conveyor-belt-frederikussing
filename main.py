
motors = int(input()) 
weight = int(input())

if weight / motors <= 12:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")

