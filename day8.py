# part 1

with open("day8.txt") as df:
    instructions = df.read().splitlines()

acc = 0
ran_instructions = []
position = 0

def execute(line):
    global acc
    global position

    if line.split()[0] == "nop":
        position += 1
    elif line.split()[0] == "acc":
        acc += int(line.split()[1])
        position +=1
    elif line.split()[0] == "jmp":
        position += int(line.split()[1])

while position not in ran_instructions:
    ran_instructions.append(position)
    execute(instructions[position])

print(f"Before looping, the acc value was {str(acc)}")

# part 2

for e in range(len(instructions)): # try changing every instruction and check if it halts
    if instructions[e].split()[0] == "nop" or instructions[e].split()[0] == "jmp":

        # try changing instruction
        if instructions[e].split()[0] == "nop":
            instructions[e] = " ".join(["jmp", instructions[e].split()[1]])
        elif instructions[e].split()[0] == "jmp":
            instructions[e] = " ".join(["nop", instructions[e].split()[1]])

        acc = 0
        ran_instructions = []
        position = 0

        while position not in ran_instructions:
            ran_instructions.append(position)
            execute(instructions[position])
            if position == len(instructions): # corresponds to wanting to execute instruction after EOF
                break
        else: #looped
            if instructions[e].split()[0] == "nop":
                instructions[e] = " ".join(["jmp", instructions[e].split()[1]])
            elif instructions[e].split()[0] == "jmp":
                instructions[e] = " ".join(["nop", instructions[e].split()[1]])
            continue

        # if while breaks
        break

print(f"If the program halted, the value of acc before halting was {str(acc)}")