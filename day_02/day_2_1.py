with open("input.txt", 'r') as f:
    commands = f.read().splitlines()
    
horizontal, depth = 0, 0
for command in commands:
    command = command.split(' ')
    if command[0] == 'forward':
        horizontal += int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
    else: # command[0] == 'up'
        depth -= int(command[1])

print(horizontal * depth)
