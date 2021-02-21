from collections import deque

jobs = [int(job) for job in input().split(', ')]
job_index = int(input())

clock_cycle = 0
counter = 0
my_job = jobs[job_index]

jobs_before_my_job = jobs[:job_index]

for i in range(len(jobs_before_my_job)):
    if jobs_before_my_job[i] == jobs[job_index]:
        counter += 1

sorted_jobs = sorted(jobs)
jobs_queue = deque(sorted_jobs)

while jobs_queue:
    task = jobs_queue.popleft()
    clock_cycle += task
    if task == jobs[job_index]:
        if counter == 0:
            break
        else:
            counter -= 1

print(clock_cycle)




