# To print no. of lines present in file.

fname = input("Enter the file name: ")
with open(fname,'r') as f:
    num_lines = 0
    for line in f:
        num_lines+=1
print("No. of lines are: ",num_lines)
