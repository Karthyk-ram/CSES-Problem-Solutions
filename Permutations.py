def main():
    n = int(input())

    if n >= 4:
        for i in range(2, n + 1):
            if i % 2 == 0:
                print(i, end=" ")

        for i in range(1, n + 1):
            if i % 2 != 0:
                print(i, end=" ")
    elif n == 1:
        print(1)
    else:
        print("NO SOLUTION")

main()