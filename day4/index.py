states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma"]
number_of_states = len(states_of_america)#50 -> 49
print(states_of_america[number_of_states - 2])


dirty_dozen = ["rotten", "moldy", "stinky", "smelly", "spoiled", "rancid", "putrid", "foul", "rank", "decayed", "decomposed", "infested"]
fruits = ["apple", "banana", "pear", "peach"]
vegetables = ["carrot", "broccoli", "asparagus", "cauliflower"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][0])

#indexing a list inside a list
#it can be used to create a 2D array, which is a list of lists. Each inner list can represent a row, and the elements within each inner list can represent columns. 
#This allows for more complex data structures and can be useful for representing grids, matrices, or tables.