import math

# Constant
x = 1.5

#  inputs in TXT files
p = [1.0, 2.5, 0.1, 4.0, 3.3]
q = [2.0, 1.5, 0.5, 3.0, 1.1]
r = [0.0, 0.5, 1.0, 1.5, 2.0]

s = [1.0, 2.0, 0.5, 1.5, 0.3]
t = [0.5, 1.0, 2.0, 1.0, 0.7]
u = [3.0, 4.0, 2.5, 5.0, 3.5]
v = [1.0, 2.0, 0.5, 1.5, 1.0]

# Calculate A values
A = []
for i in range(len(p)):
    try:
        value = math.log(p[i] + q[i]**2) + math.sin(r[i] * math.pi)
    except ValueError:
        value = float('nan')  # log of negative number
    A.append(value)

# Calculate B values
B = []
for i in range(len(s)):
    try:
        value = math.pow(math.e,(-s[i] * t[i])) + math.cos(u[i] / (v[i] + x))
    except ZeroDivisionError:
        value = float('inf')  # division by zero
    B.append(value)

# Output the results
print("A values (Equation 1):")
for i, val in enumerate(A):
    print(f"{i}: {val}")

print("\nB values (Equation 2):")
for i, val in enumerate(B):
    print(f"{i}: {val}")