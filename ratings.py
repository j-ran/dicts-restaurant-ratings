"""Restaurant rating lister."""

# Create a function that takes in restaurant names and scores
# Prints them out
def restaurant_ratings(filename):
    """Create a function that takes in restaurant names and scores
    Outputs a sorted list.
    """
# open file
    scores = open(filename)
# make an empty dictionary    
    restaurantnames_and_scores = {}
    for line in scores:
        restaurant_info = line.rstrip().split(":")
        # test the output: print(restaurant_info) – test the output 
# unpack the list made with restaurant_info        
        restaurant_name, score = restaurant_info
# define dict = {'Ministry Munchies': 1, 'The Porcupine': 5}        
        restaurantnames_and_scores[restaurant_name] = score
#input from user
    print("What restaurant would you like to rate?")
    user_restaurant = input("> ")
    user_score = input("Please provide restaurant score: ")
    # test the output: print([user_restaurant, user_score])
# add the new name and rating to the existing list of names and ratings    
    restaurantnames_and_scores[user_restaurant] = user_score
# alphabetize the list        
    sorted_list = sorted(restaurantnames_and_scores)
# for i in sorted_list    
# reference the dict pair
    for restaurant_name in sorted_list:
        print(f'{restaurant_name} is rated at {restaurantnames_and_scores[restaurant_name]}.')


# The program should:
#     Prompt the user for a restaurant name
#     Prompt the user for a restaurant score
#     Store the new restaurant/rating in the dictionary
#     Print all of the ratings in alphabetical order (including the new one, of course)


restaurant_ratings("scores.txt")
