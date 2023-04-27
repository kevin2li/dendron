---

id: 3c907m30podo1wr4ul0kz53
title: 终端管理
desc: ''
updated: 1682562443342
created: 1682484227345
---


## 终端管理
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