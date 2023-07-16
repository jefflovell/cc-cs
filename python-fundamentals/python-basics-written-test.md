1. Fill in the blanks to declare, initialize, and use Python variables using the correct syntax.

int_variable = 5
string_variable = "codecademy"
boolean_variable = `True`
# prints "I have taken 5 codecademy courses."
print("I have taken " + `str(int_variable)` + " " + `string_variable` + " courses.")

`int_variable`
`"True"`
`string_variable`
`True`
`str(int_variable)`
`int(string_variable)`

2. Fill in the blanks to properly complete these conditional statements.

cat_breed = "Calico"
 
`if` `cat_breed == "Calico"`:
    print("That cat is a Calico!")
`elif` `cat_breed == "Tabby"`:
    print("That cat is a Tabby!")
`else`:
    print("What a beautiful cat!")

`else if`
`if`
`cat_breed == "Tabby"`
`cat_breed == "Calico"`
`else`
`elif`

Click or drag and drop to fill in the blank

3. What type of Python error is shown in the message?

```py
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    piggy_bank = '2' + 0.25
 `TypeError` Error: must be str, not float
```

`TypeError` <=
`NameError`
`SyntaxError`

4. What is the output of this code attempting to access a 2D array?

```py
grades = [["Jenny", 89], ["Roberto", 98], ["Shruti", 75], ["Juliette", 78], ["Vik", 83]]
print(grades[-1][1])

```
`IndexError`
`83` <=
`"Jenny"`
`"Vik"`
`89`

5. Which of the following snippets of Python code will correctly print out only even numbers between 1 and 10, inclusive?

(Remember, even numbers are numbers that are divisible by 2.)

```py
for num in range(2,10,2):
    print(num)
```
```py
for even in range(2, 10):
    print(even)
```
```py
for num in range(2,11,2):
    print(num)
### My Answer
```
```py
for num in range(2, 11):
    if num % 2 == 1:
        print(num)
```

6. Fill in the blanks to complete this Python code snippet so that the code does NOT result in an infinite loop.

counter = 0

`while` True:
  counter += 1
  if counter == 5:
    `break`        

print("Our code exited the loop!")

`continue`
`while`
`if`
`for`
`pass`
`break`

Click or drag and drop to fill in the blank

7. Fill in the blanks to complete this code that creates a multiple choice question!

Focus on what you think the correct parameters and arguments should be for this function.

`def` create_multiple_choice_question(prompt, options, `correct_answer`):
  print(prompt)

  for option_num in range(len(options)):
      print(str(option_num) + ": " + options[option_num])

  player_answer = input("Which option is correct? ")

  if int(player_answer) == correct_answer:
      print("Great job!")
  else:
      print("Not quite!")

first_prompt = "Which one is a dog?"
first_options = ["Tabby", "Poodle", "Spaghetti", "Parakeet"]
first_answer = 1
create_multiple_choice_question(`first_prompt, first_options`, first_answer)

`correct_answer`
`function`
`first_prompt, first_options`
`prompt, options`
`first_options`
`def`
`first_prompt`

Click or drag and drop to fill in the blank

8. Fill in the blanks based on the context clues in the terminal. You are navigating to the python_programs directory to run the hello_world.py program.

$ cd Documents

$ ls
text_files  python_programs

$ `cd hello_world.py`

$ pwd
User/ccuser/Documents/python_programs

$ `ls`
hello_world.py

$ `python hello_world.py`
Hello, world!

`ls`
`python hello_world.py`
`cat`
`cd hello_world.py`
`cd python_programs`
`python python_programs`

Click or drag and drop to fill in the blank

9. Select the option that shows the correct way to commit the file hello_world.py to a GitHub repo.

```bash
$ git add hello_world.py
$ git status
On branch master
nothing to commit, working tree clean
$ git commit -m "Committing hello world."
```
```bash
$ git add hello_world.py
$ git commit -m "Committing hello world."
$ git status
On branch master
nothing to commit, working tree clean
### My Answer
```
```bash
$ git commit -m "Committing hello world."
$ git status
On branch master
nothing to commit, working tree clean
$ git add hello_world.py
```
```bash
$ git commit -m "Committing hello world."
$ git add hello_world.py
$ git status
On branch master
nothing to commit, working tree clean
```

10. Fill in the blanks to print the specified words.

`sentence = "I love programming!"`

Should print "I"`
print(`sentence[0]`)

Should print "love"
print(`sentence[2:6]`)

Should print "programming!"
print(`sentence[7:]`)

`sentence[1]`
`sentence[:7]`
`sentence[7:]`
`sentence[2:6]`
`sentence[0]`
`sentence[2:5]`

Click or drag and drop to fill in the blank

11. Which of these attempts to import the randint method from the random Python module will result in an error?
```py
import random as r
```
```py
import randint
### This one
```
```py
import random
```
```py
from random import randint
```

12. What does the code snippet print out?

```py
fridge_contents = {"egg":12, "milk": 2, "apple": 6, "celery": 5}

for variable1, variable2 in fridge_contents.items():
    if variable1 in fridge_contents:
        print(fridge_contents[variable1])
    if variable2 in fridge_contents:
        print(fridge_contents[variable2])
```

```py
egg
12
milk
2
apple
6
celery
5
```
```
No output
```
```py
"egg"
"milk"
"apple"
"celery"
```
```py
12
2
6
5
### This one
```

13. Fill in the blanks to create and write to this file in Python.

with `open` ('programming_languages.txt', `'w'`) as programming_languages_doc:

  programming_languages_doc.`write`('Python')

`'a'`
`''`
`write`
`'w'`
`read`
`write`
`open`

Click or drag and drop to fill in the blank

14. Which keyword is used to represent an instance of a class in Python?

`super()`
`def`
`constructor`
`self` <=