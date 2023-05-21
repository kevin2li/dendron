# 常用命令
## 终端
- `echo`

```bash
# Print a text message. Note: quotes are optional:
echo "Hello World"

# Print a message with environment variables:
echo "My path is $PATH"

# Print a message without the trailing newline:
echo -n "Hello World"

# Append a message to the file:
echo "Hello World" >> file.txt

# Enable interpretation of backslash escapes (special characters):
echo -e "Column 1\tColumn 2"
```
<!-- more -->

- `clear`

```bash
# Clear the screen (equivalent to pressing Control-L in Bash shell):
clear

# Clear the screen but keep the terminal's scrollback buffer:
clear -x

# Indicate the type of terminal to clean (defaults to the value of the environment variable `TERM`):
clear -T type_of_terminal

# Show the version of `ncurses` used by `clear`:
clear -V
```
- `reset`

```bash
# Reinitialize the current terminal:
reset

# Display the terminal type instead:
reset -q
```
- `history`

```bash
# Display the commands history list with line numbers:
history

# Display the last 20 commands (in `zsh` it displays all commands starting from the 20th):
history 20

# Clear the commands history list (only for current `bash` shell):
history -c

# Overwrite history file with history of current `bash` shell (often combined with `history -c` to purge history):
history -w

# Delete the history entry at the specified offset:
history -d offset
```
- `tee`

```bash
# Copy standard input to each file, and also to standard output:
echo "example" | tee path/to/file

# Append to the given files, do not overwrite:
echo "example" | tee -a path/to/file

# Print standard input to the terminal, and also pipe it into another program for further processing:
echo "example" | tee /dev/tty | xargs printf "[%s]"

# Create a directory called "example", count the number of characters in "example" and write "example" to the terminal:
echo "example" | tee >(xargs mkdir) >(wc -c)
```

## 文件管理
### 查看、切换、新建、移动、复制、重命名、删除、链接
- `ls`

```bash
# List files one per line:
ls -1

# List all files, including hidden files:
ls -a

# List all files, with trailing `/` added to directory names:
ls -F

# Long format list (permissions, ownership, size, and modification date) of all files:
ls -la

# Long format list with size displayed using human-readable units (KiB, MiB, GiB):
ls -lh

# Long format list sorted by size (descending):
ls -lS

# Long format list of all files, sorted by modification date (oldest first):
ls -ltr

# Only list directories:
ls -d */

```
- `pwd`

```bash
# Print the current directory:
pwd

# Print the current directory, and resolve all symlinks (i.e. show the "physical" path):
pwd --physical

# Print the current logical directory:
pwd --logical
```
- `cd`

```bash
# Go to the specified directory:
cd path/to/directory

# Go up to the parent of the current directory:
cd ..

# Go to the home directory of the current user:
cd

# Go to the home directory of the specified user:
cd ~username

# Go to the previously chosen directory:
cd -

# Go to the root directory:
cd /
```
- `mkdir`

```bash
# Create specific directories:
mkdir path/to/directory1 path/to/directory2 ...

# Create specific directories and their [p]arents if needed:
mkdir -p path/to/directory1 path/to/directory2 ...

# Create directories with specific permissions:
mkdir -m rwxrw-r-- path/to/directory1 path/to/directory2 ...
```
- `touch`

```bash
# Create specific files:
touch path/to/file1 path/to/file2 ...

# Set the file [a]ccess or [m]odification times to the current one and don't [c]reate file if it doesn't exist:
touch -c -a|m path/to/file1 path/to/file2 ...

# Set the file [t]ime to a specific value and don't [c]reate file if it doesn't exist:
touch -c -t YYYYMMDDHHMM.SS path/to/file1 path/to/file2 ...

# Set the file time of a specific file to the time of anothe[r] file and don't [c]reate file if it doesn't exist:
touch -c -r ~/.emacs path/to/file1 path/to/file2 ...
```
- `rm`

```bash
# Remove specific files:
rm path/to/file1 path/to/file2 ...

# Remove specific files ignoring nonexistent ones:
rm --force path/to/file1 path/to/file2 ...

# Remove specific files interactively prompting before each removal:
rm --interactive path/to/file1 path/to/file2 ...

# Remove specific files printing info about each removal:
rm --verbose path/to/file1 path/to/file2 ...

# Remove specific files and directories recursively:
rm --recursive path/to/file_or_directory1 path/to/file_or_directory2 ...
```
- `cat`


```yaml
# Print the contents of a file to the standard output:
cat path/to/file

# Concatenate several files into an output file:
cat path/to/file1 path/to/file2 ... > path/to/output_file

# Append several files to an output file:
cat path/to/file1 path/to/file2 ... >> path/to/output_file

# Copy the contents of a file into an output file in [u]nbuffered mode:
cat -u /dev/tty12 > /dev/tty13

# 写入内容到文件，内容以EOF结尾表示结束:
cat > path/to/file << EOF

# [n]umber all output lines:
cat -n path/to/file

# Display non-printable and whitespace characters (with `M-` prefix if non-ASCII):
cat -v -t -e path/to/file
```
- `tac`

```bash
# Concatenate specific files in reversed order:
tac path/to/file1 path/to/file2 ...

# Display `stdin` in reversed order:
cat path/to/file | tac

# Use a specific separator:
tac --separator , path/to/file1 path/to/file2 ...

# Use a specific regex as a separator:
tac --regex --separator [,;] path/to/file1 path/to/file2 ...

# Use a separator before each file:
tac --before path/to/file1 path/to/file2 ...
```
- `head`


```bash
# Output the first few lines of a file:
head -n count path/to/file

# Output the first few bytes of a file:
head -c count path/to/file

# Output everything but the last few lines of a file:
head -n -count path/to/file

# Output everything but the last few bytes of a file:
head -c -count path/to/file
```
- `tail`

