row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# 23 column 2, row 3 -> horizontal 2 means 0 index, and row 3 means index 1
position = input("where do you want to put the treasure? ")

# index 0 and 1
horizontal = int(position[0]) 
vertical = int(position[1])

map[vertical - 1] [horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# https://app.codingrooms.com/management/assignments/364931/overview