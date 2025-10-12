n = int(input("Enter number of processes:"))
timeQuantum = int(input("Enter time quantum:"))

pid = []
at = []
bt = []

remainingTime = []

ct = [0]*n
tat = [0]*n
wt = [0]*n

for i in range(n):
    print(f"\nEnter process {i+1} details: ")
    pid.append(i+1)
    at.append(int(input("Arrival time:")))
    bt_i = int(input("Bust time:"))
    bt.append(bt_i)
    remainingTime.append(bt_i)
    
    
time = 0
done = 0
queue =[]
visited =[0]*n



queue.append(0)
visited[0] = 1


while done<n:
    if len(queue)==0:
        time+=1
        
        
        for i in range(n):
            if at[i]<=time and visited[i]==0:
                queue.append(i)
                visited[i]=1
                
        continue
    
    
    idx = queue.pop[0]
    
    if(remainingTime[idx]<=timeQuantum):
        done+=1
        time+=remainingTime
        ct[idx] = time
        remainingTime[idx]=0
        
    else:
        time+=timeQuantum
        remainingTime[idx]-=timeQuantum
        
    for i in range(n):
        if at[i]<=time and visited[i]==0:
            queue.append(i)
            visited[i]=1
            
    if remainingTime[idx]>timeQuantum:
        queue.append(idx)
        
        
for i in range(n):
    tat[i] = ct[i] - at[i]    # TAT = Completion - Arrival
    wt[i] = tat[i] - bt[i]    # WT = TAT - Burst

# Step 6: Print Results
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
