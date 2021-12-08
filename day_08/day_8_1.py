with open("input.txt", 'r') as f:
    signals = f.readlines()

unique_digits = 0
for signal in signals:
    signal = signal.split('|')[1].strip().split()
    for digit in signal:
        if len(digit) == 5 or len(digit) == 6:
            continue
        unique_digits += 1

print(unique_digits)
    
