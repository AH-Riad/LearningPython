n = int(input("Enter number of processes:"))

pid = []
at = []
bt = []

remainingTime = []

ct = [0]*n
tat = [0]*n
wt = [0]*n

for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time:")))
    bt_i=int(input("Burst time:"))
    bt.append(bt_i)
    remainingTime.append(bt_i)
    
time = 0
done =0

while done<n:
    idx = -1
    min_remaining = 999999
    
    for i in range(n):
        if at[i]<=time and remainingTime[i]>0:
            if remainingTime[i]<min_remaining:
                min_remaining=remainingTime[i]
                idx =i
                
                
    if idx==-1:
        time+=1
        continue
        
        
    remainingTime[idx]-=1
    time+=1
    
    if remainingTime[idx]==0:
        done+=1
        ct[idx] = time
        tat[idx]=ct[idx]-at[idx]
        wt[idx] = tat[idx] - bt[idx]
        
print("\npID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(f"\n{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
            