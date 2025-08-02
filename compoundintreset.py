def compinterest(P,n,r,t):
    A = P * (1 + r/n) ** (n * t)
    return A

P = 1000  # Principal amount
r = 0.05  # Annual interest rate (5%)
n = 12    # Compounded monthly
t = 10    # Time in years

final_amount = compinterest(P, r, n, t)
print("Final amount after", t, "years:", final_amount)