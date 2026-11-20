"""Q27: Multiplication tables 1 to 10 in tabular format (nested loops)."""

print("MULTIPLICATION TABLE (1 to 10)")
print("-" * 55)
print("   x |", end="")
for j in range(1, 11):
    print(f"{j:4d}", end="")
print("\n" + "-" * 55)

for i in range(1, 11):
    print(f"{i:4d} |", end="")
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()
