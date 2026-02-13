# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

ticket = []
movie = []
def main():
    while True:
        Continue = input("Do you want to add a movie?(Y/N): ")
        if Continue == "Y":
            movies = input("Enter movie name: ")
            movie.append(movies)
            tickets = input("Enter number of movie tickets: ")
            ticket.append(tickets)
        else:
            break
    print("Your movies are ", movie)
    print("Your tickets are ", ticket)

if __name__ == '__main__':
    main()
