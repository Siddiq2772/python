# Q.1
# print("good morning:",input("enter name: "))

# Q.2
letter ='''
Dear <|name|>,
you are selected!!
<|Date|>
'''
print(letter.replace("<|name|>",input("Enter Name")).replace("<|Date|>",input("enter date")))
print("hello\n how are you")