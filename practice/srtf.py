n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []
remainingTime = []

# Input
for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at_i = int(input("Enter arrival time: "))
    bt_i = int(input("Enter burst time: "))
    at.append(at_i)
    bt.append(bt_i)
    remainingTime.append(bt_i)

# Sort processes by arrival time (important)
processes = list(zip(pid, at, bt, remainingTime))
processes.sort(key=lambda x: x[1])  # sort by AT

pid, at, bt, remainingTime = map(list, zip(*processes))

ct = [0] * n
tat = [0] * n
wt = [0] * n

time = 0
done = 0

while done < n:
    idx = -1
    minRemaining = 99999

    # find process available with shortest remaining time
    for i in range(n):
        if at[i] <= time and remainingTime[i] > 0:
            if remainingTime[i] < minRemaining:
                minRemaining = remainingTime[i]
                idx = i

    # no process available, move time forward
    if idx == -1:
        time += 1
        continue

    # Run process for 1 unit of time
    remainingTime[idx] -= 1
    time += 1

    # when process completes
    if remainingTime[idx] == 0:
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        done += 1

# Output
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

# Averages
avg_tat = sum(tat) / n
avg_wt = sum(wt) / n

print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
print(f"Average Waiting Time = {avg_wt:.2f}")
