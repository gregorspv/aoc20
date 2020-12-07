# part 1

with open("day7.txt") as df:
    rules = df.read().splitlines()

bags = {}

for rule in rules:
    rule = rule.split()
    # all colours are two-word names
    container = " ".join(rule[0:2])
    contains = []
    if len(rule) != 7: # if not "contains no bags"
        for e in range(int((len(rule) - 4) / 4)):
            number = int(rule[4 + 4 * e])
            colour = " ".join(rule[5 + 4 * e: 7 + 4 * e])

            contains.append((number, colour))
    else:
        contains.append((0, ""))

    bags[container] = contains

containers = []

while True:
    added_in_cycle = 0

    for bag in bags:
        for contains in bags[bag]:
            if contains[1] == "shiny gold" or contains[1] in containers:
                if bag not in containers: # do not duplicate
                    containers.append(bag)
                    added_in_cycle += 1

    if added_in_cycle == 0: # once no new ones are added
        break

print(f"The number of possible containers is {str(len(containers))}")

# part 2
def count_contain(bag):
    counter = 0
    for cont in bags[bag]:
        #print(bag, cont)
        if cont[0] != 0:
            counter += cont[0] + cont[0]*count_contain(cont[1]) #it took strangely long to sort this multiplication out!
    return counter


no_of_bags = 0

for cont in bags["shiny gold"]:
    no_of_bags += cont[0]
    no_of_bags += cont[0]*count_contain(cont[1])

print(f"The total number of bags is {str(no_of_bags)}")
