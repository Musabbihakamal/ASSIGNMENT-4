def main():
    for number in range(10, 20):
        if number % 2 == 0:
            print(f"{number} even", end=' ')
        else:
            print(f"{number} odd", end=' ')

if __name__ == '__main__':
    main()
