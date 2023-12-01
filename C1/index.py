def exportDigits(string: str) -> int:
  number = ''
  for char in string:
    if char.isdigit(): number += char; break
  for char in string[::-1]:
    if char.isdigit(): number += char; break
  return int(number)

with open('input.txt', 'r') as file:
  lines = file.readlines()
  result = 0
  for line in lines:
    twoDogits = exportDigits(line)
    result += twoDogits
    print(twoDogits)
  print(result)
