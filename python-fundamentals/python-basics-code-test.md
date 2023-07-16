1. Research has shown that when shoppers see odd prices like $1.99 or $7.95, they assume something is on sale. Our store makes sure all discounted items have odd prices while normal items have even prices.

The sale at our store has ended, and we need to find all of the items that have odd prices so we can remove the discount.

You will need to:

- Fix the syntax error in the program.
- Use a for loop to loop over the all_items list which contains each item’s name and price.
- Find all items with an odd price and add the name of the item to the discounted_items list.
- Make sure the testing code which prints discounted_items is at the bottom of your code. Do NOT print out items that are not discounted.

Reminder: Even numbers are divisible by 2 and odd numbers are not divisible by 2.

```py
# All of our store items
all_items = [["Taffy", 1], ["Chocolate", 2], ["Cup", 5], ["Plate", 10], ["Bowl", 11], ["Silverware", 22]]

# Empty discounted_items list
discounted_items = []

# Your code here
for item in all_items:
  if item[1] % 2 != 0:
    discounted_items.append(item[0])

# For testing purposes: print discounted list
print(discounted_items)
```

2. You are going to the store to buy dog treats, and you want to buy as many dog treats as you can. You are only limited by three things:

How much money is in your pocket.
How many dog treats that the store has in stock.
The price of the dog treats.
Write a buy_items() function that will tell you how many dog treats you can buy. (You’re naming it buy_items() so you can use this next time you go to the store too!)

You will need to:

Fix the NameError.
- Add three parameters to buy_items: The money you have, how many dog treats the store has in stock, and the price of the dog treats.
- Use a while loop in your function to calculate how many dog treats you can buy.
- return the total number of dog treats you were able to buy (num_bought).
- Make sure the labeled testing code is at the bottom of your code. It should be:

```py
total_1 = buy_items(100, 10, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))
```
Note: If you create an infinite loop, refresh your page to try again.

```py
starting_money = 100
starting_num_items = 10
item_price = 4

# Your code here
def buy_items(funds, treat_stock, treat_price):
  num_bought = 0
  while treat_stock > 0:
    if funds > treat_price:
      num_bought += 1
      funds -= treat_price
      treat_stock -= 1
    else:
      break
  return num_bought

total = buy_items(starting_money, starting_num_items, item_price)
print("You were able to buy " + str(total) + " items.")

# For testing purposes
total_1 = buy_items(100, 10, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))
```

3. You’ve just written a program for your latest project and now you need to commit the project to a new GitHub repo. Make sure to:

- Run your Python 3 program to test it. Your program is named startup.py.
- Initialize git and add startup.py to the staging area.
- Commit startup.py. Include the commit message in your terminal command.

Don’t use clear to clear the terminal. Make sure your commands are visible on the Terminal before checking your work.

```bash
$ python3 startup.py
Workspace startup in progress...
Workspace started successfully!
$ git init
Initialized empty Git repository in /home/ccuser/workspace/assessment-f925dc9418604a37801951a6a3b081ab/.git/
$ git add startup.py
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   startup.py

$ git commit -m 'commit message'
[master (root-commit) de32a0a] commit message
 1 file changed, 5 insertions(+)
 create mode 100644 startup.py
$
```

4. Hashtags are used in lots of social media to group together posts of similar types. Hashtags are created by putting a # before a word or series of words. #codecademy is an example of a hashtag.

You’re creating a class, called HashtagsCreator, that will take a list of terms and turn them all into hashtags. So far, you’ve only created two parts of this class:

The constructor, which creates a list of hashtags from a list of Strings.
A method to list the newly created hashtags, list_hashtags().
Right now, the constructor adds a # before every term and then adds that term to our list of hashtags. Unfortunately, you forgot to consider two edge cases:

Some terms may already start with a #, so you should NOT add another # to the beginning.
Some terms start with a @ which should be removed before you add a #.
For example:

