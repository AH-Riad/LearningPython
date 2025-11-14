n = int(input("Enter number of processes:"))

pid = []
at = []
bt = []
priority = []

ct = [0]*n
tat = [0]*n
wt = [0]*n
completed = [0]*n

for i in range (n):
    print(f"\nProcess{i+1} details:")
    pid.append(i+1)
    at.append(int(input("Enter arrival time:")))
    bt.append(int(input("Enter burst time:")))
    priority.append(int(input("Enter priority(lower number  = higher priority):")))
    
time = 0
done = 0

while done<n:
    idx = -1
    min_priority = 999999
    
    for i in range(n):
        if at[i] <= time and completed[i]==0:
            if priority[i]<min_priority:
                min_priority = priority[i]
                idx = i
                
    if idx == -1:
        time+=1
        continue
    
    time += bt[idx]
    ct[idx] = time
    done+=1
    completed[idx] =1
    
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    
print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
            
    