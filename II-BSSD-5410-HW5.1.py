import requests

# API Key and constants
FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
RELEASE_DATE = "2016-01-01" 
API_KEY = '7da1efeeea871e2ca9596dea6307724a'

# Function to get the list of films for a given actor ID
def get_film_list(actor_id):
    params = {
        "api_key": API_KEY,
        "with_people": actor_id,
        "primary_release_date.gte": RELEASE_DATE
    }
    
    r = requests.get(FILM_LIST_PATH, params=params)
    data = r.json()
    return data

# Convert the film data to a set of film titles
def data_to_set(data):
    film_set = set()
    for res in data['results']:  # For each element in results array
        film_set.add(res['title'])  # Add film title to set
    return film_set

# Main function to compare two actors' films
def main():
    # Prompt the user for two actor IDs
    actor1_id = input("Enter the first actor's ID: ")
    actor2_id = input("Enter the second actor's ID: ")
    
    # Get film lists for both actors
    actor1_data = get_film_list(actor1_id)
    actor2_data = get_film_list(actor2_id)
    
    # Convert the data to sets
    actor1_films = data_to_set(actor1_data)
    actor2_films = data_to_set(actor2_data)
    
    # Find common movies using set intersection
    common_movies = actor1_films & actor2_films
    
    # Print the results
    if common_movies:
        print("Movies in common:")
        for movie in common_movies:
            print(f"- {movie}")
    else:
        print("No current films in common.")

if __name__ == "__main__":
    main()
