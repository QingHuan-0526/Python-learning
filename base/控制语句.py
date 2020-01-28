# if
score = 95
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >=60:
    print("C")
else:
    print("D")
print("----------------------------------------")

# 三元表达式
a = 9
res = a if a > 10 else 10
print(res)
print("----------------------------------------")

# while
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
print("----------------------------------------")


# for
for num in range(0,10):
    print(num)
arr = [12,85,79,0,42,16]
for num in arr:
    print(num)
print("----------------------------------------")

# break
j = 0
while j <= 10:
    if j==3:
        break
    j += 1
    print(j)
print("----------------------------------------")

# continue
k = 0
while k <= 10:
    k += 1
    print(k)
    if k == 3:
        continue
print("----------------------------------------")

# while中的else
z = 0
while z <= 10:
    z += 1
else:
    print(z)
print("----------------------------------------")


# for中的else
for item in range(0,5):
    print(item)
else:
    print("xxx")
print("----------------------------------------")

# range
for i in range(0,10,2):
    print(i)
print("----------------------------------------")
for i in range(10,-10,-2):
    print(i)