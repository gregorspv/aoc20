# part 1

with open("day1.txt") as df:
    expenses = list(map(int,df.read().splitlines()))

for a in range(len(expenses)):
    for b in range(1+a, len(expenses)):
        if expenses[a] + expenses[b] == 2020:
            print(f"The product of {str(expenses[a])} and {str(expenses[b])} is {str(expenses[a]*expenses[b])}.")
            break
    else:
        continue
    break

# part 2

for a in range(len(expenses)):
    for b in range(1+a, len(expenses)):
        for c in range(1 + b, len(expenses)):
            if expenses[a] + expenses[b] + expenses[c]== 2020:
                print(f"The product of {str(expenses[a])}, {str(expenses[b])}, and {str(expenses[c])} is "
                      f"{str(expenses[a]*expenses[b]*expenses[c])}.")
                break
        else:
            continue
        break
    else:
        continue
    break