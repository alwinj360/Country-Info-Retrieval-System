Authors:    Alwin Joseph Kowattu (aka Alwin Alwin Joseph)
            Elyas Ehsan
            Vel Perez-Barba

Date: 15 May, 2023.

*********************************
The Project
*********************************
This project implements an information retrieval system using five different data structures:
    1) List
    2) Binary Search Tree Dictionary
    3) Linked List Dictionary
    4) Sorted List Dictionary
    5) Hash Table Dictionary

The "analyze.py" script compares the time efficiency of these five implementations on randomly generated files

The Binary Search Tree Dictionary (BSTDict) implementation was chosen to store and retrieve real world data in the file "dataFiles/country_data.csv". The BSTDict was chosen because it showed fast retrieval times when the number of queries were high (~10000).

Note: The List implementation was faster than BSTDict but we chose BSTDict because it offered a harder coding challenge.


**************************************************
How To Use the Interface (command line)
**************************************************
Run the file "mainBSTDict.py" using the command "python mainBSTDict.py" on the command line/Shell/Terminal.

This will start the program and additional instructions will be provided there.


**************************************************
The Real-World Data - "dataFiles/country_data.csv"
**************************************************
The provided data file "country_data.csv" includes a list of 20 countries and their development indicators like "Life Expectancy at Birth" and other data like "Population".
