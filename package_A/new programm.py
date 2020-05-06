'''
Enter 'a' to add movie, 'l' to see your movie, 'f' to find movie, 'q, to quit movie.
- add movie 
- see movie
- find movie
- stop running the programm

Tasks:
- decide where to store movie.
- what is the format of the movie.
- Allow users the main interface and get their input. 
- show all their movie 
- find movie
- stop running programm when they type 'q'
'''
movies = []
movie = '''{
       name =   str
       director =   str
       year =   int()   }'''
def menu():
    q = "Enter 'a' to add movie , 'l' to see your movie, 'f' to find movie, 'q' to quit movie: "
    user = input(q)        
    while user != 'q':
        if user == 'a':
           add_movie()
        elif user == 'l':
           show_movie()
        elif user == 'f':
           find_movie()
        else:
            print("please try again")
        user = input(q)
        
 

def add_movie():
    name = input("enter your movie name   ")
    director = input("enter your director name  ")
    year = int(input("enter your movie year  "))

    movie = {
        'name': name,
        'director': director,
        'year': year
    }

    movies.append(movie)

def show_movie():
    for movie in movies:
        show_movie_details(movie)

def show_movie_details(movie):
        print(f"name = {movie['name']}  ")
        print(f"director = {movie['director']}  ")
        print(f"year = {movie['year']} ")

def find_movie():
    find = input("what property  of the movie are you looking for?  ")
    looking_for = input("what are you searching for? ")

    found = []
    
    for movie in movies:
        if movie[find] == looking_for:
            found.append(movie)
            

    for m in found:
        show_movie_details(m)
        
        


menu()
