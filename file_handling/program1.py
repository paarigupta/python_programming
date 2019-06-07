# To count no. of words in txt file.

fname = input("Enter the file name ")
num_words = 0
with open(fname,'r') as f:
    for line in f:
        words = line.split()
        num_words +=len(words)
print("No. of words are ",num_words)
