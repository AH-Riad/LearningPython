n = int(input("Enter number of processes:"))
timeQuantum = int(input("Enter time quantum:"))

pid = []
at = []
bt = []
remaining_time = []

ct = [0]*n
wt = [0]*n
tat = [0]*n

for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Enter arrival time:")))
    bt_i = int(input("Enter burst time:"))
    bt.append(bt_i)
    remaining_time.append(bt_i)
    
time = 0
done = 0
queue = []
visited = [0]*n

min_at = min(at)
time = min_at

for i in range(n):
    if at[i] == time:
        queue.append(i)
        visited[i] = 1
        
while done<n:
    if len(queue) == 0:
        time +=1
        for i in range(n):
            if at[i]<=time and visited[i] == 0:
                queue.append(i)
                visited[i]=1
    
    idx = queue.pop(0)
    
    if remaining_time[idx]<=timeQuantum:
        time += remaining_time[idx]
        remaining_time[idx]=0
        ct[idx] = time
        done+=1
        
    else:
        remaining_time[idx] -=timeQuantum
        time+= timeQuantum
        
    for i in range(n):
        if at[i]<=time and visited[i]==0:
            queue.append(i)
            visited[i]=1
            
    if remaining_time[idx]>0:
        queue.append(idx)
        
totalTat = 0
totalWt = 0

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    totalTat+=tat[i]
    totalWt+=wt[i]

print("PID\tAT\tBT\tCT\tTAT\tWT\t")
for i in range(n):
    print(f"\n{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\t")

avgTat = totalTat/n
avgWt = totalWt/n
print("Average tat",avgTat)
print("Average wt",avgWt)

