import webbrowser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Hello World!")

# Line Plot #
xValues = [0, 1, 2, 3, 4, 5]
dataList = [3, 7, 5, 2, 9, 1]
plt.plot(xValues, dataList, label='Random Numbers')
plt.legend()  # Displays the legend
plt.show()   # Displays graph

# Scatter Plot #
# The scatter plot method requires x values as well as y values,
# So here, we're going to make another list with values 0-5
xValues = [1, 2, 3, 4, 5, 6]
dataList = [7, 8, 9, 10, 11, 12]
plt.scatter(xValues, dataList, label='Example')
plt.legend()
plt.show()

# Bar Plot #
# The bar plot method also requires x values
# So again, we're going to make a list with values 0-5 #
xValues = [5, 7, 10, 20, 21, 30]
dataList = [7, 8, 12, 15, 16, 20]
plt.bar(xValues, dataList, label='Bar Plot')
plt.legend()
plt.show()

# Here, we're writing a function that will display a line plot #


# def lineplot(xCoords, line1, line2, xLabels, lineLabels, title):
#     # Treat this like a fill in the blanks sheet!
#     # Variables like size, width, and range are totally up to you
#     # Some blanks require figuring out which parameters go where, so careful

#     # Plotting #
#     plt.ylim(0, 100)  # Defines range of y values
#     plt.plot(xCoords, line1, label=line2[0], linewidth=8, color='red')
#     plt.plot(xCoords, line2, label=line1[1], linewidth=8, color='green')

#     # Display Labels and Legend #
#     # Labels each x value
#     plt.xticks(ticks=xCoords, labels=xLabels, fontsize=13)
#     # Labels each y value
#     plt.yticks(fontsize=13)
#     # Displays title
#     plt.title(title, fontsize=13)
#     plt.grid(True, axis='y', linestyle=':',
#              linewidth='3', color='blue')  # Adds a grid
#     # Displays legend
#     plt.legend(fontsize=13, bbox_to_anchor=[0, 13])
#     # Saves graph to local computer using title
#     plt.savefig(title)
#     plt.show()

# # Generating Data #
# # This graph is a simulation of someone's personal finances


# # The list(range()) functions will put every integer
# xVals = list(range(0, 9))
# # between the lowerbound and the upperbound into a list
# # Generates random numbers for money spent
# spending = np.random.randint(low=0, high=9, size=(9))
# # Random numbers for money saved
# saving = np.random.randint(low=0, high=9, size=(9))

# # Labels x axis with months
# xMonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Calling the function #
# lineplot(xVals, spending, saving, xMonths, ['Spending', 'Saving'], 'Money')

# Word Spliting

phrase = "Do or do not, there is no try"
for letter in phrase:
    print(letter)

    words = phrase.split()

# We can print all words individually, like this:
for word in words:
    print(word)

# Or we can use this instead, depending on the format that you need
print(words)

data = "From john.doe@math.uic.edu Fri July 6 10:00:01 2021"
find_at = data.find('@')

print(find_at)

space_after_at = data.find(' ', find_at)
print(space_after_at)

# This is a simple option but doesn't work if you have to
# iterate through many of these messages
host_option1 = data[14: 26]
print(host_option1)

# Better option that's scalable
host = data[find_at + 1: space_after_at]
print(host)

# Exercise

# Test your understanding and try using what you just learned to extract some inormation from this url https://kaggle.com/c/mlb-player-digital-engagement-forecasting (site name being "Kaggle"):

# How many characters are there in the url?
# What is the 15th character in the url (when counted by a human)?
# Get the 14th through 17th character
# Create a new variable called url2 where all the characters are upper case.
# Automate code that would extract the site name for all urls that are in this format (the site name is "Kaggle")
url = "https://kaggle.com/c/mlb-player-digital-engagement-forecasting"
# Question 1
# How many characters are there in the url?
print(len(url))

# Question 2
# What is the 15th character in the url (when counted by a human)?
# "."

# Question 3
# Get the 14th through 17th character
between = url[14:17]

# Question 4
# Create a new variable called url2 where all the characters are upper case.

url2 = url.upper()
print(url2)

# Question 5
# Automate code that would extract the site name for all urls that are in this format (the site name is "Kaggle")
Automate = url[0:18]
print(Automate)

# Goes to webstie that I parsed
# webbrowser is imported above
webbrowser.open(Automate)
