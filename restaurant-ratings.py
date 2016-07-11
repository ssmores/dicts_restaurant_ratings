# your code goes here

def restaurant_ratings(filename):
    """Receives a file and returns it in alphabetical order"""

    restaurants_in_order = {}

    restaurant_file = open(filename)

    for line in restaurant_file:
        line = line.rstrip()
        restaurants = line.split(":")



        # for restaurant, ratings in restaurants_in_order.items():
            # restaurants_in_order[restaurant] = ratings
            # print restaurants_in_order
            #print "%s is rated at %d" % (restaurant, ratings)

        restaurant, ratings = restaurants
        restaurants_in_order[restaurant] = ratings
    
    for restaurant in sorted(restaurants_in_order):
        ratings = restaurants_in_order[restaurant]
        print "%s is rated at %s" % (restaurant, ratings)




#restaurant_ratings('scores.txt')