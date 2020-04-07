#First Data structure we use are lists

#List of favorite sports

fav_sport = ['fitness', 'boxing', 'jogging']

#get first value out of the list
#indexes starting with 0 so the first value has index 0

print(fav_sport[0])

print('my most favorite sport is ' + fav_sport[0])

#Lists can be nested in another list so list can be list of list;)
fav_food = ['Pizza', 'Burger', 'Salat']
my_favorites = [fav_sport, fav_food]

print('My first favorite list ' + str(my_favorites[0]))
print('My second favorite list ' + str(my_favorites[1]))

print(*my_favorites[0], sep = ' and ')

#if you want to get the value of the first element of the first list

print('my overall favorite is ' + my_favorites[0][0])