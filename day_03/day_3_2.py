with open("input.txt", 'r') as f:
    numbers = sorted(f.read().splitlines())

oxygen = ''
onumbers = numbers.copy()
while len(onumbers) > 1:
    mcb = onumbers[len(onumbers)//2][0]
    oxygen += mcb
    onumbers = [number[1:] for number in onumbers if number[0] == mcb] # don't need to sort again

co2 = ''
while len(numbers) > 1:
    lcb = '0' if numbers[len(numbers)//2][0] == '1' else '1'
    co2 += lcb
    numbers = [number[1:] for number in numbers if number[0] == lcb] # don't need to sort again
co2 += numbers[0] # not guaranteed to get to n bits, must add leftover at the end

print(int(oxygen, 2) * int(co2, 2))
