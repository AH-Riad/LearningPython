n = int(input("Enter number of processes:"))

pid = []
at = []
bt = []
priority = []

ct = [0]*n
tat = [0]*n
wt = [0]*n
completed = [0]*n


for i in range(n):
    print(f"\nEnter process {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time:")))
    bt.append(int(input("burst time:")))
    priority.append(int(input("Priority(Lower number = Higher priority):")))
    
    
time = 0
done = 0

while done<n:
    idx = -1
    h_p = 999999
    
    for i in range(n):
        if at[i]<=time and completed[i] == 0:
            if priority[i]<h_p:
                h_p = priority[i]
                idx = i
                
                
    if idx == -1:
        time+=1
        continue
    
    
    time += bt[idx]
    ct[idx] =time
    completed[idx] =1
    done+=1
            
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
