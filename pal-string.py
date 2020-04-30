s=input("Enter string: ")
s=s.upper()
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
if s==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
