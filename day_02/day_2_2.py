with open("input.txt", 'r') as f:
    commands = f.read().splitlines()
    
horizontal, depth, aim = 0, 0, 0
for command in commands:
    command = command.split(' ')
    if command[0] == 'forward':
        horizontal += int(command[1])
        depth += aim * int(command[1])
    elif command[0] == 'down':
        aim += int(command[1])
    else: # command[0] == 'up'
        aim -= int(command[1])

print(horizontal * depth)
