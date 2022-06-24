# Step 1

# Constant
# Column number
column = int(7)
# Row number
row = int(6)


# Print grid
for rows in range(row):
    for columns in range(column):
        print(" . ", end="")
    print()
for i in range(column):
    print(f" {i} ", end="")
