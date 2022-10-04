#! /bin/bash

echo "Would you like to play a game of rock, paper scissors? y/n"
read selection
if [ $selection == 'y' ]
then
    python3 rps.py
else
    echo "That is disappointing."
fi