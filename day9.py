# part 1

with open("day9.txt") as df:
    numbers = df.read().splitlines()

# initialise preamble
preamble = numbers[0:25]

# iterate over remaining numbers
for i in range(25,len(numbers)):

    # check if the number is a sum of either two in the preamble
    for e in preamble:
        if str(int(numbers[i]) - int(e)) in preamble: # is a sum
            break
    else: # if it doesn't break, it is not a sum
        print(f"The first number that does not have the property is {numbers[i]}")
        break

    # update preamble
    preamble.pop(0)
    preamble.append(numbers[i])

# part 2

desired_number = numbers[i]
contiguous_sequence = []

for beginning_index in range(len(numbers)):
    partial_sum = int(numbers[beginning_index])

    for ending_index in range(beginning_index+1, len(numbers)):
        partial_sum += int(numbers[ending_index])

        if partial_sum == int(desired_number): # match
            contiguous_sequence = numbers[beginning_index:ending_index]
            print(f"The weakness is {str(min(map(int,contiguous_sequence)) + max(map(int,contiguous_sequence)))}")
            break
        elif partial_sum > int(desired_number): # overshoot
            break # break inner loop / take new beginning_index
        # elif < : continue increasing ending_index

    if contiguous_sequence != []: # do not break out of outer loop in case of elif
        break
