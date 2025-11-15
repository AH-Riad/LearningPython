n = int(input("Enter number of processes:"))

pid = []
at = []
bt = []
priority = []

ct = [0]*n
tat = [0]*n
wt = [0]*n
remainingTime = []

for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Enter arrival time:")))
    bt_i = int(input("Enter burst time:"))
    bt.append(bt_i)
    remainingTime.append(bt_i)
    priority.append(int(input("Enter priority (Lowest number = Highest priority):")))
    
time = 0
done = 0

while done < n:
    idx = -1
    highestPriority = 999999

    for i in range(n):
        if at[i] <= time and remainingTime[i] > 0:
            if priority[i] < highestPriority:
                highestPriority = priority[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    remainingTime[idx] -= 1
    time += 1

    if remainingTime[idx] == 0:
        ct[idx] = time
        done += 1

# Calculate TAT & WT
total_tat = 0
total_wt = 0

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    total_tat += tat[i]
    total_wt += wt[i]

avg_tat = total_tat / n
avg_wt = total_wt / n

print("\nPID\tAT\tBT\tPRI\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
print(f"Average Waiting Time = {avg_wt:.2f}")
