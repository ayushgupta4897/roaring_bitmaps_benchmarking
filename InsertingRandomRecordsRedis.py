import redis
import random

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Set of generated restaurant IDs to ensure uniqueness
generated_ids = set()

# Function to manage Redis Bitmaps
def manage_redis_bitmaps(restaurant_id, dish_ids):
    if 7 in dish_ids:  # Assuming 7 corresponds to pizza
        r.setbit('dish_7', restaurant_id, 1)
    if 1 in dish_ids:  # Assuming 1 corresponds to north Indian
        r.setbit('dish_1', restaurant_id, 1)
    # Add more if conditions based on your dish_ids and their meaning
    
    # Setting bits for status and dine_out attributes
    r.setbit('active_bitmap', restaurant_id, 1)
    r.setbit('dineout_bitmap', restaurant_id, 1)

# Generating 1 million sparse restaurant IDs and managing bitmaps
for _ in range(1000000):
    while True:
        restaurant_id = random.randint(1, 1000000000)
        if restaurant_id not in generated_ids:
            generated_ids.add(restaurant_id)
            break
    
    # Randomly assign dish_ids to each restaurant
    dish_ids = random.sample(range(1, 16), random.randint(1, 15))
    
    # Call the function to manage Redis Bitmaps
    manage_redis_bitmaps(restaurant_id, dish_ids)
