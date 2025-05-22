movies = []
review = {}


def validate_movie(name):
    name = name.strip()
    if 'a' in name.lower() and len(name) > 8:
        return True
    return False


print("=== Movie Registration ===")
count = 0
while count < 5:
    movie = input(f"Enter the name of the {count + 1}° movie: ")
    if validate_movie(movie):
        movies.append(movie.strip())
        print("The movie has been added!")
    else:
        print("The movie was not added. Please ensure that it contains the letter 'A' and has more than 8 characters.")
    count += 1

print("\n=== Movie Score ===")
for movie in movies:
    while True:
        try:
            score = float(input(f"Type the rating for '{movie}' (0 to 10): "))
            if 0 <= score <= 10:
                review[movie] = score
                break
            else:
                print("Please, type a number from 1 to 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("\n=== Registered Movies ===")
print("Listed Movies")
for f in movies:
    print(" -", f)

total_movies = len(movies)
print(f"\nTotal movies added: {total_movies}")

if total_movies > 0:
    average_rating = sum(review.values()) / total_movies
    print(f"Average movie ratings: {average_rating:.2f}")
    biggest_score = max(review, key=review.get)
    print(f"Movie with biggest rating: '{biggest_score}' with rating {review[biggest_score]:.2f}")
else:
    print("No movies were registered for analysis.")

remove_movie = input("\nDo you want to remove any movies? (Y/N): ").strip().lower()
if remove_movie == "s":
    remove_movie_name = input("Enter the name of the movie you want to remove: ").strip()
    if remove_movie_name in movies:
        movies.remove(remove_movie_name)
        if remove_movie_name in review:
            del review[remove_movie_name]
        print(f"Movie '{remove_movie_name}' removed with success!")
    else:
        print("The movie entered is not on the list.")

    total_movies2 = len(movies)
    print("\n=== Updated Report ===")
    print("Listed Movies:")
    for f in movies:
        print(" -", f)
    print(f"\nTTotal movies added: {total_movies2}")

    if total_movies2 > 0:
        average_rating = sum(review.values()) / total_movies2
        print(f"Average movie ratings: {average_rating:.2f}")
        biggest_score = max(review, key=review.get)
        print(f"Movie with biggest rating: '{biggest_score}' with rating {review[biggest_score]:.2f}")
    else:
        print("There are not enough movies for analysis after removal.")
else:
    print("\nNo removals were made. Program finished.")