```bash
# Show last 'count' lines in file:
tail -n count path/to/file

# Print a file from a specific line number:
tail -n +count path/to/file

# Print a specific count of bytes from the end of a given file:
tail -c count path/to/file

# Print the last lines of a given file and keep reading file until `Ctrl + C`:
tail --follow path/to/file

# Keep reading file until `Ctrl + C`, even if the file is inaccessible:
tail --retry --follow path/to/file

# Show last 'num' lines in 'file' and refresh every 'n' seconds:
tail -n count --sleep-interval seconds --follow path/to/file
```
- `less`

```bash
# Open a file:
less source_file

# Page down / up:
<Space> (down), b (up)

# Go to end / start of file:
G (end), g (start)

# Forward search for a string (press `n`/`N` to go to next/previous match):
/something

# Backward search for a string (press `n`/`N` to go to next/previous match):
?something

# Follow the output of the currently opened file:
F

# Open the current file in an editor:
v

# Exit:
q
```
- `more`
```bash
# Open a file:
more path/to/file

# Open a file displaying from a specific line:
more +line_number path/to/file

# Display help:
more --help

# Go to the next page:
<Space>

# Search for a string (press `n` to go to the next match):
/something

# Exit:
q

# Display help about interactive commands:
h
```

- `cp`

```bash
# Copy a file to another location:
cp path/to/source_file.ext path/to/target_file.ext

# Copy a file into another directory, keeping the filename:
cp path/to/source_file.ext path/to/target_parent_directory

# Recursively copy a directory's contents to another location (if the destination exists, the directory is copied inside it):
cp -r path/to/source_directory path/to/target_directory

# Copy a directory recursively, in verbose mode (shows files as they are copied):
cp -vr path/to/source_directory path/to/target_directory

# Copy text files to another location, in interactive mode (prompts user before overwriting):
cp -i *.txt path/to/target_directory

# Follow symbolic links before copying:
cp -L link path/to/target_directory

# Use the full path of source files, creating any missing intermediate directories when copying:
cp --parents source/path/to/file path/to/target_file
```
- `mv`
```bash
# Rename a file or directory when the target is not an existing directory:
mv source target

# Move a file or directory into an existing directory:
mv source existing_directory

# Move multiple files into an existing directory, keeping the filenames unchanged:
mv source1 source2 source3 existing_directory

# Do not prompt for confirmation before overwriting existing files:
mv -f source target

# Prompt for confirmation before overwriting existing files, regardless of file permissions:
mv -i source target

# Do not overwrite existing files at the target:
mv -n source target

# Move files in verbose mode, showing files after they are moved:
mv -v source target
```
- `rename`

```bash
# Rename files using simple substitutions (substitute 'foo' with 'bar' wherever found):
rename foo bar *

# Dry-run# display which renames would occur without performing them:
rename -vn foo bar *

# Do not overwrite existing files:
rename -o foo bar *

# Change file extensions:
rename .ext .bak *.ext

# Prepend "foo" to all filenames in the current directory:
rename '' 'foo' *

# Rename a group of increasingly numbered files zero-padding the numbers up to 3 digits:
rename foo foo00 foo? && rename foo foo0 foo??
```
- `realpath`

```bash
# Display the absolute path for a file or directory:
realpath path/to/file_or_directory

# Require all path components to exist:
realpath --canonicalize-existing path/to/file_or_directory

# Resolve ".." components before symlinks:
realpath --logical path/to/file_or_directory

# Disable symlink expansion:
realpath --no-symlinks path/to/file_or_directory

# Suppress error messages:
realpath --quiet path/to/file_or_directory
```
- `tree`

```bash
# Print files and directories up to 'num' levels of depth (where 1 means the current directory):
tree -L num

# Print directories only:
tree -d

# Print hidden files too with colorization on:
tree -a -C

# Print the tree without indentation lines, showing the full path instead (use `-N` to not escape non-printable characters):
tree -i -f

# Print the size of each file and the cumulative size of each directory, in human-readable format:
tree -s -h --du

# Print files within the tree hierarchy, using a wildcard (glob) pattern, and pruning out directories that don't contain matching files:
tree -P '*.txt' --prune

# Print directories within the tree hierarchy, using the wildcard (glob) pattern, and pruning out directories that aren't ancestors of the wanted one:
tree -P directory_name --matchdirs --prune

# Print the tree ignoring the given directories:
tree -I 'directory_name1|directory_name2'
```
- `ln`

:::info{title="相关信息"}
ln命令是Linux系统中的一个非常重要的命令，它的功能是为某一个文件在另外一个位置建立一个同步的链接。当我们需要在不同的目录，用到相同的文件时，我们不需要在每一个需要的目录下都放一个必须相同的文件，我们只要在某个固定的目录，放上该文件，然后在其他的目录下用ln命令链接（link）它就可以，不必重复占用磁盘空间。

ln命令有两种链接方式：硬链接和软链接。硬链接是指通过索引节点来进行链接，而软链接则是建立一个特殊的文件来指向另外一个文件。硬链接只能对文件进行链接，而软链接可以对目录进行链接。
:::

```bash
# Create a symbolic link to a file or directory:
ln -s /path/to/file_or_directory path/to/symlink

# Overwrite an existing symbolic link to point to a different file:
ln -sf /path/to/new_file path/to/symlink

# Create a hard link to a file:
ln /path/to/file path/to/hardlink
```

## 文件对比、补丁
- `diff`


```bash
# Compare files (lists changes to turn `old_file` into `new_file`):
diff old_file new_file

# Compare files, ignoring white spaces:
diff --ignore-all-space old_file new_file

# Compare files, showing the differences side by side:
diff --side-by-side old_file new_file

# Compare files, showing the differences in unified format (as used by `git diff`):
diff --unified old_file new_file

# Compare directories recursively (shows names for differing files/directories as well as changes made to files):
diff --recursive old_directory new_directory

# Compare directories, only showing the names of files that differ:
diff --recursive --brief old_directory new_directory

# Create a patch file for Git from the differences of two text files, treating nonexistent files as empty:
diff --text --unified --new-file old_file new_file > diff.patch
```
- `patch`

