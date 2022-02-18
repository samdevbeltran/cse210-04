# Greed
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 __main__.py 
```
## Project Structure
---
The project files and folders are organized as follows:
```
root                    
  +-- game
    +--character
        +--position.py          (calculates a position)
        +--character.py         (creates a character) 
    +--states
        +--physics.py           (Generates the physics of the game)
        +--collision.py         (Detects if there is a collision)
    +--gameControl
        +--director.py          (Controls every part of the game)
    +--services
        +--keyboard.py          (Reads players input)
        +--display.py           (Rendering of the game)
    +--gameLogic
        +--score.py             (Calculates the score)
+-- __main__.py                 (entry point for program)
+-- README.md                   (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
git:https://github.com/samdevbeltran/cse210-04
Samuel Beltran (samuelbeltran@byui.edu)
Vadym Chemariev (che21025@byui.edu)
Karrass Phiri (phi21020@byui.edu)
Yamileth Rivero (riv21019@byui.edu)