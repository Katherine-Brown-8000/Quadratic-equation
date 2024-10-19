# The quadratic equation
print("Enter a, b and c to caLculate the quadratic equation")
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# Insert the values
neg_b = b * -1
num_b = b*b
num_a = 4*a*c
dom_a = 2*a

# Solve the function in the square root
solve_1 = num_b - num_a

if solve_1 < 0:
    print("Non viable solution, have no input")

else:
    # Solve the square root
    solve_2 = solve_1 ** 0.5

    # This is the part where the exponent takes it positive or negative form
    solve_3 = neg_b + solve_2
    solve_4 = neg_b - solve_2

    # Divide the positive and negative forms by the dominator
    solve_5 = solve_3/dom_a
    solve_6 = solve_4/dom_a

    print(f"X is {solve_5}")
    print(f"X is {solve_6}")