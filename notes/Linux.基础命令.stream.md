---

id: pag4hv49x8nsjzhibz8o48q
title: 流处理
desc: ''
updated: 1682562443305
created: 1682484242927
---


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
# 将文件按行数拆分成多个部分，并指定后缀和编号格式
split -l 10 -d --additional-suffix .sh  batch_run.sh part_ 

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