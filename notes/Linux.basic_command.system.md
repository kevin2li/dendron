---
id: smsc2zak0yttsp23ll0tjen
title: system
desc: ''
updated: 1682504081926
created: 1682484260711
---


## 系统管理
- `reboot`

```bash
# Reboot the system:
reboot

# Power off the system (same as `poweroff`):
reboot --poweroff

# Halt the system (same as `halt`):
reboot --halt

# Reboot immediately without contacting the system manager:
reboot --force

# Write the wtmp shutdown entry without rebooting the system:
reboot --wtmp-only
```
- `shutdown`
```bash
# Power off (halt) immediately:
shutdown -h now

# Reboot immediately:
shutdown -r now

# Reboot in 5 minutes:
shutdown -r +5 &

# Shutdown at 1:00 pm (Uses 24h clock):
shutdown -h 13:00

# Cancel a pending shutdown/reboot operation:
shutdown -c
```
- `poweroff`
```bash
# Power off the system:
poweroff

# Halt the system (same as `halt`):
poweroff --halt

# Reboot the system (same as `reboot`):
poweroff --reboot

# Shut down immediately without contacting the system manager:
poweroff --force --force

# Write the wtmp shutdown entry without shutting down the system:
poweroff --wtmp-only
```
- `halt`

```bash
# Halt the system:
halt

# Power off the system (same as `poweroff`):
halt --poweroff

# Reboot the system (same as `reboot`):
halt --reboot

# Halt immediately without contacting the system manager:
halt --force --force

# Write the wtmp shutdown entry without halting the system:
halt --wtmp-only
```
- `uname`

```bash
# Print all information:
uname --all

# Print the current kernel name:
uname --kernel-name

# Print the current network node host name:
uname --nodename

# Print the current kernel release:
uname --kernel-release

# Print the current kernel version:
uname --kernel-version

# Print the current machine hardware name:
uname --machine

# Print the current processor type:
uname --processor

# Print the current operating system name:
uname --operating-system
```
- `neofetch`

```bash
# Return the default config, and create it if it's the first time the program runs:
neofetch

# Trigger an info line from appearing in the output, where 'infoname' is the function name in the config file, e.g. memory:
neofetch --enable|disable infoname

# Hide/Show OS architecture:
neofetch --os_arch on|off

# Enable/Disable CPU brand in output:
neofetch --cpu_brand on|off
```
- `systemctl`

```bash
# Show all running services:
systemctl status

# List failed units:
systemctl --failed

# Start/Stop/Restart/Reload a service:
systemctl start|stop|restart|reload unit

# Show the status of a unit:
systemctl status unit

# Enable/Disable a unit to be started on bootup:
systemctl enable|disable unit

# Mask/Unmask a unit to prevent enablement and manual activation:
systemctl mask|unmask unit

# Reload systemd, scanning for new or changed units:
systemctl daemon-reload

# Check if a unit is enabled:
systemctl is-enabled unit
```