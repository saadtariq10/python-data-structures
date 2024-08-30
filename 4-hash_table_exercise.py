# Exercise: Hash Table


#############################   QUESTION 1   ###############################
# What was the average temperature in first week of Jan
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# 1. What was the average temperature in first week of Jan
# 2. What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

import csv

# Read the data from the CSV file
with open('nyc_weather.csv', 'r') as file:
    reader = csv.DictReader(file)
    weather_data = {row['date']: int(row['temperature']) for row in reader}

# Calculate average temperature for the first week (Jan 1 - Jan 7)
first_week_temps = [weather_data[f'2023-01-0{i}'] for i in range(1, 8)]
avg_temp_first_week = sum(first_week_temps) / len(first_week_temps)

# Find the maximum temperature in the first 10 days (Jan 1 - Jan 10)
first_ten_days_temps = [weather_data[f'2023-01-0{i}'] for i in range(1, 11)]
max_temp_first_ten_days = max(first_ten_days_temps)

print(f"Average temperature in the first week: {avg_temp_first_week}")
print(f"Maximum temperature in the first 10 days: {max_temp_first_ten_days}")


#############################   QUESTION 2   ###############################
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# 1. What was the temperature on Jan 9?
# 2. What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

# Find temperatures on specific dates
temp_jan_9 = weather_data.get('2023-01-09')
temp_jan_4 = weather_data.get('2023-01-04')

print(f"Temperature on Jan 9: {temp_jan_9}")
print(f"Temperature on Jan 4: {temp_jan_4}")


#############################   QUESTION 3   ###############################
# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8

from collections import defaultdict

# Read the poem and count word occurrences
word_count = defaultdict(int)

with open('poem.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            cleaned_word = word.strip().strip('.,;:!?"').lower()
            word_count[cleaned_word] += 1

# Print word counts
for word, count in word_count.items():
    print(f"'{word}': {count},")


#############################   QUESTION 4   ###############################
# Implement hash table where collisions are handled using linear probing. 
# We learnt about linear probing in the video tutorial. 
# Take the hash table implementation that uses chaining and modify methods to use linear probing. 
# Keep MAX size of arr in hashtable as 10.

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, index):
        # Linear probing: find the next available slot
        start_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("HashTable is full!")
        return index

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is not None:
            index = self._probe(index)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return None

    def __str__(self):
        return str([item for item in self.table if item is not None])

# Example usage
ht = HashTable()

# Insert data
ht.insert("Jan 1", 6)
ht.insert("Jan 2", 7)
ht.insert("Jan 3", 9)
ht.insert("Jan 4", 11)
ht.insert("Jan 5", 12)
ht.insert("Jan 6", 13)
ht.insert("Jan 7", 10)
ht.insert("Jan 8", 9)
ht.insert("Jan 9", 12)
ht.insert("Jan 10", 8)

# Retrieve data
print(f"Temperature on Jan 9: {ht.get('Jan 9')}")
print(f"Temperature on Jan 4: {ht.get('Jan 4')}")

# Print the hash table
print(ht)

