# 🌀 Round Robin CPU Scheduling (Preemptive)

# Step 1: Take inputs
n = int(input("Enter number of processes: "))
time_quantum = int(input("Enter time quantum: "))

pid = []
at = []
bt = []
remaining_time = []

ct = [0]*n   # Completion time
tat = [0]*n  # Turnaround time
wt = [0]*n   # Waiting time

# Step 2: Input process details
for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time: ")))
    bt_i = int(input("Burst time: "))
    bt.append(bt_i)
    remaining_time.append(bt_i)  # Initially remaining = burst

# Step 3: Initialize helper variables
time = 0
done = 0  
queue = []        # Counts how many processes are finished
visited = [0]*n   # Keeps track of which processes have entered queue

# Add the first process to queue (the one that arrives first)
queue.append(0)
visited[0] = 1

# Step 4: Main loop – run until all processes are done
while done < n:
    # 🕒 Case 1: No process has arrived yet (CPU idle)
    if len(queue) == 0:
        time += 1
        for i in range(n):
            if at[i] <= time and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
        continue

    # 🧩 Case 2: Take first process from queue
    idx = queue.pop(0)

    # ⚙️ If the process can finish within time quantum
    if remaining_time[idx] <= time_quantum:
        time += remaining_time[idx]   # CPU runs it completely
        remaining_time[idx] = 0
        ct[idx] = time                # Record its completion time
        done += 1                     # Mark as finished
    else:
        # ⏱ If process still needs more time
        time += time_quantum
        remaining_time[idx] -= time_quantum

    # 🆕 Case 3: Check if new processes arrived during this time
    for i in range(n):
        if at[i] <= time and visited[i] == 0:
            queue.append(i)
            visited[i] = 1

    # 🔁 Case 4: If current process not finished, put it back
    if remaining_time[idx] > 0:
        queue.append(idx)

# Step 5: Calculate Turnaround and Waiting Times
for i in range(n):
    tat[i] = ct[i] - at[i]    # TAT = Completion - Arrival
    wt[i] = tat[i] - bt[i]    # WT = TAT - Burst

# Step 6: Print Results
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
