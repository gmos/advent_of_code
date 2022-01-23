def run(input_matrix, day, name):

    results = []

    # scan all rows (skipping the dummies at the border)
    for row_num in range(1, len(input_matrix) - 1):
        row = input_matrix[row_num]
        for col_num in range(1, len(row) - 1):
            cell = row[col_num]
            if cell >= row[col_num - 1] or cell >= row[col_num + 1]:
                continue  # not lower horizontally
            if (
                cell >= input_matrix[row_num - 1][col_num]
                or cell >= input_matrix[row_num + 1][col_num]
            ):
                continue  # not lower vertically
            results.append((cell, row_num, col_num))

    risk_level = sum(point[0] + 1 for point in results)

    print(f"== Results for day {day} - {name}, part 1.")
    print(f"   {risk_level=}")
    return results
