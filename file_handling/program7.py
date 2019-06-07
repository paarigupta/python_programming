# TO print no. of characters present in file.

f1 = input("Enter the file name: ")
characters = 0
lines = 0
words = 0
file1 = open(f1,'r')
for line in file1:
    s = line.split()
    lines = lines + 1
    words = words + len(s)
    characters = characters+ len(line)
print("No. of characters are: ",characters)
file1.close()
