# Round Robin CPU Scheduling (Preemptive)

n = int(input("Enter number of processes: "))
timeQuantum = int(input("Enter time quantum: "))

pid = []
at = []
bt = []
remainingTime = []

ct = [0]*n
tat = [0]*n
wt = [0]*n

# Input process details
for i in range(n):
    print(f"\nEnter process {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time: ")))
    bt_i = int(input("Burst time: "))
    bt.append(bt_i)
    remainingTime.append(bt_i)

time = 0
done = 0
queue = []
visited = [0]*n

# Add first process to queue (which arrives first)
queue.append(0)
visited[0] = 1

while done < n:
    # If queue is empty, increase time until a process arrives
    if len(queue) == 0:
        time += 1
        for i in range(n):
            if at[i] <= time and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
        continue

    # Take the first process from the queue
    idx = queue.pop(0)

    # Execute the process for timeQuantum or until it finishes
    if remainingTime[idx] <= timeQuantum:
        time += remainingTime[idx]
        remainingTime[idx] = 0
        ct[idx] = time
        done += 1
    else:
        time += timeQuantum
        remainingTime[idx] -= timeQuantum

    # Add all processes that have arrived by this time
    for i in range(n):
        if at[i] <= time and visited[i] == 0:
            queue.append(i)
            visited[i] = 1

    # If current process not finished, put it back into queue
    if remainingTime[idx] > 0:
        queue.append(idx)

# Calculate Turnaround and Waiting Times
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# Print Results
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
