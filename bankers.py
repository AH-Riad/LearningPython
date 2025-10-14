n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    allocation.append(list(map(int, input(f"Process {i+1}: ").split())))

print("\nEnter Maximum Matrix:")
maximum = []
for i in range(n):
    maximum.append(list(map(int, input(f"Process {i+1}: ").split())))

available = list(map(int, input("\nEnter Available Resources: ").split()))

need = []
for i in range(n):
    need.append([maximum[i][j] - allocation[i][j] for j in range(m)])

finished = [0] * n
safe_sequence = []

while len(safe_sequence) < n:
    allocated = -1
    for i in range(n):
        if finished[i] == 0 and all(need[i][j] <= available[j] for j in range(m)):
            for j in range(m):
                available[j] += allocation[i][j]
            safe_sequence.append(i + 1)
            finished[i] = 1
            allocated = 1
    if allocated == -1:
        break

if len(safe_sequence) == n:
    print("\nSystem is in a SAFE state.")
    print("Safe Sequence:", " -> ".join(map(str, safe_sequence)))
else:
    print("\nSystem is in an UNSAFE state. Deadlock may occur.")
