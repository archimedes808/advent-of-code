with open('./input.txt', 'r') as f:
    raw_input = f.readlines()

fully_contained = 0
overlaps = 0
for line in raw_input:
    ranges = line.strip().split(',')
    set1 = set(range(int(ranges[0].split('-')[0]), int(ranges[0].split('-')[1]) + 1))
    set2 = set(range(int(ranges[1].split('-')[0]), int(ranges[1].split('-')[1]) + 1))
    if set1.intersection(set2):
        overlaps += 1
    if len(set1.intersection(set2)) == len(set1) or len(set1.intersection(set2)) == len(set2):
        fully_contained += 1

print(f"Assignments fully contained by other assignments: {fully_contained}")
print(f"Assignments with any overlap: {overlaps}")
