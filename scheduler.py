import schedule
import time
import subprocess
import sys
from datetime import datetime

def run_pipeline():
    print(f"\n[Scheduler] Starting pipeline at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    result = subprocess.run(
        [sys.executable, "pipeline.py"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(result.stdout)
        print("[Scheduler] Pipeline completed successfully.")
    else:
        print(result.stderr)
        print("[Scheduler] Pipeline failed. Check logs for details.")

# Run every 1 hour
schedule.every(1).hours.do(run_pipeline)

print("[Scheduler] Starting... Press Ctrl+C to stop.")
print("[Scheduler] Pipeline will run every 1 hour.")
run_pipeline()

while True:
    schedule.run_pending()
    time.sleep(60)