```bash
# Execute commands from standard input (press `Ctrl + D` when done):
batch

# Execute a command from standard input:
echo "./make_db_backup.sh" | batch

# Execute commands from a given file:
batch -f path/to/file
```

### 文件查找
- `find`


```bash
# Find files by extension:
find root_path -name '*.ext'

# Find files matching multiple path/name patterns:
find root_path -path '**/path/**/*.ext' -or -name '*pattern*'

# Find directories matching a given name, in case-insensitive mode:
find root_path -type d -iname '*lib*'

# Find files matching a given pattern, excluding specific paths:
find root_path -name '*.py' -not -path '*/site-packages/*'

# Find files matching a given size range, limiting the recursive depth to "1"::
find root_path -maxdepth 1 -size +500k -size -10M

# Run a command for each file (use `{}` within the command to access the filename):
find root_path -name '*.ext' -exec wc -l {} \;

# Find files modified in the last 7 days:
find root_path -daystart -mtime -7

# Find empty (0 byte) files and delete them:
find root_path -type f -empty -delete
```
- `locate`


```bash
# Look for pattern in the database. Note: the database is recomputed periodically (usually weekly or daily):
locate pattern

# Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):
locate */filename

# Recompute the database. You need to do it if you want to find recently added files:
sudo updatedb
```
- `which`


```bash
# Search the PATH environment variable and display the location of any matching executables:
which executable

# If there are multiple executables which match, display all:
which -a executable
```
- `whereis`

```bash
# Locate binary, source and man pages for ssh:
whereis ssh

# Locate binary and man pages for ls:
whereis -bm ls

# Locate source of gcc and man pages for Git:
whereis -s gcc -m git

# Locate binaries for gcc in `/usr/bin/` only:
whereis -b -B /usr/bin/ -f gcc

# Locate unusual binaries (those that have more or less than one binary on the system):
whereis -u *

# Locate binaries that have unusual manual entries (binaries that have more or less than one manual installed):
whereis -u -m *
```
### 所有者(组)、权限和属性
- `chown`

```bash
# Change the owner user of a file/directory:
chown user path/to/file_or_directory

# Change the owner user and group of a file/directory:
chown user:group path/to/file_or_directory

# Recursively change the owner of a directory and its contents:
chown -R user path/to/directory

# Change the owner of a symbolic link:
chown -h user path/to/symlink

# Change the owner of a file/directory to match a reference file:
chown --reference=path/to/reference_file path/to/file_or_directory
```
- `chmod`

```bash
# Give the [u]ser who owns a file the right to e[x]ecute it:
chmod u+x path/to/file

# Give the [u]ser rights to [r]ead and [w]rite to a file/directory:
chmod u+rw path/to/file_or_directory

# Remove e[x]ecutable rights from the [g]roup:
chmod g-x path/to/file

# Give [a]ll users rights to [r]ead and e[x]ecute:
chmod a+rx path/to/file

# Give [o]thers (not in the file owner's group) the same rights as the [g]roup:
chmod o=g path/to/file

# Remove all rights from [o]thers:
chmod o= path/to/file

# Change permissions recursively giving [g]roup and [o]thers the ability to [w]rite:
chmod -R g+w,o+w path/to/directory

# Recursively give [a]ll users [r]ead permissions to files and e[X]ecute permissions to sub-directories within a directory:
chmod -R a+rX path/to/directory
```
- `chgrp`

```bash
# Change the owner group of a file/directory:
chgrp group path/to/file_or_directory

# Recursively change the owner group of a directory and its contents:
chgrp -R group path/to/directory

# Change the owner group of a symbolic link:
chgrp -h group path/to/symlink

# Change the owner group of a file/directory to match a reference file:
chgrp --reference=path/to/reference_file path/to/file_or_directory
```
- `lsattr`

```bash
# Display the attributes of the files in the current directory:
lsattr

# List the attributes of files in a particular path:
lsattr path

# List file attributes recursively in the current and subsequent directories:
lsattr -R

# Show attributes of all the files in the current directory, including hidden ones:
lsattr -a

# Display attributes of directories in the current directory:
lsattr -d
```
- `chattr`

```bash
# Make a file or directory immutable to changes and deletion, even by superuser:
chattr +i path/to/file_or_directory

# Make a file or directory mutable:
chattr -i path/to/file_or_directory

# Recursively make an entire directory and contents immutable:
chattr -R +i path/to/directory
```
### (解)压缩类
- `tar`

```bash
# [c]reate an archive and write it to a [f]ile:
tar cf path/to/target.tar path/to/file1 path/to/file2 ...

# [c]reate a g[z]ipped archive and write it to a [f]ile:
tar czf path/to/target.tar.gz path/to/file1 path/to/file2 ...

# [c]reate a g[z]ipped archive from a directory using relative paths:
tar czf path/to/target.tar.gz --directory=path/to/directory .

# E[x]tract a (compressed) archive [f]ile into the current directory [v]erbosely:
tar xvf path/to/source.tar[.gz|.bz2|.xz]

# E[x]tract a (compressed) archive [f]ile into the target directory:
tar xf path/to/source.tar[.gz|.bz2|.xz] --directory=path/to/directory

# [c]reate a compressed archive and write it to a [f]ile, using [a]rchive suffix to determine the compression program:
tar caf path/to/target.tar.xz path/to/file1 path/to/file2 ...

# Lis[t] the contents of a tar [f]ile [v]erbosely:
tar tvf path/to/source.tar

# E[x]tract files matching a pattern from an archive [f]ile:
tar xf path/to/source.tar --wildcards "*.html"
```
- `zip`


