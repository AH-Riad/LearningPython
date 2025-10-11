n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []
priority = []

# Copy burst times for calculation
remaining_time = []

ct = [0]*n
tat = [0]*n
wt = [0]*n

# Input process details
for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time: ")))
    bt_i = int(input("Burst time: "))
    bt.append(bt_i)
    remaining_time.append(bt_i)
    priority.append(int(input("Priority (lower number = higher priority): ")))

time = 0
done = 0

while done < n:
    idx = -1
    highest_priority = 999999

    # Find process with highest priority among arrived and not finished
    for i in range(n):
        if at[i] <= time and remaining_time[i] > 0:
            if priority[i] < highest_priority:
                highest_priority = priority[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    # Run process for 1 unit
    remaining_time[idx] -= 1
    time += 1

    # If process finished
    if remaining_time[idx] == 0:
        done += 1
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]

# Display final table
print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
