def movieRating(l):
    if l["imdb"] > 5.5:
        return True
    return False

def movielist(dictionary):
    movielist = []
    for i in dictionary:
        if movieRating(i):
            movielist.append(i)
    return movielist

def categoryFilter(dictionary):
    # s = str(input("Введите название категории: "))
    s = "Romance"
    for i in dictionary:
        if i["category"] == s:
            print(i['name'], i['imdb'], i['category'])
        
    return

def averageScore(dictionary):
    total = 0
    counter = 0
    for i in dictionary:
        total += i['imdb']
        counter += 1

    avg = total/counter
    print(f'The average IMDB score is {avg:.2f}')
    return

def avgScoreCategory(dictionary):
    total = 0
    counter = 0
    # s = str(input("Введите категорию: "))
    s = 'Romance'
    for i in dictionary:
        if i['category']==s:
                total += i['imdb']
                counter += 1 

    avg = total/counter
    print(f'The average IMDB score of {s} category is {avg:.2f}')
    return


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

listtt = movielist(movies)

for i in listtt:
    print(i['name'], i['imdb'], i['category'])

print()

categoryFilter(movies)

print()

averageScore(movies)

print()

avgScoreCategory(movies)