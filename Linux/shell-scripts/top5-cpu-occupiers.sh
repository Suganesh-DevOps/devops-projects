# Write a script to display the top 5 CPU-consuming processes.

#!/bin/bash

echo "Top 5 CPU eaters"

ps -eo pid,ppid,CMD,%cpu,%mem --sort=-%cpu | head -n 6