```bash
# Add files/directories to a specific archive:
zip -r path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

# Remove files/directories from a specific archive:
zip --delete path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

# Archive files/directories e[x]cluding specified ones:
zip path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ... --exclude path/to/excluded_files_or_directories

# Archive files/directories with a specific compression level (`0` # the lowest, `9` # the highest):
zip -r -0-9 path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

# Create an encrypted archive with a specific password:
zip -r --encrypt path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

# Archive files/directories to a multi-part [s]plit zip file (e.g. 3 GB parts):
zip -r -s 3g path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

# Print a specific archive contents:
zip -sf path/to/compressed.zip
```
- `unzip`

```bash
# Extract all files/directories from specific archives into the current directory:
unzip path/to/archive1.zip path/to/archive2.zip ...

# Extract files/directories from archives to a specific path:
unzip path/to/archive1.zip path/to/archive2.zip ... -d path/to/output

# List the contents of a specific archive without extracting them:
unzip -l path/to/archive.zip

# Extract files/directories from archives to `stdout`:
unzip -c path/to/archive1.zip path/to/archive2.zip ...

# Extract the contents of the file(s) to `stdout` alongside the extracted file names:
unzip -O gbk path/to/archive1.zip path/to/archive2.zip ...

# Extract a specific file from an archive:
unzip -j path/to/archive.zip path/to/file_in_archive1 path/to/file_in_archive2 ...
```

- `unrar`

```bash
# Extract files with original directory structure:
unrar x {{compressed.rar}}

# Extract files to a specified path with the original directory structure:
unrar x {{compressed.rar}} {{path/to/extract}}

# Extract files into current directory, losing directory structure in the archive:
unrar e {{compressed.rar}}

# Test integrity of each file inside the archive file:
unrar t {{compressed.rar}}

# List files inside the archive file without decompressing it:
unrar l {{compressed.rar}}
```
- `7z`

```bash
# 安装
sudo apt install p7zip-full

# [a]dd a file or directory to a new or existing archive:
7z a {{path/to/archive.7z}} {{path/to/file_or_directory}}

# Encrypt an existing archive (including filenames):
7z a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}

# E[x]tract an archive preserving the original directory structure:
7z x {{path/to/archive.7z}}

# E[x]tract an archive to a specific directory:
7z x {{path/to/archive.7z}} -o{{path/to/output}}

# E[x]tract an archive to stdout:
7z x {{path/to/archive.7z}} -so

# [a]rchive using a specific archive type:
7z a -t{{7z|bzip2|gzip|lzip|tar|zip}} {{path/to/archive.7z}} {{path/to/file_or_directory}}

# [l]ist the contents of an archive:
7z l {{path/to/archive.7z}}

# List available archive types:
7z i
```
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
## 内存管理
- `free`

```bash
# Display system memory:
free

# Display memory in Bytes/KB/MB/GB:
free -b|k|m|g

# Display memory in human-readable units:
free -h

# Refresh the output every 2 seconds:
free -s 2
```
### 虚拟内存设置
- `swapon`

参考：https://blog.kevin2li.top/post/25

## 设备/磁盘管理
- `fdisk`
```bash
# List partitions:
sudo fdisk -l

# Start the partition manipulator:
sudo fdisk /dev/sdX

# Once partitioning a disk, create a partition:
n

# Once partitioning a disk, select a partition to delete:
d

# Once partitioning a disk, view the partition table:
p

# Once partitioning a disk, write the changes made:
w

# Once partitioning a disk, discard the changes made:
q

# Once partitioning a disk, open a help menu:
m
```

- `mount`

```bash
# 将设备 "/dev/sdb1" 挂载到 "/mnt/media" 目录
sudo mount /dev/sdb1 /mnt/media
```
:::info{title="相关信息"}
格式：
`mount [OPTION...] DEVICE_NAME DIRECTORY`
:::

- `umount`
```bash
umount DIRECTORY
umount DEVICE_NAME
```
- `df`
```bash
# Display all filesystems and their disk usage:
df

# Display all filesystems and their disk usage in human-readable form:
df -h

# Display the filesystem and its disk usage containing the given file or directory:
df path/to/file_or_directory

# Display statistics on the number of free inodes:
df -i

# Display filesystems but exclude the specified types:
df -x squashfs -x tmpfs
```
- `du`
```bash
# List the sizes of a directory and any subdirectories, in the given unit (B/KiB/MiB):
du -b|k|m path/to/directory

# List the sizes of a directory and any subdirectories, in human-readable form (i.e. auto-selecting the appropriate unit for each size):
du -h path/to/directory

# Show the size of a single directory, in human-readable units:
du -sh path/to/directory

# List the human-readable sizes of a directory and of all the files and directories within it:
du -ah path/to/directory

# List the human-readable sizes of a directory and any subdirectories, up to N levels deep:
du -h --max-depth=N path/to/directory

# List the human-readable size of all `.jpg` files in subdirectories of the current directory, and show a cumulative total at the end:
du -ch */*.jpg
```
- `lsblk`  
列出块设备,可以查看到块设备的挂载点

```bash
# List all storage devices in a tree-like format:
lsblk

# Also list empty devices:
lsblk -a

# Print the SIZE column in bytes rather than in a human-readable format:
lsblk -b

# Output info about filesystems:
lsblk -f

# Use ASCII characters for tree formatting:
lsblk -i

# Output info about block-device topology:
lsblk -t

# Exclude the devices specified by the comma-separated list of major device numbers:
lsblk -e 1,7

# Display a customized summary using a comma-separated list of columns:
lsblk --output NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a782557c2deceee5720cf743b319a1c3.image.png)
- `lsusb`  

```bash
# List all the USB devices available:
lsusb

