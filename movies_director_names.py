## pip install IMDbPY

from imdb import IMDb

# Initialize IMDb object
ib = IMDb()

# Get movie name from user
movie_name = input("Enter the movie name: ").strip()

# Validate input
if not movie_name:
    print("No movie name provided. Please try again.")
else:
    try:
        # Search for the movie
        movies = ib.search_movie(movie_name)

        if movies:
            # Use the first search result
            movie = movies[0]
            ib.update(movie)  # Fetch detailed information
            
            print(f"\nMovie: {movie.get('title', 'Unknown')} ({movie.get('year', 'Unknown')})")

            # Get directors
            directors = movie.get('directors')
            if directors:
                print("\nDirector(s):")
                for director in directors:
                    print(f"  - {director['name']}")
            else:
                print("\nNo director information found.")

            # Optionally display other details
            print(f"\nGenres: {', '.join(movie.get('genres', []))}")
            plot = movie.get('plot')
            if plot:
                print(f"\nPlot: {plot[0]}")

        else:
            print("Movie not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

