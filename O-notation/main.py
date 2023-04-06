#1. Какая сложность у этого алгоритма?
n = int(input())
m = int(input())
cnt = 0
for i in range(n):
	for j in range(m):
		cnt += 1
print(cnt)
#Сложность: О(n + m)

#------------------------------------------------------------------------------------------------------------------------

#2. Какая сложность у этого алгоритма?
n = int(input())
ans = n * n + 100
ans -= 200
ans *= ans
if (ans < 1000000):
	ans *= 2

#Сложность: O(n ^ 2)

#------------------------------------------------------------------------------------------------------------------------

#3. Какая сложность у этого алгоритма?
n = int(input())
m = int(input())
k = 1000
for i in range(n):
	for j in range(m):
		k += 100

for i in range(m):
	for j in range(m):
		k -= 100

#Сложность: O(n*m + m^2)