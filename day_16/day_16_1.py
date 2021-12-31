with open('input.txt', 'r') as f:
    bits_code = f.read().strip()
bits_code = ''.join([f"{int(hex_, 16):0{4}b}" for hex_ in bits_code])

cursor = iter(enumerate(bits_code))

version_total = 0
while True:
    try:
        version, opcode = '', ''
        for _ in range(3):
            version += next(cursor)[1]
        version_total += int(version, 2)
        for _ in range(3):
            opcode += next(cursor)[1]
        if opcode == '100': # opcode 4, literal
            while True:
                not_last = int(next(cursor)[1])
                for _ in range(4):
                    next(cursor)
                if not not_last:
                    break

        else: # operation
            length = int(next(cursor)[1])
            if length: # 11 bit
                length = ''
                for _ in range(11):
                    length += next(cursor)[1]
                length = int(length, 2)
            else: # 15 bit
                length = ''
                for _ in range(15):
                    length += next(cursor)[1]
                length = int(length, 2)
    except StopIteration:
        break

print(version_total)
