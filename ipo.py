def knapsack(C, w, v):
    # Sort the items by value-to-weight ratio
    ratio = [v[i] / w[i] for i in range(len(w))]
    items = sorted(range(len(w)), key=lambda i: ratio[i], reverse=True)
    # Fill the knapsack with the items
    x = [0] * len(w)
    z = 0
    for i in items:
        if w[i] <= C:
            x[i] = 1
            z += v[i]
            C -= w[i]
        else:
            x[i] = C / w[i]
            z += v[i] * x[i]
            break
    return x, z


# Example usage
C = 50
w = [10, 20, 30]
v = [60, 100, 120]
x, z = knapsack(C, w, v)
print(f"x = {x}")
print(f"z = {z}")
