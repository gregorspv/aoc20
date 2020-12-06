# part 1
import re

with open("day2.txt") as df:
    passwords = df.read().splitlines()

valid_counter = 0

pattern = re.compile(r"""(?P<start>.*)
                             -(?P<end>.*)\s
                             (?P<letter>.*):\s
                             (?P<entry>.*)""", re.X)

parsed_passwords = []

for password in passwords:
    match = pattern.match(password)

    elements = {}
    elements["start"] = int(match.group("start"))
    elements["end"] = int(match.group("end"))
    elements["letter"] = match.group("letter")
    elements["entry"] = match.group("entry")

    parsed_passwords.append(elements)

for password in parsed_passwords:
    letter_counter = 0
    for character in password["entry"]:
        if character == password["letter"]:
            letter_counter += 1

    if password["start"] <= letter_counter <= password["end"]:
        valid_counter += 1

print(f"The number of valid passwords is {str(valid_counter)}")

# part 2
valid_counter = 0

for password in parsed_passwords:
    if (password["entry"][password["start"]-1] == password["letter"] and password["entry"][password["end"]-1] != password["letter"]) or (password["entry"][password["start"]-1] != password["letter"] and password["entry"][password["end"]-1] == password["letter"]):
        valid_counter += 1

print(f"The number of valid passwords is {str(valid_counter)}")
