"""
ITSC 1212 Project 4

"""


# --------------------------------------------------
# PROVIDED FUNCTION (DO NOT MODIFY)
# --------------------------------------------------
def load_coromon_data(filename: str) -> list:
    """
    Reads Coromon data from a CSV file and returns it as a nested list.
    Each inner list represents one Coromon.
    """
    data = []

    file = open(filename, 'r')

    # Skip header row
    file.readline()

    for line in file:
        values = line.strip().split(',')

        # Convert numeric values to integers (indices 2 -> end)
        for i in range(2, len(values)):
            values[i] = int(values[i])

        data.append(values)

    file.close()

    return data


# --------------------------------------------------
# QUICK EXPLORATION
# Uncomment the following lines to see what a single Coromon entry looks like
# --------------------------------------------------
'''
coromon_data = load_coromon_data("Coromon_Dataset.txt")

print(coromon_data[0])          # inspect the first Coromon entry
print(type(coromon_data[0]))   # confirm the type of each element (should be a list)

print(coromon_data[20])        # inspect another Coromon entry (21st)

print(len(coromon_data))       # determine the total number of entries in the dataset

'''

# --------------------------------------------------
# ADD YOUR CODE BELOW THIS LINE
# --------------------------------------------------
import random


def display_random_coromon(coromon_data):
    random_index = random.randint(0, len(coromon_data) - 1)
    coromon = coromon_data[random_index]

    # Pull each individual value out of the inner list
    name, c_type, hp, atk, sp_atk, defense, sp_def, speed, stamina = coromon

    print("Randomly selected Coromon:")
    print("Name:", name)
    print("Type:", c_type)
    print("Health Points:", hp)
    print("Attack:", atk)
    print("Special Attack:", sp_atk)
    print("Defense:", defense)
    print("Special Defense:", sp_def)
    print("Speed:", speed)
    print("Stamina Points:", stamina)


def organize_by_type(coromon_data):
    """
    Organizes Coromon data by type using lists (no dictionaries).

    Returns multiple parallel lists that store:
    - unique types
    - counts per type
    - totals per attribute per type
    """
    types = []
    counts = []
    totals = []

    for coromon in coromon_data:
        c_type = coromon[1]

        # Grab the 6 numeric attributes (indices 2 through 7: HP up to Speed)
        stats = [
            coromon[2],
            coromon[3],
            coromon[4],
            coromon[5],
            coromon[6],
            coromon[7],
        ]

        # If this is a new type, add it to all three parallel lists
        if c_type not in types:
            types.append(c_type)
            counts.append(1)
            totals.append(stats)

        # If this type already exists, find its position and add to its count and totals
        else:
            idx = types.index(c_type)
            counts[idx] = counts[idx] + 1

            for i in range(6):
                totals[idx][i] = totals[idx][i] + stats[i]

    return (types, counts, totals)


def compute_type_averages(types, counts, totals):
    """
    Computes average stats for each type and returns
    a nested list of averages.
    """
    averages = []

    for i in range(len(types)):
        type_avg = []
        for j in range(6):
            avg_value = totals[i][j] / counts[i]
            type_avg.append(avg_value)
        averages.append(type_avg)

    return averages


def find_max_average(types, averages, attribute_index):
    """
    Returns a list of type name(s) with the highest average
    for the given attribute index.
    """
    highest_val = averages[0][attribute_index]
    best_types = []

    # First pass: find the highest average value
    for i in range(len(averages)):
        if averages[i][attribute_index] > highest_val:
            highest_val = averages[i][attribute_index]

    # Second pass: collect all types that match that highest value (handles ties)
    for i in range(len(averages)):
        if averages[i][attribute_index] == highest_val:
            best_types.append(types[i])

    return best_types


def find_min_average(types, averages, attribute_index):
    """
    Returns a list of type name(s) with the lowest average
    for the given attribute index.
    """
    lowest_val = averages[0][attribute_index]
    lowest_types = []

    # First pass: find the lowest average value
    for i in range(len(averages)):
        if averages[i][attribute_index] < lowest_val:
            lowest_val = averages[i][attribute_index]

    # Second pass: collect all types that match that lowest value (handles ties)
    for i in range(len(averages)):
        if averages[i][attribute_index] == lowest_val:
            lowest_types.append(types[i])

    return lowest_types


def display_summary_results(types, averages):
    """Displays the highest and lowest average types for all 6 attributes."""
    attributes = [
        "Health Points",
        "Attack",
        "Special Attack",
        "Defense",
        "Special Defense",
        "Speed",
    ]

    for attr_idx in range(len(attributes)):
        max_types = find_max_average(types, averages, attr_idx)
        min_types = find_min_average(types, averages, attr_idx)

        # Print highest average type(s) cleanly without brackets
        print("Highest average " + attributes[attr_idx] + ": ", end="")
        for i in range(len(max_types)):
            if i == len(max_types) - 1:
                print(max_types[i])
            else:
                print(max_types[i], end=", ")

        # Print lowest average type(s) cleanly without brackets
        print("Lowest average " + attributes[attr_idx] + ": ", end="")
        for i in range(len(min_types)):
            if i == len(min_types) - 1:
                print(min_types[i])
            else:
                print(min_types[i], end=", ")

        print()


def main():
    # Load the dataset using the provided function
    coromon_data = load_coromon_data("Coromon_Dataset.txt")

    # --------------------------------------------------
    # PART A: Basic Dataset Information
    # --------------------------------------------------
    print("Total number of Coromon:", len(coromon_data))
    print()

    display_random_coromon(coromon_data)
    print()

    # --------------------------------------------------
    # PART B: Organize Data by Type
    # --------------------------------------------------
    types, counts, totals = organize_by_type(coromon_data)

    print("Distinct Coromon Types:")
    for i in range(len(types)):
        if i == len(types) - 1:
            print(types[i])
        else:
            print(types[i], end=", ")
    print()

    # --------------------------------------------------
    # PART C: Compute Averages & Display Highest/Lowest
    # --------------------------------------------------
    averages = compute_type_averages(types, counts, totals)
    display_summary_results(types, averages)


if __name__ == "__main__":
    main()
