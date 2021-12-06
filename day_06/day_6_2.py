with open("input.txt", 'r') as f:
    input_fish = f.readline().split(',')
input_fish = list(map(int, input_fish))
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for f in input_fish:
    fish[f] += 1

for day in range(256):
    new_fish = fish[0]
    for i in range(8):
        fish[i] = fish[i+1]
    fish[8] = new_fish # actual new fish
    fish[6] += new_fish # freshly spawned

print(sum(fish))
