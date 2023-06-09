# # Codecademy
# # Fundamentals of Python
# # Computer Science Track
# # 'Boredless Tourist' implementation

# # each set of numbers represents the exercise steps
# # associated with the adjacent code.

# # comments are double hashbanged
# # test functions are single hashbanged
# # select all and press 'cmd + /' to
# # uncomment all test functions while
# # maintaining code function by retaining comments

# # 1, 2, 3, 4
destinations = [
  "Paris, France",
  "Shanghai, China",
  "Los Angeles, USA",
  "São Paulo, Brazil",
  "Cairo, Egypt"
]

# # 5, 6, 7
test_traveler = [
  "Erin Wilkes",
  "Shanghai, China",
  [
    "historical site",
    "art"
  ]
]

# # 8, 9, 10
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# # 11
# # Unit test for get_destination_index() => 2
# print(get_destination_index("Los Angeles, USA"))

# # 12
# # Unit test for get_destination_index() => 0
# print(get_destination_index("Paris, France"))

# # 13, 14
# # Unit test for get_destination_index() => "ValueError: 'Hyderabad, India' is not in list"
# print(get_destination_index("Hyderabad, India"))

# # 15, 16, 17, 18
def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# # 19, 20, 21, 22, 23
# # Unit test for get_traveler_location() => 1
# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

# 24, 25
attractions = [[] for i in range(len(destinations))]

# # 26
# # Unit test for attractions empty 2D list via comprehension => [[],[],[],[],[]]
# print(attractions)

# # 27, 28, 29 (deprecated), 30 (deprecated), 31, 32
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)

# # 33, 34
# # Unit test for add_attraction() => [[], [], [['Venice Beach', ['beach']]], [], []]
# add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
# print(attractions)

# # 35, 36, 37
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# # 38, 39, 40, 41, 42, 43, 44, 45, 46
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

# # 47, 48, 49, 50, 51, 52
# # Unit test for find_attractions() => ['LACMA']
# la_arts = find_attraction("Los Angeles, USA", ["art"])
# print(la_arts)

# # 53, 54, 55, 56, 57, 58, 59, 60
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  count = 0
  while count < len(traveler_attractions) - 1:
    interests_string += "the " + traveler_attractions[count] + ", "
    count += 1
  while count < len(traveler_attractions):
    interests_string += "the " + traveler_attractions[count] + "."
    count += 1
  return interests_string

# # 61, 62, 63, 64
# # Unit test for get_attractions_for_traveler() => "Hi Dereck Smill, we think you'll like these places around Paris, France: the Arc de Triomphe."
# smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
# print(smills_france)

# # Congratulations, I suppose