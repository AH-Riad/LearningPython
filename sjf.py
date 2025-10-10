# Shortest Job First (Non-Preemptive) Scheduling

# Step 1: Take number of processes
n = int(input("Enter number of processes: "))

# Step 2: Create empty lists
pid = []     # Process ID
at = []      # Arrival Time
bt = []      # Burst Time
ct = [0]*n   # Completion Time
tat = [0]*n  # Turnaround Time
wt = [0]*n   # Waiting Time
done = [0]*n # To mark finished processes

# Step 3: Take input
for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))

# Step 4: Initialize time and completed process count
time = 0
completed = 0

# Step 5: Keep running until all processes are done
while completed < n:
    # Find process with smallest burst time among arrived ones
    min_bt = 9999
    idx = -1

    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if bt[i] < min_bt:
                min_bt = bt[i]
                idx = i

    if idx == -1:
        # No process has arrived yet — CPU idle
        time += 1
    else:
        # Process found — run it completely
        time += bt[idx]
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        done[idx] = 1
        completed += 1

# Step 6: Print results
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

# Step 7: Print average times
avg_tat = sum(tat)/n
avg_wt = sum(wt)/n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
