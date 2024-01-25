def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Gagandeep Kaur",
        "student_id": 10312221,
        "pizza_toppings": ["ONIONS", "PEPPERONI", "PEPPERS"],
        "movies": [
            {"tittle": "zoolander", "genre": "comedy"},
            {"tittle": "back to the future", "genre": "sci-fi"},
        ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"tittle": "anchorman", "genre": "comedy"}
    about_me["movies"].append(new_movie)

    print_student_name_and_id(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(
        f"My name is {full_name}, but you can call me Miss {first_name}.\nMy student ID is {student_id}."
    )
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    add_pizza_toppings_simple(about_me, 'Cheese', 'tomotao')

    print_pizza_toppings("pizza_toppings")
    print_movie_genres("movies")
    print_movie_titles(about_me['movies'])

def add_pizza_toppings_simple(about_me, *new_toppings):
    about_me['pizza_toppings'].extend(new_toppings)
    about_me['pizza_toppings'] = sorted(about_me['pizza_toppings'])

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f"My favourite pizza toppings are:"Onions")
    for topping in  ['pizza_toppings']:
        print(f"- {topping}")
    print()
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
genres = [movie['comedy'] for movie ['zoolandar']]
    print(f"I like to watch movies.\n")

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
     
if __name__ == '__main__':
    main()