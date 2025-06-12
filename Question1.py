import math

# Constant
x = 1.5

# Input lists
p = [1.0, 2.5, 0.1, 4.0, 3.3]
q = [2.0, 1.5, 0.5, 3.0, 1.1]
r = [0.0, 0.5, 1.0, 1.5, 2.0]

s = [1.0, 2.0, 0.5, 1.5, 0.3]
t = [0.5, 1.0, 2.0, 1.0, 0.7]
u = [3.0, 4.0, 2.5, 5.0, 3.5]
v = [1.0, 2.0, 0.5, 1.5, 1.0]

# Calculate A values using Equation 1
A = []
for pi, qi, ri in zip(p, q, r):
    try:
        result = math.log(pi + qi ** 2) + math.sin(ri * math.pi)
    except ValueError:
        result = float('nan')
    A.append(result)

# Calculate B values using Equation 2
B = []
for si, ti, ui, vi in zip(s, t, u, v):
    try:
        result = math.exp(-si * ti) + math.cos(ui / (vi + x))
    except ZeroDivisionError:
        result = float('inf')
    B.append(result)

# Print A results
print("A values (Equation 1):")
for i, val in enumerate(A):
    print(f"{i}: {val}")

# Print B results
print("\nB values (Equation 2):")
for i, val in enumerate(B):
    print(f"{i}: {val}")