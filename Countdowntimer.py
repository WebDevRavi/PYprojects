import time
print("This programme is to do count down")
Count_time = int(input("Enter time : "))
zero = 0
while Count_time>zero:
    time.sleep(1)
    print(Count_time)
    Count_time = Count_time - 1
print("Timer Ends!!")