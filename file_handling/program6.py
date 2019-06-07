# To compare two files are identical or not

f1 = input("Enter the file name: ")
f2 = input("Enter the file name: ")
file1 = open(f1,'r')
file2 = open(f2,'r')
s1 = file1.read()
s2 = file2.read()
if s1 == s2:
    print("Identical")
else:
    print("Not Identical")
file1.close()
file2.close()
