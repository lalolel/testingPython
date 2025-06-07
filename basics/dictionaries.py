user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


# Overwrite values

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# Dict Comprehensions
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

''' zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:
Takes a pair from the iterator of tuples
Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
Creates a key : value item in the students dictionary
Repeats steps 1-3 for the entire iterator of pairs '''

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
