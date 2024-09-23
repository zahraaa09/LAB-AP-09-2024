N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(f"MOVE ke ({i}, {j})")
    else:
        for j in range (M-1, -1, -1):
            print(f"MOVE ke ({i}, {j})")