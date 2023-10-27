import redis
import time

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Record the start time
start_time = time.time()

# Execute the BITOP command
r.bitop('AND', 'result_bitmap', 'dish_7', 'active_bitmap', 'dineout_bitmap')

# Record the end time
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"The BITOP command took {execution_time} seconds to execute.")
