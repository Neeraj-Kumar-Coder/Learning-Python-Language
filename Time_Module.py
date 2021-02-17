import time
initial_time = time.time()
for i in range(50):
    print("Loop", end=" ")
print("\nTime taken =", time.time()-initial_time, "seconds")

k = 0
initial_time = time.time()
while(k < 50):
    print("Loop", end=" ")
    k += 1
print("\nTime taken =", time.time()-initial_time, "seconds")


local_time = time.asctime(time.localtime(time.time()))
print(local_time)