# List the USB hierarchy as a tree:
lsusb -t

# List verbose information about USB devices:
lsusb --verbose

# List detailed information about a USB device:
lsusb -D {{device}}

# List devices with a specified vendor and product ID only:
lsusb -d {{vendor}}:{{product}}
```
- `lspci`  

```bash
# Show a brief list of devices:
lspci

# Display additional info:
lspci -v

# Display drivers and modules handling each device:
lspci -k

# Show a specific device:
lspci -s {{00:18.3}}

# Dump info in a readable form:
lspci -vm
```
- `iotop`  
```bash
# 查看所有进程的磁盘I/O
sudo iotop

# 查看当前实际进行磁盘I/O的进程
sudo iotop -o

# 查看指定进程的磁盘I/O情况
sudo iotop -p 22
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/db000798190b020829a6a243333aac05.image.png)

## 网络管理
### 基本网络配置
- `ping`


```bash
# Ping host:
ping host

# Ping a host only a specific number of times:
ping -c count host

# Ping host, specifying the interval in seconds between requests (default is 1 second):
ping -i seconds host

# Ping host without trying to lookup symbolic names for addresses:
ping -n host

# Ping host and ring the bell when a packet is received (if your terminal supports it):
ping -a host

# Also display a message if no response was received:
ping -O host
```
- `ifconfig`

```bash
# View network settings of an Ethernet adapter:
ifconfig eth0

# Display details of all interfaces, including disabled interfaces:
ifconfig -a

# Disable eth0 interface:
ifconfig eth0 down

# Enable eth0 interface:
ifconfig eth0 up

# Assign IP address to eth0 interface:
ifconfig eth0 ip_address
```
- `ip`

```bash
# List interfaces with detailed info:
ip address

# List interfaces with brief network layer info:
ip -brief address

# List interfaces with brief link layer info:
ip -brief link

# Display the routing table:
ip route

# Show neighbors (ARP table):
ip neighbour

# Make an interface up/down:
ip link set interface up/down

# Add/Delete an IP address to an interface:
ip addr add/del ip/mask dev interface

# Add a default route:
ip route add default via ip dev interface

```
- `route`

```bash
# Display the information of route table:
route -n

# Add route rule:
sudo route add -net ip_address netmask netmask_address gw gw_address

# Delete route rule:
sudo route del -net ip_address netmask netmask_address dev gw_address
```
- `traceroute`

```bash
# Traceroute to a host:
traceroute host

# Disable IP address and host name mapping:
traceroute -n host

# Specify wait time for response:
traceroute -w 0.5 host

# Specify number of queries per hop:
traceroute -q 5 host

# Specify size in bytes of probing packet:
traceroute host 42
```
- `lsof`

```bash
# Find the processes that have a given file open:
lsof path/to/file

# Find the process that opened a local internet port:
lsof -i :port

# Only output the process ID (PID):
lsof -t path/to/file

# List files opened by the given user:
lsof -u username

# List files opened by the given command or process:
lsof -c process_or_command_name

# List files opened by a specific process, given its PID:
lsof -p PID

# List open files in a directory:
lsof +D path/to/directory

# Find the process that is listening on a local IPv6 TCP port and don't convert network or port numbers:
lsof -i6TCP:port -sTCP:LISTEN -n -P
```
- `netstat`

```bash
# List all ports:
netstat --all

# List all listening ports:
netstat --listening

# List listening TCP ports:
netstat --tcp

# Display PID and program names:
netstat --program

# List information continuously:
netstat --continuous

# List routes and do not resolve IP addresses to hostnames:
netstat --route --numeric

# List listening TCP and UDP ports (+ user and process if you're root):
netstat --listening --program --numeric --tcp --udp --extend
```
### 防火墙
- `firewall-cmd`

```bash
# View the available firewall zones:
firewall-cmd --get-active-zones

# View the rules which are currently applied:
firewall-cmd --list-all

# Permanently move the interface into the block zone, effectively blocking all communication:
firewall-cmd --permanent --zone=block --change-interface=enp1s0

# Permanently open the port for a service in the specified zone (like port 443 when in the `public` zone):
firewall-cmd --permanent --zone=public --add-service=https

# Permanently close the port for a service in the specified zone (like port 80 when in the `public` zone):
firewall-cmd --permanent --zone=public --remove-service=http

# Permanently open two arbitrary ports in the specified zone:
firewall-cmd --permanent --zone=public --add-port=25565/tcp --add-port=19132/udp

# Reload firewalld to force rule changes to take effect:
firewall-cmd --reload
```
- `iptables`

```bash
# View chains, rules, and packet/byte counters for the filter table:
sudo iptables -vnL

# Set chain policy rule:
sudo iptables -P chain rule

# Append rule to chain policy for IP:
sudo iptables -A chain -s ip -j rule

# Append rule to chain policy for IP considering protocol and port:
sudo iptables -A chain -s ip -p protocol --dport port -j rule

# Add a NAT rule to translate all traffic from the `192.168.0.0/24` subnet to the host's public IP:
sudo iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j MASQUERADE

# Delete chain rule:
sudo iptables -D chain rule_line_number

# Save iptables configuration of a given table to a file:
sudo iptables-save -t tablename > path/to/iptables_file

# Restore iptables configuration from a file:
sudo iptables-restore < path/to/iptables_file
```
### 抓包
- `tcpdump`

```bash
# List available network interfaces:
tcpdump -D

# Capture the traffic of a specific interface:
tcpdump -i eth0

# Capture all TCP traffic showing contents (ASCII) in console:
tcpdump -A tcp

# Capture the traffic from or to a host:
tcpdump host www.example.com

# Capture the traffic from a specific interface, source, destination and destination port:
tcpdump -i eth0 src 192.168.1.1 and dst 192.168.1.2 and dst port 80

# Capture the traffic of a network:
tcpdump net 192.168.1.0/24

# Capture all traffic except traffic over port 22 and save to a dump file:
tcpdump -w dumpfile.pcap port not 22

# Read from a given dump file:
tcpdump -r dumpfile.pcap
```
- `tshark`

