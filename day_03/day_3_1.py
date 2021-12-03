with open("input.txt", 'r') as f:
    numbers = sorted(f.read().splitlines())

gamma = ''
while numbers[0]:
    gamma += numbers[len(numbers)//2][0]
    numbers = sorted([number[1:] for number in numbers])

epsilon = ''.join(['0' if bit == '1' else '1' for bit in gamma])

print(int(gamma, 2) * int(epsilon, 2))
