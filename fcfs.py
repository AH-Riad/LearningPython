# 🔹 FCFS (First Come First Serve) Scheduling Algorithm with Arrival Time

# Step 1: Take number of processes as input
n = int(input("Enter number of processes: "))

# Step 2: Create empty lists to store data
pid = []           # Process IDs
at = []            # Arrival Times
bt = []            # Burst Times
ct = [0] * n       # Completion Times (initially all 0)
tat = [0] * n      # Turnaround Times
wt = [0] * n       # Waiting Times

# Step 3: Input process details one by one
for i in range(n):
    print(f"\nProcess {i + 1} details:")
    pid.append(i + 1)                         # Process ID (P1, P2, ...)
    at.append(int(input("Arrival Time: ")))   # Arrival Time
    bt.append(int(input("Burst Time: ")))     # Burst Time

# Step 4: Sort all processes by their Arrival Time (smallest first)
# Using a simple nested loop (like bubble sort)
for i in range(n - 1):
    for j in range(i + 1, n):
        if at[i] > at[j]:
            # Swap Arrival Time
            at[i], at[j] = at[j], at[i]
            # Swap Burst Time to keep aligned with the correct process
            bt[i], bt[j] = bt[j], bt[i]
            # Swap Process ID as well
            pid[i], pid[j] = pid[j], pid[i]

# Step 5: Calculate Completion Time (CT) for each process
# The first process completes after its arrival + burst time
ct[0] = at[0] + bt[0]

# For the rest of the processes:
for i in range(1, n):
    if at[i] > ct[i - 1]:
        # CPU is idle until the next process arrives
        ct[i] = at[i] + bt[i]
    else:
        # CPU continues immediately after the previous process
        ct[i] = ct[i - 1] + bt[i]

# Step 6: Calculate Turnaround Time (TAT) and Waiting Time (WT)
for i in range(n):
    tat[i] = ct[i] - at[i]   # TAT = Completion - Arrival
    wt[i] = tat[i] - bt[i]   # WT = Turnaround - Burst

# Step 7: Print final table of results
print("\nP#\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

# Step 8 (optional): Calculate and print average times
avg_tat = sum(tat) / n
avg_wt = sum(wt) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
