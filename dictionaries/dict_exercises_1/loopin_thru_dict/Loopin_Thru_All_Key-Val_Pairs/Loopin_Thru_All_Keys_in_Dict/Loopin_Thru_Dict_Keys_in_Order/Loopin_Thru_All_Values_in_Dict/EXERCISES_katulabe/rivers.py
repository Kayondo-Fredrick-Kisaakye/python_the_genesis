# Make a dictionary containing three major rivers and the country
# each river runs through . One key-value pair might be 'nile': 'egypt' .
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt .
# Use a loop to print the name of each river included in the dictionary .
# Use a loop to print the name of each country included in the dictionary

the_dict = {
    'river nile':'jinja',
    'river katonga':'masaka',
    'river kyoga':'kayunga',
    'river fredrick':'dyk nation',
}

for river, country in the_dict.items():
    print("River: " + river)
    print("Country: " + country)

for river, country in the_dict.items():
    print(river + " flows through " + country)