import string


def split_compartments(puzzle_input):
    puzzle_input = puzzle_input.strip()
    if len(puzzle_input) % 2 != 0:
        raise Exception(f"Invalid puzzle input. String must be divisible by 2. \nInput: {puzzle_input}")
    return [puzzle_input[:len(puzzle_input) // 2], puzzle_input[len(puzzle_input) // 2:]]


def find_common_items(compartments):
    local_common_items = []
    for item in compartments[0]:
        if item not in local_common_items and item in compartments[1]:
            local_common_items.append(item)
    return local_common_items


def get_priority(common_item):
    item_priority = 0
    if common_item.islower():
        item_priority += int(string.ascii_lowercase.index(common_item)) + 1
    elif common_item.isupper():
        item_priority += int(string.ascii_uppercase.index(common_item)) + 27
    else:
        raise Exception(f"invalid input {common_item}. must provide string.")
    return item_priority


def tally_priorities(items):
    combined_priorities = 0
    for item in items:
        combined_priorities += get_priority(item)
    return combined_priorities


rucksacks = [split_compartments(line) for line in open('./input.txt')]

common_items = []
for rucksack in rucksacks:
    common_items += find_common_items(rucksack)

print("Item priorities total at:" + str(tally_priorities(common_items)))


def bag_to_set(comparts):
    combined = str(comparts[0]) + str(comparts[1])
    # Split string into list using unpack
    return set([*combined])


def get_badges(bags, bag_numbers):
    bag_one = bag_to_set(bags[bag_numbers[0]])
    bag_two = bag_to_set(bags[bag_numbers[1]])
    bag_three = bag_to_set(bags[bag_numbers[2]])

    b1b2 = bag_one.intersection(bag_two)
    b1b2b3 = b1b2.intersection(bag_three)
    if len(b1b2b3) > 1:
        raise Exception(f'Error: More than one common item found in bags {bag_numbers}.')
    else:
        b1b2b3 = ''.join(b1b2b3)
    return b1b2b3


bag_number = 0
indices = []
badges = []
while bag_number < len(rucksacks):
    if (bag_number + 1) % 3 == 0:
        indices.append(bag_number)
        badges.append(get_badges(rucksacks, indices))
        indices.clear()
    else:
        indices.append(bag_number)
    bag_number += 1

badge_priority = tally_priorities(badges)
print(f"{len(badges)} badges found. Total badge priority {badge_priority}")
