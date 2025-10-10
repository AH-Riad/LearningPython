# Input number of processes
n = int(input("Enter number of processes: "))

# Lists to store process info
pid = []
at = []
bt = []
priority = []

# Lists for results
ct = [0]*n
tat = [0]*n
wt = [0]*n
completed = [0]*n  # 0 = not completed, 1 = completed

# Input process details
for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))
    priority.append(int(input("Priority (lower number = higher priority): ")))

# Initialize CPU time and completed count
time = 0
done = 0

while done < n:
    idx = -1
    highest_priority = 999999  # start with large number

    # Find process with highest priority that has arrived
    for i in range(n):
        if at[i] <= time and completed[i] == 0:
            if priority[i] < highest_priority:
                highest_priority = priority[i]
                idx = i

    # If no process has arrived, increment time
    if idx == -1:
        time += 1
        continue

    # Run the selected process
    time += bt[idx]
    ct[idx] = time
    completed[idx] = 1
    done += 1

# Calculate TAT and WT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# Display the final table
print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
