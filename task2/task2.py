films = { 
 "Семёнова" : {
    "New life": 40,
    "Love trap": 45,
    "Toxic": 104,
    "You": 51,
    "My country kitchen": 25
 }, 
 "Золотова" : {
    "Big door prize": 103,
    "Flight attendant": 38,
    "Just ask for it": 18,
    "Masters of flip": 43
 }, 
 "Вишнякова" : {
    "Happy Cleaners": 93,
    "Olivia": 30,
    "The new frontier": 23
 }
}
def salary(films):
    for i in range(len(films)):
        person = list(films)[i]
        key_1 = list(films.values())[i]
        sal = 35 * sum(key_1.values())
        print(f'{person} заработала {sal}')

salary(films)
