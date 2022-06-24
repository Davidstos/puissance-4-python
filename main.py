# Step 1

# Constant
# Column number
nb_column = int(7)
# Row number
nb_row = int(6)
# Victory boolean
victory = bool()
retry="o"
# Grid List
grid=[]
row_count_column = []


def count_column():
    row_count_column.clear()
    for i in range(nb_column):
        row_count_column.append(i)
    return row_count_column
for row in range(nb_row):
    grid.append(["."]*nb_column)

# Print grid
def print_grid():
    for row in grid:
        for char in row:
            print(char, end=' ')
        print()
    for char in count_column():
        print(char, end=' ')

while retry == "o" or retry == "O":
    victory = False
    while victory==False:
        print_grid()
        print()
        choice = input('Joueur 1 à vous de jouer!\n')
        choice = input('Joueur 2 à vous de jouer!\n')
        victory = True
    retry = input("Voulez-vous rejouer? [O/N]")


