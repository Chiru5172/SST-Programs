# s="madam"
# print(s[::-1])


# n=int(input())
# a=n
# s=0
# while a>0:
#     r=a%10
#     s=s*10+r
#     a//=10
# if s==n:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


s="madam"
a=''
for i in s:
    a+=i
if a==s:
    print("Palindrome")
else:
    print("Not a Palindrome")