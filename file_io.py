#open a file in a write mode - "w", append mode - "a", read mode - "r"
#file open modes
# r - read only
# w - write only - cannot read
# r+ - opens for read and write. will not create a file if not exists
# w+ - opens for read and write. if file does not exist creates a new file. If exists overwrites file
# a - opens in append mode. Whatever you write will be appended
f=open("/home/training/Documents/python_tutorial/data/file_io.txt","a")
f.write("\nI love php")
f.close()

#read and print the entire file
f=open("/home/training/Documents/python_tutorial/data/file_io.txt","r")
print(f.read())
f.close()
print("---------------------------------------------------------------------")
#read and print the file line by line
f=open("/home/training/Documents/python_tutorial/data/file_io.txt","r")
for line in f:
    print(line)
f.close()
print("---------------------------------------------------------------------")
#read and print the file line by line and count the number of words in a line
f=open("/home/training/Documents/python_tutorial/data/file_io.txt","r")
for line in f:
    tokens = line.split(' ') #split will split the string using input character and 
                             #return a list(array) or words
    print("Wordcount:"+str(len(tokens))+ ' '+line)
f.close()


#use with statement so that you dont have to close the file.

with open("/home/training/Documents/python_tutorial/data/file_io.txt","r") as f:
    print(f.read())

print(f.closed)

