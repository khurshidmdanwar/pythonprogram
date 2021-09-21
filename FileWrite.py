# open the file.txt in append mode. Create a new file if no such file exists.
fileptr = open("firstFile.txt", "a")
# appending the content to the file
fileptr.write('''Hello, how are you?
I'm fine, how about you????
''')
# closing the opened the file
fileptr.close()
