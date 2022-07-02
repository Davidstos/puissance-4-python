import os

# Constant
# Column number
nb_column = int(7)
# Row number
nb_row = int(6)
# Victory boolean
victory = bool()
# Grid List
grid = []
row_count_column = []
# Coin Skin
skin_coin_player_one = ["o"]
skin_coin_player_two = ["x"]

# Count the number of column used in print_grid function
def count_column():
    row_count_column.clear()
    for i in range(nb_column):
        row_count_column.append(i)
    return row_count_column


# Function that format the display of the grid
def print_grid():
    for row in grid:
        for char in row:
            print(char, end=" ")
        print()
    for char in count_column():
        print(char, end=" ")
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
def create_grid():
    grid.clear()
    for row in range(nb_row):
        grid.append(["."] * nb_column)


# Check if the user input is valid
def check_input(player_input, player):
    while True:
        try:
            int(player_input)
            if 0 <= int(player_input) < nb_column:
                os.system("cls")
                return int(player_input)
        except ValueError:
            player_input = input(
                f"Votre saisie est incorrecte joueur {player} \nVeuillez saisir un chiffre entre 0 et 6!\n"
            )


# Function to check if 4 coins are aligned horizontally
def row_alignment(grid: list):
    for i in range(6):
        nb_player_1 = 0
        nb_player_2 = 0

        for j in range(7):
            if grid[i][j] == skin_coin_player_one[0]:
                nb_player_1 += 1
                nb_player_2 = 0
                if nb_player_1 == 4:
                    return True
            elif grid[i][j] == skin_coin_player_two[0]:
                nb_player_2 += 1
                nb_player_1 = 0
                if nb_player_2 == 4:
                    return True
            else:
                nb_player_1 = 0
                nb_player_2 = 0
    return False


# Function to check if 4 coins are aligned vertically
def column_alignment(grid: list):
    for j in range(7):
        nb_player_1 = 0
        nb_player_2 = 0

        for i in range(6):
            if grid[i][j] == skin_coin_player_one[0]:
                nb_player_1 += 1
                nb_player_2 = 0
                if nb_player_1 == 4:
                    return True
            elif grid[i][j] == skin_coin_player_two[0]:
                nb_player_2 += 1
                nb_player_1 = 0
                if nb_player_2 == 4:
                    return True
            else:
                nb_player_1 = 0
                nb_player_2 = 0
    return False


# Function to check if 4 coins are diagonal descending aligned
def down_alignment(grid: list):
    for i in range(3):
        nb_player_1 = 0
        nb_player_2 = 0
        x = 0
        y = i

        while x < 7 and y < 6:
            if grid[y][x] == skin_coin_player_one[0]:
                nb_player_1 += 1
                nb_player_2 = 0
                if nb_player_1 == 4:
                    return True
            elif grid[y][x] == skin_coin_player_two[0]:
                nb_player_2 += 1
                nb_player_1 = 0
                if nb_player_2 == 4:
                    return True
            else:
                nb_player_1 = 0
                nb_player_2 = 0

            x += 1
            y += 1

    for j in range(4):
        nb_player_1 = 0
        nb_player_2 = 0
        x = j
        y = 0

        while x < 7 and y < 6:
            if grid[y][x] == skin_coin_player_one[0]:
                nb_player_1 += 1
                nb_player_2 = 0
                if nb_player_1 == 4:
                    return True
            elif grid[y][x] == skin_coin_player_two[0]:
                nb_player_2 += 1
                nb_player_1 = 0
                if nb_player_2 == 4:
                    return True
            else:
                nb_player_1 = 0
                nb_player_2 = 0

            x += 1
            y += 1

    return False


