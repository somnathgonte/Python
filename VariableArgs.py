def addition(*No):
    print(No)           # (11,21,51,101)
    print(type(No))     # Tuple
    print(len(No))      # 4

def main():
    addition(11,21,51,101)

if __name__ == "__main__":
    main()