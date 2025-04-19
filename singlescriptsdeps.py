# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "rich",
# ]
# ///
import time
from rich.progress import track

for i in track(range(20), description="For example:"):
    time.sleep(0.05)

