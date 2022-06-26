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
unvalid = True

# Count the number of column
def count_column():
    row_count_column.clear()
    for i in range(nb_column):
        row_count_column.append(i)
    return row_count_column

# Print grid
def print_grid():
    for row in grid:
        for char in row:
            print(char, end=' ')
        print()
    for char in count_column():
        print(char, end=' ')
    print()

# Function that add coin to the grid
def add_coin(choice, symbol):
    for row in grid[::-1]:
        if row[choice] == ".":
            row[choice] = symbol
            return False
    return True
    """
    add_coin(int(input("Impossible rejouez :\n")), symbol)
    We could also have used this recursion but to avoid certain nesting limits we 
    have used an alternative
    """

# Creation of the grid
for row in range(nb_row):
    grid.append(["."]*nb_column)

# Main function
def main():
    while retry == "o" or retry == "O":
        victory = False
        print_grid()
        while victory==False:
            while add_coin(int(input('Joueur 1 à vous de jouer!\n')), "o"):
                print('Colonne pleine rejouez!\n')
            print_grid()
            while add_coin(int(input('Joueur 2 à vous de jouer!\n')), "x"):
                print('Colonne pleine rejouez!\n')
            print_grid()
            # victory = True
        retry = input("Voulez-vous rejouer? [O/N]")


