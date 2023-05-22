---
id: 3zv8uwsn42iccjabhc4wuvd
title: 文件管理
desc: ''
updated: 1682562388427
created: 1682484030444
---

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
### 文件所有者(组)、权限和属性
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