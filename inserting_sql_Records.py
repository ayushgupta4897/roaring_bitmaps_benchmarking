import mysql.connector
import random

conn = mysql.connector.connect(user='your_username', password='your_password', host='127.0.0.1', database='your_db')
cursor = conn.cursor()

# Define the function to insert data into the restaurants and dishes tables
def insert_data():
    generated_ids = set()  # Keep track of generated restaurant IDs
    
    for _ in range(1000000):
        # Generate a unique restaurant_id between 1 and 1 billion
        while True:
            restaurant_id = random.randint(1, 1000000000)
            if restaurant_id not in generated_ids:
                generated_ids.add(restaurant_id)
                break
        
        status = random.choice([True, False])
        dine_out = random.choice([True, False])
        
        restaurant_query = "INSERT INTO restaurants (restaurant_id, status, dine_out) VALUES (%s, %s, %s);"
        cursor.execute(restaurant_query, (restaurant_id, status, dine_out))
        
        # Randomly assign dishes to the restaurant
        dish_ids = [1, 3, 5, 7]  # IDs for north Indian, Asian, Italian, and pizza
        assigned_dishes = random.sample(dish_ids, random.randint(1, len(dish_ids)))
        for dish_id in assigned_dishes:
            dish_query = "INSERT INTO dishes (dish_id, restaurant_id) VALUES (%s, %s);"
            cursor.execute(dish_query, (dish_id, restaurant_id))
    
    conn.commit()

# Execute the function to insert data
insert_data()

# Close the connection
cursor.close()
conn.close()
