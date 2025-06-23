# for variable in range(start, stop, step): (syntax)
# while condition: (syntax)
  
import time

for i in range(10, 0, -2):
  print(i)
  time.sleep(2)
print("Welcome Back!")

# Countdown program

import time

# 1: Get user input for countdown start
start = int(input("Enter the number to start the countdown from: "))

# 2: Countdown using a while loop
print("\n Starting Countdown")
while start > 0:
  print(start)
  time.sleep(1)
  start -= 1

# 3: Print final message
print("Countdown Complete!")