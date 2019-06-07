# To copy content of one file in another

with open('file1.py' , 'r') as f:
    with open('file2.py' , 'w') as f1:
        for line in f:
            f1.write(line)