### 扫描
- `nmap`
```bash
# 安装
sudo apt install nmap

# 端口扫描
sudo nmap -Pn 192.168.2.121
nmap -sV -p 1-65535 192.168.1.1/24
```

- `ncat`
```bash
# Connect to example.org on TCP port 8080.
ncat example.org 8080

# Listen for connections on TCP port 8080.
ncat -l 8080

# Redirect TCP port 8080 on the local machine to host on port 80.
ncat --sh-exec "ncat example.org 80" -l 8080 --keep-open

# Bind to TCP port 8081 and attach /bin/bash for the world to access freely.
ncat --exec "/bin/bash" -l 8081 --keep-open

# Bind a shell to TCP port 8081, limit access to hosts on a local network, and limit the maximum number of simultaneous connections to 3.
ncat --exec "/bin/bash" --max-conns 3 --allow 192.168.0.0/24 -l 8081 --keep-open

# Connect to smtphost:25 through a SOCKS4 server on port 1080.
ncat --proxy socks4host --proxy-type socks4 --proxy-auth joe smtphost 25

# Connect to smtphost:25 through a SOCKS5 server on port 1080.
ncat --proxy socks5host --proxy-type socks5 --proxy-auth joe:secret smtphost 25

# Create an HTTP proxy server on localhost port 8888.
ncat -l --proxy-type http localhost 8888

# Send a file over TCP port 9899 from host2 (client) to host1 (server).
HOST1$ ncat -l 9899 > outputfile

HOST2$ ncat HOST1 9899 < inputfile

# Transfer in the other direction, turning Ncat into a “one file” server.
HOST1$ ncat -l 9899 < inputfile
HOST2$ ncat HOST1 9899 > outputfile
```
- `nc`

```bash
# Open a TCP connection to port 42 of host.example.com, using port 31337 as the source port, with a timeout of 5 seconds:
nc -p 31337 -w 5 host.example.com 42

# Open a UDP connection to port 53 of host.example.com:
nc -u host.example.com 53

# Open a TCP connection to port 42 of host.example.com using 10.1.2.3 as the IP for the local end of the connection:
nc -s 10.1.2.3 host.example.com 42

# Create and listen on a UNIX-domain stream socket:
nc -lU /var/tmp/dsocket

# Connect to port 42 of host.example.com via an HTTP proxy at 10.2.3.4, port 8080.  This example could also be used by ssh(1); see the ProxyCommand directive in ssh_config(5) for more information.
nc -x10.2.3.4:8080 -Xconnect host.example.com 42

# The same example again, this time enabling proxy authentication with username “ruser” if the proxy requires it:
nc -x10.2.3.4:8080 -Xconnect -Pruser host.example.com 42
```
### 下载
- `wget`
- `curl`

```bash
# 携带数据
curl -d "name=curl" https://example.com
curl -d "name=curl" -d "tool=cmdline" https://example.com

# 表单数据(Content-Type multipart/form-data)
curl -F name=John -F shoesize=11 https://example.com/
curl -F profile=@portrait.jpg https://example.com/upload.cgi
 
# POST请求
curl -d '{"channel":"4","ifautologin":"0","pagesign":"secondauth"}' -H "Content-Type: application/json" -X POST http://10.255.255.34/api/v1/login

# 下载保存
curl -o output.html http://example.com/
curl -O http://example.com/file.html

# 自动重定向
curl -L https://example.com

# 使用代理
curl -x socks5://192.168.2.1:10080 https://www.baidu.com
curl -x http://user:password@proxy.example.com:8080 http://www.example.com
curl -U daniel:secr3t -x myproxy:80 http://example.com
curl --proxy-header "User-Agent: magic/3000" -x proxy https://example.com/
```
- `axel`

```bash
# Download a URL to a file:
axel url

# Download and specify filename:
axel url -o path/to/file

# Download with multiple connections:
axel -n connections_num url

# Search for mirrors:
axel -S mirrors_num url

# Limit download speed (bytes per second):
axel -s speed url
```
### 监控流量
- `iftop`
```bash
# Show the bandwidth usage:
sudo iftop

# Show the bandwidth usage of a given interface:
sudo iftop -i interface

# Show the bandwidth usage with port information:
sudo iftop -P

# Do not show bar graphs of traffic:
sudo iftop -b

# Do not look up hostnames:
sudo iftop -n
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c3347f697509e1a47e9cb8159b831999.image.png)

## 字符串处理
- `awk`

```bash
# Print the fifth column (a.k.a. field) in a space-separated file:
awk '{print $5}' path/to/file

# Print the second column of the lines containing "foo" in a space-separated file:
awk '/foo/ {print $2}' path/to/file

# Print the last column of each line in a file, using a comma (instead of space) as a field separator:
awk -F ',' '{print $NF}' path/to/file

# Sum the values in the first column of a file and print the total:
awk '{s+=$1} END {print s}' path/to/file

# Print every third line starting from the first line:
awk 'NR%3==1' path/to/file

# Print different values based on conditions:
awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' path/to/file

# Print all lines where the 10th column value equals the specified value:
awk '($10 == value)'

# Print all the lines which the 10th column value is between a min and a max:
awk '($10 >= min_value && $10 <= max_value)'
```
- `grep`

```bash
# Search for a pattern within a file:
grep "search_pattern" path/to/file

# Search for an exact string (disables regular expressions):
grep --fixed-strings "exact_string" path/to/file

# Search for a pattern in all files recursively in a directory, showing line numbers of matches, ignoring binary files:
grep --recursive --line-number --binary-files=without-match "search_pattern" path/to/directory

