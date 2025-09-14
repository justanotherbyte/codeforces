rows, cols = list(map(int, input().split(" ")))

table = [["#"] * cols] * rows

side = True # left = True, right = False
for idx, row in enumerate(table, start=1):
    if idx % 2 == 0:
        new_row = ["."] * (cols - 1)
        new_row.append("#")

        if side is False:
            new_row.reverse()

        table[idx-1] = new_row

        side = not side

for row in table:
    print("".join(row))