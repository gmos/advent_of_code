def run(cave_connections:dict[str,list[str]], day, name):

    def advance(to_cave:str, visited: tuple, ):
        visited = (*visited, to_cave)
        from_cave = to_cave
        for next_cave in cave_connections[from_cave]:
            print('try', next_cave, 'from', from_cave)
            if next_cave in visited and next_cave.islower():
                # Not allowed to go back to minor cave -> skip
                print('minor twice -> skip')
                continue
            if next_cave == 'end':
                # We are done with one path
                print('got one', visited)
                continue
            return advance(next_cave, visited)
        return visited[:-2]

    visited = tuple()
    advance('start', visited)

    print(f"== Results for day {day} - {name}, part 1.")
    print(" ** TBD **")
