from get_data import get_input_data
import part1
import part2

DAY = 12
NAME = "Passage Pathing"

input_data ="""start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

def add_path(from_cave, to_cave, cave_connections:dict):
    destinations = cave_connections.get(from_cave, [])
    if to_cave not in destinations:
        destinations.append(to_cave)
        cave_connections[from_cave] = destinations

#input_data = get_input_data(day=DAY)
input_lines = input_data.strip().split('\n')
all_connections = [line.split('-')  for line in input_lines]
cave_connections = {}
for f_c, t_c in all_connections:
    # path works two ways
    add_path(f_c, t_c, cave_connections)
    add_path(t_c, f_c, cave_connections)

print(cave_connections)

part1.run(cave_connections, DAY, NAME)
part2.run(cave_connections, DAY, NAME)
