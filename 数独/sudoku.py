"""
Output: 
[["1","9","8","4","5","6","3","7","2"], 
["7","3","6","8","1","2","9","4","5"], 
["4","2","5","7","3","9","1","6","8"], 
["6","4","3","9","2","8","7","5","1"], 
["9","8","2","1","7","5","4","3","6"], 
["5","7","1","6","4","3","8","2","9"], 
["3","5","7","2","9","1","6","8","4"], 
["8","1","4","5","6","7","2","9","3"],
["2","6","9","3","8","4","5","1","7"]]"""

table = [["1", " ", " ", "4", "5", "6", "3", "7", "2"],
         ["7", "3", "6", "8", " ", " ", " ", " ", "5"],
         [" ", "2", " ", "7", " ", "9", "1", " ", "8"],
         ["6", "4", " ", " ", " ", "8", "7", "5", " "],
         [" ", "8", "2", " ", " ", "5", " ", " ", " "],
         ["5", " ", "1", "6", " ", "3", "8", " ", " "],
         ["3", "5", "7", "2", "9", "1", " ", "8", "4"],
         [" ", " ", " ", "5", " ", "7", " ", " ", "3"],
         ["2", " ", " ", "3", "8", " ", " ", " ", " "]]
print("Input:")
for row in table:
    print(row)
print()


def constraint(i_row, i_col):
    _row = sorted(table[i_row])
    for i in range(len(_row) - 1):
        # 检查i_row行内有没有相同的数字
        if _row[i] != ' ' and _row[i] == _row[i + 1]:
            return False

    _col = sorted([table[i][i_col] for i in range(len(table))])
    for i in range(len(_col) - 1):
        if _col[i] != ' ' and _col[i] == _col[i + 1]:
            return False

    if 0 < i_row < 8 and 0 < i_col < 8:
        i = i_row // 3 * 3  # 该3*3的左上角
        j = i_col // 3 * 3  # 该3*3的左上角
        _box = sorted([table[i0][j0] for i0 in range(i, i + 3) for j0 in range(j, j + 3)])
        for i in range(len(_box) - 1):
            if _box[i] != ' ' and _box[i] == _box[i + 1]:
                return False

    return True


def find_next(_row, _col):
    for j in range(_col + 1, 9):
        if table[_row][j] == " ":
            return _row, j
    for i in range(_row + 1, 9):
        for j in range(0, 9):
            if table[i][j] == " ":
                return i, j
    return 9, 0


def back_tracing(_row, _col):
    if _row > 8:
        print("Output:")
        for row in table:
            print(row)
    else:
        for _value in range(1, 10):
            table[_row][_col] = str(_value)
            if constraint(_row, _col):
                back_tracing(*find_next(_row, _col))
        table[_row][_col] = " "


back_tracing(*find_next(0, 0))
