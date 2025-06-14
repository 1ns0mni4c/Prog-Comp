data = """6
5 9 9 12 3 6
2 2 6 3 12 7
10 11 1 1 11 10
8 4 4 8 7 5""" #Input data goes here

def parse_data(data):
    lines = data.strip().split("\n")
    numbers = []

    for line in lines[1:]:
        numbers.extend([int(x) for x in line.split()])
    
    return numbers

numbers = parse_data(data)

while True:
    changed = False
    last_number = numbers[0]

    for current_number in numbers[1:]:
        if current_number == last_number:
            numbers.remove(last_number)
            numbers.remove(last_number)
            changed = True
            break
        else:
            last_number = current_number

    if len(numbers) == 0:
        print("YES")
        break
    if not changed:
        print("NO")
        break