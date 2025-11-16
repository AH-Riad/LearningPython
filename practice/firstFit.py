# First Fit Memory Allocation Algorithm
# Author: Beginner-friendly version

# Input number of memory blocks
n = int(input("Enter number of memory blocks: "))

# Input sizes of each memory block
blocks = list(map(int, input("Enter sizes of each block: ").split()))

# Input number of processes
m = int(input("Enter number of processes: "))

# Input sizes of each process
processes = list(map(int, input("Enter sizes of each process: ").split()))

# Create allocation list to store which block each process gets
allocation = [-1] * m  # -1 means not allocated

# First Fit Allocation
for i in range(m):
    for j in range(n):
        if blocks[j] >= processes[i]:
            allocation[i] = j  # allocate block j to process i
            blocks[j] -= processes[i]  # reduce available memory in block
            break

# Print results
print("\nProcess No.\tProcess Size\tBlock Allocated")
for i in range(m):
    if allocation[i] != -1:
        print(f"P{i+1}\t\t{processes[i]}\t\tB{allocation[i]+1}")
    else:
        print(f"P{i+1}\t\t{processes[i]}\t\tNot Allocated")
