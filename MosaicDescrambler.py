import os

WIDTH = 3500
HEIGHT = 3200
SIZE = 100
W = int(WIDTH / SIZE)
H = int(HEIGHT / SIZE)
FILENAME = 'scrambled.png'

spiral = []

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
current_direction = 0
x = 0
y = 0
visited = [[False for i in range(0, W)] for j in range(0, H)]

# Generate spiral coordinates
for i in range(0, W * H):
    spiral.append((x, y))
    visited[x][y] = True
    tmp_x = x + directions[current_direction][0]
    tmp_y = y + directions[current_direction][1]
    if tmp_x >= H or tmp_y >= W or tmp_x < 0 or tmp_y < 0 or visited[tmp_x][tmp_y]:
        # switch to next direction
        current_direction += 1
        current_direction = current_direction % 4
        tmp_x = x + directions[current_direction][0]
        tmp_y = y + directions[current_direction][1]
    x = tmp_x
    y = tmp_y
    # count += 1

# Slice tiles using spiral order, using imagemagick
# mkdir scrambled
for (i, (x, y)) in enumerate(spiral):
    offset_x = x * SIZE
    offset_y = y * SIZE
    command = f'convert {FILENAME} -crop {SIZE}x{SIZE}+{offset_y}+{offset_x} scrambled/{i:04}.png'
    print(command)
    os.system(command)

# Rename the files (to suit the order for using montage to combine the tiles)
# mkdir scrambled2
for row in range(0, 32):
    for column in range(0, 35):
        from_tile = column * 32 + row
        to_tile = row * 35 + column
        os.system(f'cp scrambled/{from_tile:04}.png scrambled2/{to_tile:04}.png')

# Run the following command to combine the tiles:
# montage scrambled2/*.png -mode Concatenate -tile 35x32 murphy.png
