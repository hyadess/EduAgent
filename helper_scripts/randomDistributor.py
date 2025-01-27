import random
import csv

def create_sets(numbers):
    # Group numbers by their remainders when divided by 4
    group_0 = [n for n in numbers if n % 4 == 0]
    group_1 = [n for n in numbers if n % 4 == 1]
    group_2 = [n for n in numbers if n % 4 == 2]
    group_3 = [n for n in numbers if n % 4 == 3]

    # Find the minimum size among the groups to determine the maximum possible sets
    num_sets = min(len(group_0), len(group_1), len(group_2), len(group_3))
    
    # Shuffle the groups to create random sets
    random.shuffle(group_0)
    random.shuffle(group_1)
    random.shuffle(group_2)
    random.shuffle(group_3)

    sets = []
    
    # Create sets with one element from each group
    for i in range(num_sets):
        sets.append([group_0[i], group_1[i], group_2[i], group_3[i]])

    return sets

def save_sets_to_csv(sets, filename):
    # Open the CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['set', 'first', 'second', 'third', 'forth'])
        
        # Write each set with its corresponding set number
        for idx, s in enumerate(sets, start=1):
            writer.writerow([f'{idx}'] + s)

# Example usage
numbers = list(range(0, 120))  # Replace with your list of numbers
sets = create_sets(numbers)

# Save the sets to a CSV file
save_sets_to_csv(sets, '../6_convo_htmls_prep/sets.csv')

print("Sets saved to 'sets.csv'.")
