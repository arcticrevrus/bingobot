import random


class BingoBoard:
    def __init__(self, cells, free_cell):
        self.cells = cells
        self.free_cell = free_cell

    def __str__(self):
        header_fix = "       "
        header = f"|{header_fix}B{header_fix}|{header_fix}I{header_fix}|{header_fix}N{header_fix}|{header_fix}G{header_fix}|{header_fix}O{header_fix}|\n"
        spacer = "|"
        seperator = "|_______________"
        final_string = " _______________" * 5 + "\n" + f"{header}"
        for row in range(5):
            for cell_line in range(2):
                if cell_line != 1:
                    final_string += seperator * 5 + "|\n"
                else:
                    for column in range(5):
                        if (5 * row + column) < 24:
                            for cell_line in range(2):
                                match cell_line:
                                    case 1:
                                        if column == 2 and row == 2:
                                            text = self.free_cell.strip()
                                            if len(text) < 15:
                                                while len(text) < 15:
                                                    text = " " + text
                                                    if len(text) < 15:
                                                        text = text + " "
                                            final_string += spacer + text + spacer
                                        else:
                                            text = self.cells[5 * row + column].strip()
                                            if len(text < 15):
                                                words = text.split(" ")

                                            if len(text) < 15:
                                                while len(text) < 15:
                                                    text = " " + text
                                                    if len(text) < 15:
                                                        text = text + " "
                                                final_string += spacer + text
                            if column == 4:
                                final_string += "|\n"
        final_string += "\n" + seperator * 5 + "|\n"

        return final_string


free_file = open("free.txt", "r").readlines()
line_file = open("lines.txt", "r").readlines()
if sum(1 for _ in line_file) < 24:
    print("not enough lines in lines.txt")
    exit()
if sum(1 for _ in free_file) < 1:
    print("not enough lines in free.txt")
    exit()

lines = []


while len(lines) < 24:
    line = random.choice(line_file)
    if line not in lines:
        lines.append(line)

test_board = BingoBoard(lines, random.choice(free_file))

print(test_board)
