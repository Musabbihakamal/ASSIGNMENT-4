MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"Removed: {removed_element}")

def main():
    lst = ['a', 'b', 'c', 'd', 'e']
    print("Original list:", lst)
    shorten(lst)
    print("Modified list:", lst)

if __name__ == "__main__":
    main()
