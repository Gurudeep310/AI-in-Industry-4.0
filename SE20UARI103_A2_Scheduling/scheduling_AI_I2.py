def calculate_waiting_and_turnaround_times(processes_info, num_processes, burst_times, waiting_times, turnaround_times):
    # FCFS algorithm
    waiting_times[0] = 0
    for i in range(1, num_processes):
        waiting_times[i] = burst_times[i - 1] + waiting_times[i - 1]

    for i in range(num_processes):
        turnaround_times[i] = burst_times[i] + waiting_times[i]

def find_waiting_and_turnaround_times_shortest_job_first(processes_info, num_processes, burst_times):
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    remaining_burst_times = burst_times.copy()
    current_time = 0

    while True:
        done = True

        # Find the process with the shortest remaining burst time
        min_burst_time = float('inf')
        shortest_process_index = -1

        for i in range(num_processes):
            if remaining_burst_times[i] > 0 and processes_info[i][1] <= current_time:
                if remaining_burst_times[i] < min_burst_time:
                    shortest_process_index = i
                    min_burst_time = remaining_burst_times[i]

        # If no process is found, break the loop
        if shortest_process_index == -1:
            break

        # Update time and remaining burst time for the chosen process
        current_time += min_burst_time
        remaining_burst_times[shortest_process_index] -= min_burst_time
        waiting_times[shortest_process_index] = current_time - processes_info[shortest_process_index][1]
        turnaround_times[shortest_process_index] = waiting_times[shortest_process_index] + burst_times[shortest_process_index]

    return waiting_times, turnaround_times

def find_waiting_and_turnaround_times_priority_scheduling(processes_info, num_processes, burst_times):
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    remaining_burst_times = burst_times.copy()
    current_time = 0

    while True:
        done = True

        # Find the process with the highest priority
        max_priority = -1
        highest_priority_process_index = -1

        for i in range(num_processes):
            if remaining_burst_times[i] > 0 and processes_info[i][1] <= current_time:
                if processes_info[i][2] > max_priority:
                    highest_priority_process_index = i
                    max_priority = processes_info[i][2]

        # If no process is found, break the loop
        if highest_priority_process_index == -1:
            break

        # Update time and remaining burst time for the chosen process
        current_time += 1
        remaining_burst_times[highest_priority_process_index] -= 1
        waiting_times[highest_priority_process_index] = current_time - processes_info[highest_priority_process_index][1]
        turnaround_times[highest_priority_process_index] = waiting_times[highest_priority_process_index] + burst_times[highest_priority_process_index]

    return waiting_times, turnaround_times

def find_waiting_and_turnaround_times_round_robin(processes_info, num_processes, burst_times, time_quantum=4):
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    remaining_burst_times = burst_times.copy()
    current_time = 0

    while True:
        done = True

        for i in range(num_processes):
            if remaining_burst_times[i] > 0:
                done = False

                if remaining_burst_times[i] > time_quantum:
                    current_time += time_quantum
                    remaining_burst_times[i] -= time_quantum
                else:
                    current_time += remaining_burst_times[i]
                    waiting_times[i] = current_time - processes_info[i][1]
                    remaining_burst_times[i] = 0
                    turnaround_times[i] = waiting_times[i] + burst_times[i]

        if done:
            break

    return waiting_times, turnaround_times

def main():
    # Process information: (Patient Name, Arrival Time, Burst Time, Priority)
    processes_info = [("A", 0, 30, 3), ("B", 10, 20, 5), ("C", 15, 40, 2), ("D", 20, 15, 4)]
    num_processes = len(processes_info)
    burst_times = [process[2] for process in processes_info]

    # Initialize waiting_time and turnaround_time arrays
    waiting_times_fcfs = [0] * num_processes
    turnaround_times_fcfs = [0] * num_processes

    waiting_times_sjf = [0] * num_processes
    turnaround_times_sjf = [0] * num_processes

    waiting_times_priority = [0] * num_processes
    turnaround_times_priority = [0] * num_processes

    waiting_times_rr = [0] * num_processes
    turnaround_times_rr = [0] * num_processes

    # Calculate waiting times and turnaround times for each algorithm
    calculate_waiting_and_turnaround_times(processes_info, num_processes, burst_times, waiting_times_fcfs, turnaround_times_fcfs)
    waiting_times_sjf, turnaround_times_sjf = find_waiting_and_turnaround_times_shortest_job_first(processes_info, num_processes, burst_times)
    waiting_times_priority, turnaround_times_priority = find_waiting_and_turnaround_times_priority_scheduling(processes_info, num_processes, burst_times)
    waiting_times_rr, turnaround_times_rr = find_waiting_and_turnaround_times_round_robin(processes_info, num_processes, burst_times)

    # Calculate average waiting time and average turnaround time
    avg_waiting_time_fcfs = sum(waiting_times_fcfs) / num_processes
    avg_turnaround_time_fcfs = sum(turnaround_times_fcfs) / num_processes

    avg_waiting_time_sjf = sum(waiting_times_sjf) / num_processes
    avg_turnaround_time_sjf = sum(turnaround_times_sjf) / num_processes

    avg_waiting_time_priority = sum(waiting_times_priority) / num_processes
    avg_turnaround_time_priority = sum(turnaround_times_priority) / num_processes

    avg_waiting_time_rr = sum(waiting_times_rr) / num_processes
    avg_turnaround_time_rr = sum(turnaround_times_rr) / num_processes

    # Display results
    print("First-Come, First-Served (FCFS):")
    for i in range(num_processes):
        print(f"{processes_info[i][0]} - Waiting Time: {waiting_times_fcfs[i]} minutes, Turnaround Time: {turnaround_times_fcfs[i]} minutes")

    print(f"Average Waiting Time: {avg_waiting_time_fcfs} minutes")
    print(f"Average Turnaround Time: {avg_turnaround_time_fcfs} minutes")
    print()

    print("Shortest Job First (SJF):")
    for i in range(num_processes):
        print(f"{processes_info[i][0]} - Waiting Time: {waiting_times_sjf[i]} minutes, Turnaround Time: {turnaround_times_sjf[i]} minutes")

    print(f"Average Waiting Time: {avg_waiting_time_sjf} minutes")
    print(f"Average Turnaround Time: {avg_turnaround_time_sjf} minutes")
    print()

    print("Priority Scheduling:")
    for i in range(num_processes):
        print(f"{processes_info[i][0]} - Waiting Time: {waiting_times_priority[i]} minutes, Turnaround Time: {turnaround_times_priority[i]} minutes")

    print(f"Average Waiting Time: {avg_waiting_time_priority} minutes")
    print(f"Average Turnaround Time: {avg_turnaround_time_priority} minutes")
    print()

    print("Round Robin (Time Quantum = 4):")
    for i in range(num_processes):
        print(f"{processes_info[i][0]} - Waiting Time: {waiting_times_rr[i]} minutes, Turnaround Time: {turnaround_times_rr[i]} minutes")

    print(f"Average Waiting Time: {avg_waiting_time_rr} minutes")
    print(f"Average Turnaround Time: {avg_turnaround_time_rr} minutes")

if __name__ == "__main__":
    main()
