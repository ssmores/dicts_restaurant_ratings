# your code goes here
import random

def restaurant_ratings(filename):
    """Receives a file and returns it in alphabetical order"""

    restaurants_in_order = {}

    restaurant_file = open(filename)

    for line in restaurant_file:
        line = line.rstrip()
        restaurants = line.split(":")

        restaurant, ratings = restaurants
        ratings = float(ratings)
        restaurants_in_order[restaurant] = ratings


    user_name = raw_input("Hello! What is your name? ")

    restaurant_info = raw_input("Do you want to hear about a restaurant? type 'q' to quit ")

    while restaurant_info != "q":
         
        random_restaurant = random.choice(restaurants_in_order.keys())
        print "The rating for %s is %d" % (random_restaurant, restaurants_in_order[random_restaurant])

        new_rating = float(raw_input("What is your rating for this restaurant? "))
        restaurants_in_order[random_restaurant] = new_rating

        restaurant_info = raw_input("Do you want to hear another restaurant? type 'q' to quit ")


    # restaurant_user = raw_input("Please enter a restaurant you'd like to rate: ")
    # ratings_user = float(raw_input("Please enter a rating for the restaurant: "))

    # restaurants_in_order[restaurant_user] = ratings_user

    for restaurant in sorted(restaurants_in_order):
        ratings = restaurants_in_order[restaurant]
        print "%s is rated at %d" % (restaurant, ratings)

    



    restaurant_file.close()
