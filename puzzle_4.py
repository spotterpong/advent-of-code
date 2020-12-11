import sys
import math
import re

def read_file(file_name):
	with open(file_name) as f:
		lines = f.readlines()
		return [line.strip() for line in lines]

def get_list_of_passports(data):
  passports = []
  working_passport = ""
  for row in data:
    if row == "":
      passports.append(working_passport.strip())
      working_passport = ""
    else:
      working_passport += row + " "
  if working_passport != "":
    passports.append(working_passport.strip())
  return passports

def get_valid_passport_count(passports):
  valid_count = 0
  valid_passports = []
  for passport in passports:
    valid_key_set = {
      "byr",
      "iyr",
      "eyr",
      "hgt",
      "hcl",
      "ecl",
      "pid",
      "cid"
    }
    key_set = { x.split(":")[0] for x in passport.split(" ")}
    key_diff = valid_key_set - key_set
    if len(key_diff) == 0 or (len(key_diff) == 1 and "cid" in key_diff):
      valid_passports.append({ x.split(":")[0]: x.split(":")[1] for x in passport.split(" ")})
      valid_count += 1
  return valid_count, valid_passports

def validate_passport(passport):
  if not re.match(r"^20[1]\d{1}$|^2020$", passport["iyr"]):
    return False
  if not re.match(r"^19[2-9]\d{1}$|^2001$|^2002$", passport["byr"]):
    return False
  if not re.match(r"^20[2-3]\d{1}$", passport["eyr"]):
    return False
  if not re.match(r"^1[5-8]\d{1}cm$|^19[0-3]cm$|^59in$|^6\d{1}in$|^7[0-6]in$", passport["hgt"]):
    return False
  if not (re.match(r"^#[0-9a-f]{6}$", passport["hcl"])):
    return False
  if not (re.match(r"amb|blu|brn|gry|grn|hzl|oth", passport["ecl"])):
    return False
  if not (re.match(r"^\d{9}$", passport["pid"])):
    return False
  return True

def validate_valid_passports(passports):
  valid_count = 0
  for passport in passports:
    if validate_passport(passport):
      valid_count += 1
  return valid_count


if __name__ == "__main__":
    data = read_file(sys.argv[1])
    passports = get_list_of_passports(data)
    valid_count, valid_passports = get_valid_passport_count(passports)
    print(f"Part 1 count: {valid_count}")
    valid_count_2 = validate_valid_passports(valid_passports)
    print(f"Part 2 count: {valid_count_2}")

