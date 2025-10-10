n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []

ct = [0]*n
tat = [0]*n
wt = [0]*n
completed = [0]*n  # keeps track of finished processes

for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i+1)
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))

time = 0
done = 0

while done < n:
    idx = -1
    min_bt = 999999

    # find process with min burst among arrived ones
    for i in range(n):
        if at[i] <= time and completed[i] == 0:
            if bt[i] < min_bt:
                min_bt = bt[i]
                idx = i

    if idx == -1:
        # No process has arrived yet
        time += 1
        continue

    # run selected process
    time += bt[idx]
    ct[idx] = time
    completed[idx] = 1
    done += 1

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nP#\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
