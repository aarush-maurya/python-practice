import random
def ran():
    number = random.randint(1,90)
    return number

num = [ran(),ran(),ran(),ran(),ran(),ran(),ran(),ran()]
num_sorted = sorted(num)
card = [[num_sorted[0],num_sorted[1],num_sorted[2]],
        [num_sorted[3],"BINGO!",num_sorted[4]],
        [num_sorted[5],num_sorted[6],num_sorted[7]]]
print(f"===BINGO CARD GENERATOR===")
print()
print(f"{card[0][0]: ^6}|{card[0][1]: ^6}|{card[0][2]: ^6}") 
print(f"{'-'*20}")
print(f"{card[1][0]: ^6}|{card[1][1]: ^6}|{card[1][2]: ^6}")
print(f"{'-'*20}")
print(f"{card[2][0]: ^6}|{card[2][1]: ^6}|{card[2][2]: ^6}")