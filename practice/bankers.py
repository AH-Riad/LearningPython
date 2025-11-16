n = int(input("Enter number of processes:"))
m = int(input("Enter number of resources:"))

print("\nEnter allocation matrix:")
allocation = []
for i in range (n):
    allocation.append(list(map(int,input(f"process{i+1}:").split())))
    
print("\nEnter maximum matrix:")
maximum = []
for i in range(n):
    maximum.append(list(map(int, input(f"Process {i+1}:").split())))
    
available = list(map(int, input("Enter available matrix:").split()))

need = []
for i in range(n):
    need.append([maximum[i][j] - allocation[i][j] for j in range(m)])


finished = [0]*n
safeSequence = []

while len(safeSequence)<n:
    allocated = -1
    for i in range(n):
        if finished[i] == 0 and all(need[i][j]<=available[j] for j in range(m)):
            for j in range(m):
                available[j]+=allocation[i][j]
            safeSequence.append(i+1)
            finished[i] = 1
            allocated = 1
            
    if allocated == -1:
        break
    
    
if len(safeSequence) ==n:
    print("Process is in safe state")
    print("Safe sequenece = ","->".join(map(str,safeSequence)))
else:
    print("The process is not in safe state")
            
        