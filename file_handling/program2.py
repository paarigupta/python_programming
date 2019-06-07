# To count the repeation of words.

fname = input("Enter the file name ")
word = input("Enter the word ")
k = 0
f = open(fname , 'r') 
for line in f.readlines():
    words = line.split()
    for i in words:
        if i==word:
            k+=1
print(k ,'times')
f.close()
