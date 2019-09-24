'''
This program asks the user for the ISBN number and checks if it is a valid
ISBN code. It prints out YES if it is valid, and NO when it is not valid
'''
#Miki Ando

isbn = input("ISBN: ")

while (isbn.isdigit() == False) or (len(isbn) != 10):
    isbn = input("Retry: ")

digit = int(isbn) % 10
sumValue = 0

for i in range (9,0,-1):
    isbnDigit = ((int(isbn) // (10** (10 - i))) % 10) * i
    sumValue = sumValue + isbnDigit

if sumValue % 11 == digit:
    print("YES")
else:
    print("NO")
 
