gTree - .gitignore Aware Tree
====

`tree` is one of my most used linux commands. However, adding files to ignore can be annoying or really verbose. So I decided to write a basic python script to parse .gitignore files and pipe them into tree!

### Getting Started

Install `tree` from your package manager:
```
# Debian, Ubuntu, etc.
sudo apt-get install tree
# Arch
sudo pacman -S tree
# Red Hat distros
sudo yum install tree
# And so on...
```

Install this package with the setup.py file:
```
git clone https://github.com/madelyneriksen/gtree .
python3 setup.py install
```

### Usage

Use the .gitignore file in the current directory:
```
gtree
```

Use a custom .gitignore file:
```
gtree /path/to/.gitignore
```