# Function to check if 4 coins are diagonal ascending aligned
def up_alignment(grid: list):
    for i in range(3, 6):
        nb_player_1 = 0
        nb_player_2 = 0
        x = 0
        y = i

        while x < 7 and y > -1:
            if grid[y][x] == skin_coin_player_one[0]:
                nb_player_1 += 1
                nb_player_2 = 0
                if nb_player_1 == 4:
                    return True
            elif grid[y][x] == skin_coin_player_two[0]:
                nb_player_2 += 1
                nb_player_1 = 0
                if nb_player_2 == 4:
                    return True
            else:
                nb_player_1 = 0
                nb_player_2 = 0

            x += 1
            y -= 1

    for j in range(4):
        nb_player_1 = 0
        nb_player_2 = 0
        x = j
        y = 0

        while x < 7 and y > -1:
            if grid[y][x] == skin_coin_player_one[0]:
                nb_player_1 += 1
                nb_player_2 = 0
                if nb_player_1 == 4:
                    return True
            elif grid[y][x] == skin_coin_player_two[0]:
                nb_player_2 += 1
                nb_player_1 = 0
                if nb_player_2 == 4:
                    return True
            else:
                nb_player_1 = 0
                nb_player_2 = 0

            x += 1
            y -= 1
    return False


# Function that displays the scoreboard
def score_board(score_player_one, score_player_two):
    print(" ------------- ")
    print(f"|    score     |")
    print(" ------------- ")
    print(f"| Joueur 1 : {score_player_one} |")
    print(f"| Joueur 2 : {score_player_two} |")
    print(" ------------- ")


# Function that change the skin of coins
def change_coin():
    print(" --------------------- ")
    print("|  Modification Coin  |")
    print("| ------------------- |")
    print(f"|  1 - Joueur 1 -> {skin_coin_player_one[0]}  |")
    print(f"|  2 - Joueur 2 -> {skin_coin_player_two[0]}  |")
    print("|  3 - Menu           |")
    print(" --------------------- ")
    choice = input()
    match choice:
        case "1":
            skin_coin_player_one.clear()
            skin_coin_player_one.append(
                str(input("Choisissez votre nouveau skin ex: V\n"))
            )
            os.system("cls")
        case "2":
            skin_coin_player_two.clear()
            skin_coin_player_two.append(
                str(input("Choisissez votre nouveau skin ex: V\n"))
            )
            os.system("cls")
        case "3":
            os.system("cls")
            menu()
        case _:
            os.system("cls")
            print("Le choix n'est pas correct")
            change_coin()


# Function that launches the game
def start_game():
    retry = "o"
    score_player_one = 0
    score_player_two = 0
    while retry == "o" or retry == "O":
        create_grid()
        create_grid()
        victory = False
        score_board(score_player_one, score_player_two)
        print_grid()
        while victory == False:
            while add_coin(
                check_input(input("Joueur 1 à vous de jouer!\n"), 1),
                skin_coin_player_one[0],
            ):
                print("Colonne pleine rejouez!\n")
            score_board(score_player_one, score_player_two)
            print_grid()
            g1 = row_alignment(grid)
            g2 = column_alignment(grid)
            g3 = down_alignment(grid)
            g4 = up_alignment(grid)
            # test if player one is
            if g1 or g2 or g3 or g4:
                print("Le joueur 1 à gagné !")
                victory = True
                score_player_one += 1
                continue
            while add_coin(
                check_input(input("Joueur 2 à vous de jouer!\n"), 2),
                skin_coin_player_two[0],
            ):
                print("Colonne pleine rejouez!\n")
            score_board(score_player_one, score_player_two)
            print_grid()

            g1 = row_alignment(grid)
            g2 = column_alignment(grid)
            g3 = down_alignment(grid)
            g4 = up_alignment(grid)

            if g1 or g2 or g3 or g4:
                print("Le joueur 2 à gagné !")
                victory = True
                score_player_two += 1
                continue
            # victory = True
        retry = input("Voulez-vous rejouer? [O/N]\n")
    menu()


# Menu
def menu():
    print(" ------------------------- ")
    print("|           MENU          |")
    print("| ----------------------- |")
    print("| 1 - Commencer la partie |")
    print("| 2 - Changement de coin  |")
    print("| 3 - Quitter             |")
    print(" ------------------------- ")
    choice = input()
    match choice:
        case "1":
            os.system("cls")
            print("Démarrage de la partie")
            start_game()
        case "2":
            change_coin()
            menu()
        case "3":
            quit("A la prochaine :)")
        case _:
            os.system("cls")
            print("Le choix n'est pas correct")
            menu()


menu()
