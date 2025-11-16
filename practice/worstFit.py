# Worst Fit Memory Allocation Algorithm
# Author: Beginner-friendly version

# Input number of memory blocks
n = int(input("Enter number of memory blocks: "))

# Input sizes of each memory block
blocks = list(map(int, input("Enter sizes of each block: ").split()))

# Input number of processes
m = int(input("Enter number of processes: "))

# Input sizes of each process
processes = list(map(int, input("Enter sizes of each process: ").split()))

# Create allocation list
allocation = [-1] * m

# Worst Fit Allocation
for i in range(m):
    worst_index = -1
    for j in range(n):
        if blocks[j] >= processes[i]:
            if worst_index == -1 or blocks[j] > blocks[worst_index]:
                worst_index = j
    if worst_index != -1:
        allocation[i] = worst_index
        blocks[worst_index] -= processes[i]

# Print results
print("\nProcess No.\tProcess Size\tBlock Allocated")
for i in range(m):
    if allocation[i] != -1:
        print(f"P{i+1}\t\t{processes[i]}\t\tB{allocation[i]+1}")
    else:
        print(f"P{i+1}\t\t{processes[i]}\t\tNot Allocated")
