import tetris_blocks
import numbersforscore
import color


class NumberToBlock:
    @staticmethod
    def get_block(number: int):
        numbers_list = NumberToBlock.get_list_of_single_numbers(number)

        blocks = []
        for number in numbers_list:
            blocks.append(numbersforscore.NumbersForScore.number[number])

        field = []
        for block in blocks:
            field.extend(block)

        return tetris_blocks.Block([field]*4, color.BlockColor.red)


    @staticmethod
    def get_list_of_single_numbers(number: int):
        numbers_list = [number % 10, number // 10 % 10, number // 100 % 10, number // 1000 % 10]
        return numbers_list


nb = NumberToBlock()
nb.get_block(98876)