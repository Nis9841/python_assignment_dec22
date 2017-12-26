word = input("Enter the word separated by comma : ")
sort= sorted(word.split(','))
last = ",".join(sort)
print(last)