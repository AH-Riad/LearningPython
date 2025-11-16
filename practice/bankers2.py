n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

print("\nEnter allocation matrix:")
allocation = []
for i in range(n):
    allocation.append(list(map(int, input(f"Process {i+1}: ").split())))
    
print("\nEnter maximum matrix:")
maximum = []
for i in range(n):
    maximum.append(list(map(int, input(f"Process {i+1}: ").split())))

available = list(map(int, input("Enter available resources: ").split()))

# Calculate the Need matrix
need = []
for i in range(n):
    need.append([maximum[i][j] - allocation[i][j] for j in range(m)])

# Print Need matrix
print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i+1}: {need[i]}")

# Print Available resources
print("\nAvailable Resources:", available)

finish = [0] * n
safeSequence = []

while len(safeSequence) < n:
    found = False
    for i in range(n):
        if finish[i] == 0 and all(need[i][j] <= available[j] for j in range(m)):
            # Process can be allocated
            for j in range(m):
                available[j] += allocation[i][j]  # Release resources
            finish[i] = 1
            safeSequence.append(i + 1)
            found = True
            break  # Go back to start and check from first process again
    if not found:
        break

if len(safeSequence) == n:
    print("\nSystem is in a safe state.")
    print("Safe sequence:", " -> ".join(map(str, safeSequence)))
else:
    print("\nSystem is NOT in a safe state.")
