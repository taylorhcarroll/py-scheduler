import schedule

def job():
    print("A simple Python scheduler")

# do() specifies the job_func that should be called every time the job runs
schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()