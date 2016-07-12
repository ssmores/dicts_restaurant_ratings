# your code goes here

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

    restaurant_user = raw_input("Please enter a restaurant you'd like to rate: ")
    ratings_user = float(raw_input("Please enter a rating for the restaurant: "))

    restaurants_in_order[restaurant_user] = ratings_user


    for restaurant in sorted(restaurants_in_order):
        ratings = restaurants_in_order[restaurant]
        print "%s is rated at %d" % (restaurant, ratings)

    restaurant_file.close()
