---

id: 66gcnq88v4ivqgackachqsj
title: 进程管理
desc: ''
updated: 1682562443285
created: 1682484168205
---


## 进程管理
- `ps`

```bash
# List all running processes:
ps aux

# List all running processes including the full command string:
ps auxww

# Search for a process that matches a string:
ps aux | grep string

# List all processes of the current user in extra full format:
ps --user $(id -u) -F

# List all processes of the current user as a tree:
ps --user $(id -u) f

# Get the parent PID of a process:
ps -o ppid= -p pid

# Sort processes by memory consumption:
ps --sort size
```
- `top`

```bash
# Start top:
top

# Do not show any idle or zombie processes:
top -i

# Show only processes owned by given user:
top -u username

# Sort processes by a field:
top -o field_name

# Show the individual threads of a given process:
top -Hp process_id

# Show only the processes with the given PID(s), passed as a comma-separated list. (Normally you wouldn't know PIDs off hand. This example picks the PIDs from the process name):
top -p $(pgrep -d ',' process_name)

# Get help about interactive commands:
?
```
- `htop`


```bash
# Start htop:
htop

# Start htop displaying processes owned by a specific user:
htop --user username

# Sort processes by a specified `sort_item` (use `htop --sort help` for available options):
htop --sort sort_item

# See interactive commands while running htop:
?

# Switch to a different tab:
tab

# Display help:
htop --help
```
- `kill`

```bash
# Terminate a program using the default SIGTERM (terminate) signal:
kill process_id

# List available signal names (to be used without the `SIG` prefix):
kill -l

# Terminate a background job:
kill %job_id

# Terminate a program using the SIGHUP (hang up) signal. Many daemons will reload instead of terminating:
kill -1|HUP process_id

# Terminate a program using the SIGINT (interrupt) signal. This is typically initiated by the user pressing `Ctrl + C`:
kill -2|INT process_id

# Signal the operating system to immediately terminate a program (which gets no chance to capture the signal):
kill -9|KILL process_id

# Signal the operating system to pause a program until a SIGCONT ("continue") signal is received:
kill -17|STOP process_id

# Send a `SIGUSR1` signal to all processes with the given GID (group id):
kill -SIGUSR1 -group_id
```
- `pkill`


```bash
# Kill all processes which match:
pkill "process_name"

# Kill all processes which match their full command instead of just the process name:
pkill -f "command_name"

# Force kill matching processes (can't be blocked):
pkill -9 "process_name"

# Send SIGUSR1 signal to processes which match:
pkill -USR1 "process_name"

# Kill the main `firefox` process to close the browser:
pkill --oldest "firefox"
```
- `fg`


```bash
# Bring most recently suspended or running background job to foreground:
fg

# Bring a specific job to foreground:
fg %job_id
```
- `bg`


```bash
# Resume the most recently suspended job and run it in the background:
bg

# Resume a specific job (use `jobs -l` to get its ID) and run it in the background:
bg %job_id
```
- `nohup`

```bash
# Run a process that can live beyond the terminal:
nohup command argument1 argument2 ...

# Launch `nohup` in background mode:
nohup command argument1 argument2 ... &

# Run a shell script that can live beyond the terminal:
nohup path/to/script.sh &

# Run a process and write the output to a specific file:
nohup command argument1 argument2 ... > path/to/output_file &
```
- `jobs`

```bash
# View jobs spawned by the current shell:
jobs

# List jobs and their process IDs:
jobs -l

# Display information about jobs with changed status:
jobs -n

# Display process ID of process group leader:
jobs -p

# Display running processes:
jobs -r

# Display stopped processes:
jobs -s
```