# Use extended regular expressions (supports `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode:
grep --extended-regexp --ignore-case "search_pattern" path/to/file

# Print 3 lines of context around, before, or after each match:
grep --context|before-context|after-context=3 "search_pattern" path/to/file

# Print file name and line number for each match with color output:
grep --with-filename --line-number --color=always "search_pattern" path/to/file

# Search for lines matching a pattern, printing only the matched text:
grep --only-matching "search_pattern" path/to/file

# Search `stdin` for lines that do not match a pattern:
cat path/to/file | grep --invert-match "search_pattern"
```
- `sed`

```bash
# Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in all input lines and print the result to `stdout`:
command | sed 's/apple/mango/g'

# Execute a specific script [f]ile and print the result to `stdout`:
command | sed -f path/to/script.sed

# Replace all `apple` (extended regex) occurrences with `APPLE` (extended regex) in all input lines and print the result to `stdout`:
command | sed -E 's/(apple)/\U\1/g'

# Print just a first line to `stdout`:
command | sed -n '1p'
sed -n "29496,29516p" service.log

# Replace all `apple` (basic regex) occurrences with `mango` (basic regex) in a specific file and overwrite the original file in place:
sed -i 's/apple/mango/g' path/to/file
```

- `jq`

```bash
# Execute a specific expression (print a colored and formatted json):
cat path/to/file.json | jq '.'

# Execute a specific script:
cat path/to/file.json | jq --from-file path/to/script.jq

# Pass specific arguments:
cat path/to/file.json | jq --arg "name1" "value1" --arg "name2" "value2" ... '. + $ARGS.named'

# Print specific keys:
cat path/to/file.json | jq '.key1, .key2, ...'

# Print specific array items:
cat path/to/file.json | jq '.[index1], .[index2], ...'

# Print all array items/object keys:
cat path/to/file.json | jq '.[]'

# Add/remove specific keys:
cat path/to/file.json | jq '. +|- {"key1": "value1", "key2": "value2", ...}'
```
- `column`

```bash
# Format the output of a command for a 30 characters wide display:
printf "header1 header2\nbar foo\n" | column --output-width 30

# Split columns automatically and auto-align them in a tabular format:
printf "header1 header2\nbar foo\n" | column --table

# Specify the column delimiter character for the `--table` option (e.g. "," for CSV) (defaults to whitespace):
printf "header1,header2\nbar,foo\n" | column --table --separator ,

# Fill rows before filling columns:
printf "header1\nbar\nfoobar\n" | column --output-width 30 --fillrows
```

- `cut`

```bash
# Print a specific character/field range of each line:
command | cut --characters|fields=1|1,10|1-10|1-|-10

# Print a range of each line with a specific delimiter:
command | cut --delimiter="," --fields=1

# Print a range of each line of the specific file:
cut --characters=1 path/to/file
```
- `split`

```bash
# Split a file, each split having 10 lines (except the last split):
split -l 10 path/to/file

# Split a file into 5 files. File is split such that each split has same size (except the last split):
split -n 5 path/to/file

# Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):
split -b 512 path/to/file

# Split a file with at most 512 bytes in each split without breaking lines:
split -C 512 path/to/file
```
- `join`

```bash
# Join two files on the first (default) field:
join file1 file2

# Join two files using a comma (instead of a space) as the field separator:
join -t ',' file1 file2

# Join field3 of file1 with field1 of file2:
join -1 3 -2 1 file1 file2

# Produce a line for each unpairable line for file1:
join -a 1 file1 file2

# Join a file from `stdin`:
cat path/to/file1 | join# path/to/file2
```
- `sort`

```bash
# Sort a file in ascending order:
sort path/to/file

# Sort a file in descending order:
sort --reverse path/to/file

# Sort a file in case-insensitive way:
sort --ignore-case path/to/file

# Sort a file using numeric rather than alphabetic order:
sort --numeric-sort path/to/file

# Sort `/etc/passwd` by the 3rd field of each line numerically, using ":" as a field separator:
sort --field-separator=: --key=3n /etc/passwd

# Sort a file preserving only unique lines:
sort --unique path/to/file

# Sort a file, printing the output to the specified output file (can be used to sort a file in-place):
sort --output=path/to/file path/to/file

# Sort numbers with exponents:
sort --general-numeric-sort path/to/file
```
- `uniq`

```bash
# Display each line once:
sort path/to/file | uniq

# Display only unique lines:
sort path/to/file | uniq -u

# Display only duplicate lines:
sort path/to/file | uniq -d

# Display number of occurrences of each line along with that line:
sort path/to/file | uniq -c

# Display number of occurrences of each line, sorted by the most frequent:
sort path/to/file | uniq -c | sort -nr
```
- `tr`


```bash
# Replace all occurrences of a character in a file, and print the result:
tr find_character replace_character < path/to/file

# Replace all occurrences of a character from another command's output:
echo text | tr find_character replace_character

# Map each character of the first set to the corresponding character of the second set:
tr 'abcd' 'jkmn' < path/to/file

# Delete all occurrences of the specified set of characters from the input:
tr -d 'input_characters' < path/to/file

# Compress a series of identical characters to a single character:
tr -s 'input_characters' < path/to/file

# Translate the contents of a file to upper-case:
tr "[:lower:]" "[:upper:]" < path/to/file

# Strip out non-printable characters from a file:
tr -cd "[:print:]" < path/to/file
```
- `wc`

```bash
# Count all lines in a file:
wc -l path/to/file

# Count all words in a file:
wc -w path/to/file

# Count all bytes in a file:
wc -c path/to/file

# Count all characters in a file (taking multi-byte characters into account):
wc -m path/to/file

# Count all lines, words and bytes from `stdin`:
find . | wc

