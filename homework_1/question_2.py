# Question 2

# # n = int(raw_input())
# n = 8
#
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i +=  1
# print(fact)

n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
