## 🐍 Hangman Game  

Hello!  

I am happy to share with you my first real project using Python. This is a simple Hangman game that I did for fun and to practice the basics of Python programming.  

While building it, I got to practice things like file handling, loops and conditionals, user input, string manipulation, and getting random choices from a set.  

# 🎮 How it Works  

The game picks a random id from a file called words.txt and pulls out all the letters.  
Also, it shows blanks (_) as placeholders while waiting for correct guesses to fill in the letters of the word.  

You can either guess the word all at once or letter by letter. When either option is selected, the game matches the guess against the various levels of difficulty and keeps a tally of failures.  

For each guess that doesn't match, a tally count on the upper left portion of the screen is incremented by 1.  

If the check mark key is pressed and the allowance runs out, the game will show you the options for winning either in the form of a give up button or going on till all allowed attempts are hit.  

# 🧠 Features  

The game implements a simple word list stored in words.txt that can easily be modified. Removing or changing the word list file is not constrained in any way which makes it easier for modifying the offered words or guessing words.  

Also, all guesses given do not care about case sensitivity which means uppercase letters do not change what is treated as a word or lower case letters (additional note).  

Repeating letters are also ignored and if on needs to change their mind about selection, they can be warned.

