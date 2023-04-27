---

id: qqs1qwwk1f53cxkxp2yz2pe
title: 用户管理
desc: ''
updated: 1682562443361
created: 1682484159135
---


## 用户(组)管理
- `sudo`

```bash
# Run a command as the superuser:
sudo {{less /var/log/syslog}}

# Edit a file as the superuser with your default editor:
sudo --edit {{/etc/fstab}}

# Run a command as another user and/or group:
sudo --user={{user}} --group={{group}} {{id -a}}

# Repeat the last command prefixed with sudo (only in bash, zsh, etc.):
sudo !!

# Launch the default shell with superuser privileges and run login-specific files (.profile, .bash_profile, etc.):
sudo --login

# Launch the default shell with superuser privileges without changing the environment:
sudo --shell

# Launch the default shell as the specified user, loading the user's environment and reading login-specific files (.profile, .bash_profile, etc.):
sudo --login --user={{user}}

# List the allowed (and forbidden) commands for the invoking user:
sudo --list
```

:::info{title="配置执行特权命令免输入密码"}

```bash
echo "`whoami` ALL=(ALL) NOPASSWD:ALL" | sudo tee "/etc/sudoers.d/dont-prompt-$USER-for-sudo-password"
```
参考：https://zhuanlan.zhihu.com/p/531767015
:::
- `passwd`


```bash
# Change the password of the current user interactively:
passwd

# Change the password of a specific user:
passwd username

# Get the current status of the user:
passwd -S

# Make the password of the account blank (it will set the named account passwordless):
passwd -d
```
- `su`


```bash
# Switch to superuser (requires the root password):
su

# Switch to a given user (requires the user's password):
su username

# Switch to a given user and simulate a full login shell:
su - username

# Execute a command as another user:
su - username -c "command"
```
- `whoami`

```bash
# Display currently logged username:
whoami

# Display the username after a change in the user ID:
sudo whoami
```
- `useradd`

```bash
# Create a new user:
sudo useradd username

# Create a new user with the specified user id:
sudo useradd --uid id username

# Create a new user with the specified shell:
sudo useradd --shell path/to/shell username

# Create a new user belonging to additional groups (mind the lack of whitespace):
sudo useradd --groups group1,group2,... username

# Create a new user with the default home directory:
sudo useradd --create-home username

# Create a new user with the home directory filled by template directory files:
sudo useradd --skel path/to/template_directory --create-home username

# Create a new system user without the home directory:
sudo useradd --system username
```
- `userdel`

```bash
# Remove a user:
sudo userdel username

# Remove a user in other root directory:
sudo userdel --root path/to/other/root username

# Remove a user along with the home directory and mail spool:
sudo userdel --remove username
```
- `adduser`

```bash
# Create a new user with a default home directory and prompt the user to set a password:
adduser username

# Create a new user without a home directory:
adduser --no-create-home username

# Create a new user with a home directory at the specified path:
adduser --home path/to/home username

# Create a new user with the specified shell set as the login shell:
adduser --shell path/to/shell username

# Create a new user belonging to the specified group:
adduser --ingroup group username
```
- `deluser`

```bash
# Remove a user:
sudo deluser username

# Remove a user and their home directory:
sudo deluser --remove-home username

# Remove a user and their home, but backup their files into a `.tar.gz` file in the specified directory:
sudo deluser --backup-to path/to/backup_directory --remove-home username

# Remove a user, and all files owned by them:
sudo deluser --remove-all-files username
```
- `groupadd`

```bash
# Create a new group:
sudo groupadd group_name

# Create a new system group:
sudo groupadd --system group_name

# Create a new group with the specific groupid:
sudo groupadd --gid id group_name
```
- `groupdel`

```bash
# Delete an existing group:
sudo groupdel group_name
```
- `w`

```bash
# Display information about all users who are currently logged in:
w

# Display information about a specific user:
w username

# Display information without including the header:
w --no-header

# Display information without including the login, JCPU and PCPU columns:
w --short
```