#coding should stay #coding and NOT become ##coding.
@oop should become #oop and NOT become #@oop.
You need to fix the constructor so that terms that already start with # or @ are correctly turned into hashtags. For now, you don’t need to address any other edge cases or worry about spaces.

If you Run your code, some methods have already been written that will help you test your code. Try it!

```py
class HashtagsCreator:
  
  def __init__(self,list_of_terms):
    self.hashtags = []
    
    for term in list_of_terms:
      if term[0] == '@':
        self.hashtags.append("#" + term[1:])
      elif term[0] == '#':
        self.hashtags.append(term)
      else:
        self.hashtags.append("#" + term)
      
  def list_hashtags(self):
    for hashtag in self.hashtags:
      print(hashtag)

# Do not edit testing code
test_hashtags = HashtagsCreator(["@codecademy", "#python", "programming", "#strings"])
test_hashtags.list_hashtags()
```

5. You’re programming a number guessing game class. This class sets up a game that chooses a secret number between 1 and 10 and lets players guess the number.

The class has a dictionary called player_guesses which stores player guesses. In player_guesses, a player’s name is the key and their guess is the associated value. The constructor for our class takes in a list of names and adds each player name to player_guesses and initializes their guess to -1. The -1 value is used to mark that a player hasn’t guessed yet.

```py
def __init__(self, player_names):
  self.player_guesses = {}
  for name in player_names:
    self.player_guesses[name] = -1
 
game1 = Number_Guesser(["Thuy", "Joe", "Diya"])
```

Player guesses are added using the add_player_guess() method. This method takes in two pieces of information, the player’s name and their guess:

```py
def add_player_guess(self, name, guess)
```
It’s used like this:

```py
game1.add_player_guess("Diya", 8)
```
You’re still missing a few pieces:

Within your constructor, you need to use the random library to initialize a random integer between 1 and 10.
You need to write the add_player_guess() method. This method should check if the person is playing the game and add their guess to the dictionary. If the person is NOT playing, don’t add their guess to the dictionary. (If you look at the bottom of the code, you’ll see that Roger is trying to guess even though he’s not playing!)
If you Run your code, some code has already been written that will help you test your code. Try it!

```py
# Import random class
import random

class Number_Guesser:
  
  def __init__(self, player_names):
    self.player_guesses = {}

    # Adds names and -1 to player_guesses
    for name in player_names:
      self.player_guesses[name] = -1
      
    # Update to choose a random number
    self.secret_number = random.randint(1, 10)

  def add_player_guess(self, name, guess):
    # Fill in this method
    if name in self.player_guesses:
      self.player_guesses[name] = guess
    
  def print_answer(self):
    print(str(self.secret_number), "is the secret number!")
    
  def print_guesses(self):
    for player in self.player_guesses.items():
      if player[1] != -1:
        print(player[0], "guessed", str(player[1]))
      else:
        print(player[0], "needs to guess!") 

game1 = Number_Guesser(["Thuy", "Joe", "Diya"])
game1.add_player_guess("Roger", 10)
game1.add_player_guess("Diya", 8)
game1.add_player_guess("Thuy", 1)
game1.add_player_guess("Joe", 5)
game1.print_guesses()
game1.print_answer()
```

6. You’ve received a CSV of names, email addresses, and phone numbers, and you need to change it to a more person-readable format. The file is named employees.csv.

The file looks like:
```csv
Name,Email,Phone Number
Roger Smith,wigginsryan@yahoo.com,(555) 123-4567
Dan Meki,dmeki@hotmail.com,(555) 234-5678
```
...
Your task is to only take the Name and Phone Number fields and print out each line as:

Roger Smith: (555) 123-4567
You must:

Use the correct syntax for processing a CSV file.
Use a DictReader in your solution.
Print a line for every entry in the file!

```py
# Fill in your code below
import csv

with open('employees.csv', newline='') as employeesfile:
  reader = csv.DictReader(employeesfile)
  for row in reader:
    print(row['Name'] + ': ' + row['Phone Number'])
```