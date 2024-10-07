# python-challenge

## Overview
This repository contains two Python scripts designed to analyze financial and election data. The two tasks, **PyBank** and **PyPoll**, represent real world scenarios of data analysis.

## Features

### PyBank
The PyBank script analyzes company financial records from a CSV file containing "Date" and "Profit/Losses" columns. The script calculates:
- Total number of months in the dataset.
- Net total amount of "Profit/Losses".
- Changes in "Profit/Losses" between months, and their average.
- Greatest increase in profits (date and amount).
- Greatest decrease in profits (date and amount).

The budget analysis is printed in the terminal and exported to a text file.

### PyPoll
The PyPoll script analyzes election voting data from a CSV file containing "Voter ID", "County", and "Candidate" columns. The script calculates:
- Total number of votes cast.
- Complete list of candidates who received votes.
- Percentage and total number of votes each candidate received.
- The winner of the election based on popular vote.

The election results are printed in the terminal and exported to a text file.