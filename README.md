# Conway's Game of Life 

Have some fun with a terminal version of Conway's Game of Life. 

Best thing about this version: it's live (you can actually see the game's progress).

# Requirements

Make sure you have Python 3 installed on your machine.

The following Python libraries are also required: 

* random, time (should be available out-of-the-box)
* curses (to format output text)
* shutil (so the game adapts to the size of your terminal)

# How to run

Simply run the following command, which runs the only script in this repository:

```
python3 conway.py
```

# How does it work? 

Mechanics of the game is explained here: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life.

This version assumes a toroid (donut-shaped) structure on the field.
Initial generation is a random placement of live cells in the field.

