---

id: 68jcdxt4qg5qdao1kop8ffo
title: 软件包管理
desc: ''
updated: 1682562443260
created: 1682484267171
---


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