n = int(input("Enter number of processes:"))

pid = []
at = []
bt =[]

ct= [0]*n
tat=[0]*n
wt=[0]*n

for i in range(n):
    print(f"\nProcess {i+1} details: ")
    pid.append(i+1)
    at.append(int(input("Arrival time :")))
    bt.append(int(input("Burst time :")))
    
    
for i in range(n-1):
    for j in range(i+1, n):
        if at[i]>at[j]:
            at[i],at[j]=at[j],at[i]
            bt[i],bt[j]=bt[j],bt[i]
            pid[i],pid[j]=pid[j],pid[i]
            
ct[0] = at[0]+bt[0]

for i in range(1, n):
    if at[i]>ct[i-1]:
        ct[i] = at[i]+bt[i]
    else:
        ct[i] = ct[i-1]+bt[i]
        
        
for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i] = tat[i]-bt[i]
    
    
    
print("\nP#\tAT\tBT\tCT\tTAT\tWT") 
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
