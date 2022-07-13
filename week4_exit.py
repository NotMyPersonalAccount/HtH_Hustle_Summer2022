"""" EXIT TICKET """
# Rename this file here & call it week4_exit.py

## Part I: Create a dictionary

# Create your food table here via key:value pairs
# (input the food & prices from lines 73-76):
food_prices = {
  "chicken": 1.56,
  "beef": 1.59,
  "cheese": 1.25,
  "milk": 1.20
}
print(food_prices)

# Retrieve any value from the food prices dictionary by using its corresponding key along with the bracket notation
# For example, to get the price for cheese, run this:
milk_price = food_prices["milk"]
print(milk_price)

# Access the prices for each item & store into their own variable, just like the milk example.  
chicken_price = food_prices["chicken"]
beef_price = food_prices["beef"]
cheese_price = food_prices["cheese"]

# Print those variables to check that you get the right value. Write the code to print on the line below:
print(chicken_price, beef_price, cheese_price)

## Part II. Create a list of the Spotify playlist

# First, add the songs in your section's list in 
playlist = [
  "Iniko - The King’s Affirmation",
  "FKJ - Ylang Ylang",
  "grentperez - Cherry Wine",
  "Cafune - Tek It"
]

# Print the playlist in the line below:
print(playlist)

# Lists have an index, which is a number assigned to each item in the list based on the oder in which they appear in the list, starting at 0. 
# What's the first song on your list?
print(playlist[0])

# Pick your top 2 favorite songs from the list & print them using the list's index to access them
fave_songs = playlist[1:2]
print(fave_songs)

# Update your playlist by changing the last song to something else
playlist[2] = "Kate Bush - Running Up That Hill"
# print the playlist to show that you have updated it
print(playlist)

# Add another song to the end of the list using append()
playlist.append("Journey - Separate Ways")
# print the playlist to show that you added a new song
print(playlist)

# You changed your mind & want to delete the last song you just added
playlist.pop()
# Print the playlist to show that you deleted the last song
print(playlist)

# How many songs are in your list? Use len()
print(len(playlist))
# Write here how many songs are in your playlist = 

# Sort your playlist in alphabetical order using sorted()
playlist = sorted(playlist)
# Write here the order of the songs in your playlist:
print(playlist)
