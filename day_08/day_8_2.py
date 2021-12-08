with open("input.txt", 'r') as f:
    signals = f.readlines()

total_sum = 0
for signal in signals:
    display_map = dict()
    digits, output = [x.strip() for x in signal.split('|')]

    # get the "easy digits"
    for digit in digits.split():
        if len(digit) == 7:
            display_map['8'] = ''.join(sorted(digit))
        elif len(digit) == 3:
            display_map['7'] = ''.join(sorted(digit))
        elif len(digit) == 4:
            display_map['4'] = ''.join(sorted(digit))
        elif len(digit) == 2:
            display_map['1'] = ''.join(sorted(digit))

    # top = 7 - 1
    for segment in display_map['1']:
        display_map['top'] = display_map['top'].replace(segment, '') if 'top' in display_map else display_map['7'].replace(segment, '')

    # The b(ottom)l(eft) segment is the only segment with a frequency of 3 in the remaining digits
    unknown_digits = list()
    segment_freq = dict()
    for digit in digits.split():
        if len(digit) == 5 or len(digit) == 6:
            unknown_digits.append(''.join(sorted(digit)))
    for digit in unknown_digits:
        for segment in 'a', 'b', 'c', 'd', 'e', 'f', 'g':
            if segment in digit:
                segment_freq[segment] = 1 if segment not in segment_freq else segment_freq[segment] + 1
    for key, value in segment_freq.items():
        if value == 3:
            display_map['bl'] = key
            break

    # 9 = 8 - bl
    display_map['9'] = display_map['8'].replace(display_map['bl'], '')
    unknown_digits.remove(display_map['9'])

    # 5 and 6 are diff'ed only by bl
    for digit in unknown_digits:
        for _digit in unknown_digits:
            if digit == _digit.replace(display_map['bl'], '') and digit != _digit:
                display_map['5'] = digit
                display_map['6'] = _digit
                break
        else:
            continue
        break
    unknown_digits.remove(display_map['5'])
    unknown_digits.remove(display_map['6'])

    # with 6 solved, only 0 has len(6)
    for digit in unknown_digits:
        if len(digit) == 6:
            display_map['0'] = digit
            unknown_digits.remove(digit)
            break

    # between 2 and 3, 2 has bl and 3 does not
    for digit in unknown_digits:
        if display_map['bl'] in digit:
            display_map['2'] = digit
        else:
            display_map['3'] = digit

    # flip the map for easier access
    display_map = {value: key for key, value in display_map.items()}

    number = ''
    for digit in output.split():
        number += display_map[''.join(sorted(digit))]
    total_sum += int(number)

print(total_sum)
