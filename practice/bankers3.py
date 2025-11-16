n = int(input("Enter number of processes:"))
m = int(input("Enter number of resources:"))

print("\nEnter allocation matrix:")
allocation = []
for i in range (n):
    allocation.append(list(map(int, input(f"process{i+1}:").split())))
    
print("\nEnter maximum matrix:")
maximum = []
for i in range(n):
    maximum.append(list(map(int, input(f"process{i+1}:").split())))
    
    
available = list(map(int, input("Enter available resources:").split()))

need = []
for i in range (n):
    need.append([ maximum[i][j]-allocation[i][j] for j in range(m)])
    
    
finish = [0]*n
safe_seq = []

while len(safe_seq)<n:
    allocated = -1
    if finish[i]==0 and all(need[i][j]<=available[j] for j in range(m)):
        for j in range(m):
            available[j]+=allocated[i][j]
            
        finish[i]=1
        safe_seq.append(i+1)
        allocated = 1
    
    if allocated == -1:
        break
    
if len(safe_seq)==n:
    print("Process is in safe state:")
    print("Safe_seq =".join(map(str,safe_seq)))
    
else:
    print("Unsafe state")