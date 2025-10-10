n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []

for i in range(n):
    print(f"\nProcess {i+1} details:")
    pid.append(i + 1)
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))

# Copy burst times because we'll decrease remaining times
remaining_time = bt.copy()

ct = [0]*n   # Completion time
tat = [0]*n  # Turnaround time
wt = [0]*n   # Waiting time

time = 0
completed = 0
min_bt = 99999
shortest = -1
check = False

# Continue until all processes are completed
while completed != n:
    # Find process with minimum remaining time among arrived ones
    for i in range(n):
        if at[i] <= time and remaining_time[i] > 0:
            if remaining_time[i] < min_bt:
                min_bt = remaining_time[i]
                shortest = i
                check = True

    if not check:
        time += 1
        continue

    # Decrease remaining time for selected process
    remaining_time[shortest] -= 1
    min_bt = remaining_time[shortest]
    
    if min_bt == 0:
        min_bt = 99999

    # If process finishes
    if remaining_time[shortest] == 0:
        completed += 1
        check = False
        finish_time = time + 1
        ct[shortest] = finish_time
        tat[shortest] = ct[shortest] - at[shortest]
        wt[shortest] = tat[shortest] - bt[shortest]
    
    # Move time forward by 1 unit
    time += 1

# Display results
print("\nP#\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
