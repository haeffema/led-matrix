import playground
import tetris
class matrix:
    matrix_20_10 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def print_block(block):
        print("")
        for x in range(0, len(block)):
            for y in range(0, len(block[0])):
                print(block[x][y], end=" ")
            print("")
        print("")


    def is_line_full(line):
        ret = True
        for pos in line:
            if pos == 0:
                ret = False
        return ret

    for line in matrix_20_10:
            is_full = is_line_full(line)

    while matrix_20_10.count([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) > 0:
        matrix_20_10.remove([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        matrix_20_10.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        print_block(matrix_20_10)



