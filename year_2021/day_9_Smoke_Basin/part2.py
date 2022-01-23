def run(input_matrix, p1_results, day, name):
    def find_basin_size(p1_result, im):
        def check_point(row, col, locs, im):
            if ((row, col)) in locs:
                return
            if im[row][col] >= 9:
                return
            locs.add((row, col))
            for rc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                check_point(rc[0], rc[1], locs, im)

        _, r, c = p1_result
        locs = set()
        check_point(r, c, locs, im)
        #print(locs)
        return len(locs)

    basin_sizes = []
    for p1_result in p1_results:
        basin_sizes.append(find_basin_size(p1_result, input_matrix))
        # print(basin_sizes)
    answer = 1
    for size in sorted(basin_sizes, reverse=True)[0:3]:
        answer *= size

    print(f"== Results for day {day} - {name}, part 2.")
    print(f"   {answer=}")
