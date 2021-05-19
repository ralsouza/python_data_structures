matrix = [
    ["John" , 8  , 7,  6],
    ["Peter", 4.5, 9, 10],
    ["Marc" , 6  , 6,  8]
]

for row in matrix:
    for col in row:
        print(f"{col} \t", end=" ")
    print("")