# Count the length of the longest line in number of characters:
wc --max-line-length path/to/file
```
## 管道
- `xargs`

```bash
# Run a command using the input data as arguments:
arguments_source | xargs command

# Run multiple chained commands on the input data:
arguments_source | xargs sh -c "command1 && command2 | command3"

# Delete all files with a `.backup` extension (`-print0` uses a null character to split file names, and `-0` uses it as delimiter):
find . -name '*.backup' -print0 | xargs -0 rm -v

# Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as `_`) with the input line:
arguments_source | xargs -I _ command _ optional_extra_arguments

# Parallel runs of up to `max-procs` processes at a time; the default is 1. If `max-procs` is 0, xargs will run as many processes as possible at a time:
arguments_source | xargs -P max-procs command
```
## 日志管理
- `journalctl`  
`journalctl`是一种用于查看Systemd系统日志的命令行工具。它可以帮助你查找特定的日志数据或浏览整个日志文件，以便审查系统活动或故障。以下是一些journalctl的常用用法：

1. 列出所有日志条目： 

```
journalctl
```

2. 根据服务名称列出所有与该服务相关的日志条目：

```
journalctl -u service_name
```

3. 根据日期和时间过滤日志词条。例如，列出12月3日之后的所有日志：

```
journalctl --since "2019-12-03"
```

4. 使用实时输出功能实时查看系统日志：

```
journalctl -f
```

5. 通过系统日志查找与特定进程相关的条目：

```
journalctl _PID=process_id
```

6. 列出指定进程名称的所有日志条目：

```
journalctl _COMM=process_name
```

7. 列出最近特定行数的日志：

```
journalctl -n number_of_lines
```

8. 列出日志文件大小，磁盘使用量和剩余磁盘空间：

```
journalctl --disk-usage
```

9. 显示特定时间段内的内核消息：

```
journalctl --dmesg
```

- `last`

```bash
# View last logins, their duration and other information as read from `/var/log/wtmp`:
last

# Specify how many of the last logins to show:
last -n login_count

# Print the full date and time for entries and then display the hostname column last to prevent truncation:
last -F -a

# View all logins by a specific user and show the IP address instead of the hostname:
last username -i

# View all recorded reboots (i.e., the last logins of the pseudo user "reboot"):
last reboot

# View all recorded shutdowns (i.e., the last logins of the pseudo user "shutdown"):
last shutdown

```
- `lastb`

```bash
# Show a list of all last logged in users:
sudo lastb

# Show a list of all last logged in users since a given time:
sudo lastb --since YYYY-MM-DD

# Show a list of all last logged in users until a given time:
sudo lastb --until YYYY-MM-DD

# Show a list of all logged in users at a specific time:
sudo lastb --present hh:mm

# Show a list of all last logged in users and translate the IP into a hostname:
sudo lastb --dns
```
- `lastlog`

```bash
# Display the most recent login of all users:
lastlog

# Display the lastlog record of the specified user:
lastlog --user username

# Display records older than 7 days:
lastlog --before 7

# Display records more recent than 3 days:
lastlog -time 3
```
- `watch`

```bash
# Monitor files in the current directory:
watch ls

# Monitor disk space and highlight the changes:
watch -d df

# Monitor "node" processes, refreshing every 3 seconds:
watch -n 3 "ps aux | grep node"
```
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

## 软件包管理
- `apt`

```bash
# Update the list of available packages and versions (it's recommended to run this before other `apt` commands):
sudo apt update

# Search for a given package:
apt search package

# Show information for a package:
apt show package

# Install a package, or update it to the latest available version:
sudo apt install package

# Remove a package (using `purge` instead also removes its configuration files):
sudo apt remove package

# Upgrade all installed packages to their newest available versions:
sudo apt upgrade

# List all packages:
apt list

# List installed packages:
apt list --installed
```
- `apt-get`

```bash
# Update the list of available packages and versions (it's recommended to run this before other `apt-get` commands):
apt-get update

# Install a package, or update it to the latest available version:
apt-get install package

# Remove a package:
apt-get remove package

# Remove a package and its configuration files:
apt-get purge package

# Upgrade all installed packages to their newest available versions:
apt-get upgrade

# Clean the local repository# removing package files (`.deb`) from interrupted downloads that can no longer be downloaded:
apt-get autoclean

# Remove all packages that are no longer needed:
apt-get autoremove

# Upgrade installed packages (like `upgrade`), but remove obsolete packages and install additional packages to meet new dependencies:
apt-get dist-upgrade
```
- `dpkg`

```bash
# Install a package:
dpkg -i path/to/file.deb

# Remove a package:
dpkg -r package_name

# List installed packages:
dpkg -l pattern

# List a package's contents:
dpkg -L package_name

# List contents of a local package file:
dpkg -c path/to/file.deb

# Find out which package owns a file:
dpkg -S filename
```
- `pacman`

```bash
# Synchronize and update all packages:
sudo pacman -Syu

# Install a new package:
sudo pacman -S package_name

# Remove a package and its dependencies:
sudo pacman -Rs package_name

# Search the package database for a regular expression or keyword:
pacman -Ss "search_pattern"

# List installed packages and versions:
pacman -Q

# List only the explicitly installed packages and versions:
pacman -Qe

# List orphan packages (installed as dependencies but not actually required by any package):
pacman -Qtdq

# Empty the entire pacman cache:
sudo pacman -Scc
```
## 设备管理
### 显卡管理
- `nvidia-smi`

```bash
# Display information on all available GPUs and processes using them:
nvidia-smi

# Display more detailed GPU information:
nvidia-smi --query

# Monitor overall GPU usage with 1-second update interval:
nvidia-smi dmon
```
- `gpustat`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/dc6fd11aa98f8b564e9957e19ef3f86f.image.png)

- `nvtop`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0e94990aba0beefddd56429077e3c838.image.png)
# 参考
