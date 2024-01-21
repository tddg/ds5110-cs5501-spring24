import subprocess
from subprocess import check_output
import os

from tester import init, test, cleanup, tester_main

@test(points = 15)
def os_test():
    with open("os.txt") as f:
        if "Ubuntu 22.04" in f.read():
            return None
    return "could not find Ubuntu 22.04 in os.txt"

@test(points = 10)
def cpu_test():
    with open("cpu.txt") as f:
        if "x86_64" in f.read():
            return None
    return "could not find x86_64 in cpu.txt"

@test(points = 10)
def mem_test():
    with open("mem.txt") as f:
        if "8G" in f.read():
            return None
    return "could not find 8G in mem.txt"

@test(points = 10)
def pip3_test():
    with open("pip3.txt") as f:
        if "22.0.2" in f.read():
            return None
    return "could not find 22.0.2 in pip3.txt"

@test(points = 15)
def jupyter_test():
    with open("jupyter.txt") as f:
        if "8.20.0" in f.read():
            return None
    return "could not find 8.20.0 in jupyter.txt"

@test(points = 10)
def bashfile_test():
    if not os.path.exists("count_python.sh"):
        return "missing count_python.sh"

@test(points = 10)
def shebang_test():
    with open("count_python.sh") as f:
        line = f.readline()
    if line.startswith("#!") and "bash" in line:
        return None
    return "count_python.sh does not appear to have a bash shebang line"

@test(points = 10)
def executable_test():
    if not os.access("count_python.sh", os.X_OK):
        return "count_python.sh does not have executable permissions"

if __name__ == "__main__":
    tester_main()
