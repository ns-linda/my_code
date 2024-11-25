class Test:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        
    def __del__(self):
        print("%s is deleted" % self.obj1)

ob= Test("linda", "catherine")

del(ob)
ob= Test("linda", "catherine")
print(ob.obj1)
print(ob.obj2)

print("Hello, World!")
from datetime import datetime

end_time = "2023-11-15_15.04.50.667193"
start_time = "2023-11-15_14.35.11.326031"

# Convert timestamps to datetime objects
end_datetime = datetime.strptime(end_time, "%Y-%m-%d_%H.%M.%S.%f")
start_datetime = datetime.strptime(start_time, "%Y-%m-%d_%H.%M.%S.%f")

# Calculate the time difference in seconds
time_difference = (end_datetime - start_datetime).total_seconds()

print("Time taken (seconds):", time_difference)

