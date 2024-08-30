######################################   QUESTION 1   ########################################

# Let us say your expense for every month are listed below, January - 2200, February - 2350, March - 2600, April - 2130, May - 2190
#Create a list to store these monthly expenses and using that find out,

monthly_expense = {'January': 2200, 'February': 2350, 'March': 2600, 'April': 2130, 'May': 2190} 
print("Initial monthly expenses:", monthly_expense)

# 1. In Feb, how many dollars you spent extra compared to January?
feb_vs_jan = monthly_expense['February'] - monthly_expense['January']
print("1. Extra dollars spent in February compared to January:", feb_vs_jan)

# 2. Find out your total expense in the first quarter (first three months) of the year.
total_first_quarter = monthly_expense['January'] + monthly_expense['February'] + monthly_expense['March']
print("2. Total expense in the first quarter (Jan-Mar):", total_first_quarter)

# 3. Find out if you spent exactly 2000 dollars in any month.
for month, expense in monthly_expense.items():
    if expense == 2000:
        print("3. Yes, I spent exactly 2000 dollars in the month of", month)
print("3. No, I did not spend exactly 2000 dollars in any month.")

# 4. June month just finished, and your expense is 1980 dollars. Add this item to your monthly expense dictionary.
monthly_expense['June'] = 1980
print("4. Updated monthly expenses after adding June:", monthly_expense)

# 5. You returned an item that you bought in the month of April and got a refund of 200$. Make a correction to your monthly expense list based on this.
monthly_expense['April'] += 200
print("5. Updated monthly expenses after correcting April's expense:", monthly_expense)



######################################   QUESTION 2   ########################################

#You have a list of your favourite marvel super heros.

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
length_of_list = len(heros)
print("1. Length of the heros list:", length_of_list)

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print("2. Heros list after adding 'black panther':", heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print("3. Heros list after adding 'black panther' after 'hulk':", heros)

# 4. Now you don't like thor and hulk because they get angry easily :), So you want to remove them from the list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros[1:3] = ['doctor strange']
print("4. Heros list after replacing 'thor' and 'hulk' with 'doctor strange':", heros)

# 5. Sort the heros list in alphabetical order 
heros.sort()
print("5. Heros list sorted in alphabetical order:", heros)



######################################   QUESTION 3   ########################################

# 1. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
odd_numbers = []
max_number = int(input("Enter the maximum number: "))

for i in range(1, max_number+1):
    if i % 2 != 0:
        odd_numbers.append(i)

print("Odd numbers between 1 and", max_number, "are:", odd_numbers)