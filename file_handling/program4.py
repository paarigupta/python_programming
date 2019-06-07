# To print all the numbers present in file

fname = input("Enter the file name: ")
with open(fname,'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if letter.isdigit():
                    print(letter)
    else:
        print("No digit present")
