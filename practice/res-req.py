# Input number of processes and resources
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

# Input Allocation matrix
print("\nEnter allocation matrix:")
allocation = []
for i in range(n):
    allocation.append(list(map(int, input(f"Process {i+1}: ").split())))

# Input Maximum matrix
print("\nEnter maximum matrix:")
maximum = []
for i in range(n):
    maximum.append(list(map(int, input(f"Process {i+1}: ").split())))

# Input Available resources
available = list(map(int, input("Enter available resources: ").split()))

# Calculate Need matrix
need = []
for i in range(n):
    need.append([maximum[i][j] - allocation[i][j] for j in range(m)])

# Print Need matrix
print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i+1}: {need[i]}")

# Print Available resources
print("\nAvailable Resources:", available)

# Resource request input (0-based process index)
p = int(input(f"\nEnter process making request (0 to {n-1}): "))
req = list(map(int, input(f"Enter request for P{p}: ").split()))
print(f"Request of P{p}: {req}")

# Check if request <= need
if any(req[j] > need[p][j] for j in range(m)):
    print("Error: Request exceeds process's maximum claim.")
else:
    # Check if request <= available
    if any(req[j] > available[j] for j in range(m)):
        print("Resource is not available. Process must wait.")
    else:
        # Tentatively allocate resources
        for j in range(m):
            available[j] -= req[j]
            allocation[p][j] += req[j]
            need[p][j] -= req[j]

        print("\nTentatively allocated resources.")
        print("Available:", available)
        print(f"Allocation for P{p}: {allocation[p]}")
        print(f"Need for P{p}: {need[p]}")

        # Safety algorithm (inline Banker's logic)
        work = available.copy()
        finish = [0] * n  # 0 = not finished, 1 = finished
        safe_seq = []

        while len(safe_seq) < n:
            allocated = -1  # Track if a process is allocated in this pass
            for i in range(n):
                if finish[i] == 0 and all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = 1
                    safe_seq.append(i)
                    allocated = i  # Process allocated
                    break
            if allocated == -1:
                break  # No process could be allocated, exit

        # Check safe state
        if len(safe_seq) == n:
            print("\nRequest can be granted. System is in SAFE state.")
            print("Safe sequence:", " -> ".join(f"P{i}" for i in safe_seq))
        else:
            print("\nRequest CANNOT be granted. System would be unsafe.")
            # Rollback
            for j in range(m):
                available[j] += req[j]
                allocation[p][j] -= req[j]
                need[p][j] += req[j]

print("\nFinal available resources:", available)
