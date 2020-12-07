# part 1
import re
import string

with open("day4.txt") as df:
    file = df.read().splitlines()

valid = 0

passports = []
current_passport = {}

for line in range(len(file)):
    if file[line] == "": # end of passport
        passports.append(current_passport)
        current_passport = {}
    else:
        line = file[line].split()
        for entry in line:
            entry = entry.split(":")
            current_passport[entry[0]] = entry[1]

for passport in passports:
    if len(passport) == 8:
        valid += 1
    elif len(passport) == 7 and "cid" not in passport:
        valid += 1

print(f"The number of “valid” passports is {str(valid)}")

# part 2
valid = 0

for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        if passport["hgt"][-2:] and passport["hgt"][0:-2]:
            height_units = passport["hgt"][-2:]
            height = int(passport["hgt"][0:-2])

            if passport["hcl"][0] == "#" and set(passport["hcl"][1:0]) <= set(string.hexdigits):
                if (1920<=int(passport["byr"])<=2002) and (2010<=int(passport["iyr"])<=2020) and (2020<=int(passport["eyr"])<=2030) and ((height_units=="cm" and 150<=height<=193) or (height_units=="in" and 59<=height<=76)) and (passport["ecl"] == "amb" or passport["ecl"] == "blu" or passport["ecl"] == "brn" or passport["ecl"] == "gry" or passport["ecl"] == "grn" or passport["ecl"] == "hzl" or passport["ecl"] == "oth") and (len(passport["pid"]) == 9) and (set(passport["pid"]) <= set(string.digits)):
                    valid += 1

print(f"The number of valid passports is {str(valid)}")