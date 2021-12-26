import subprocess

completed = subprocess.run(["ls", "-l"])
print("args", completed.args)
print("returncode", completed.returncode)
print("stdout", completed.stdout)
print("stderr", completed.stderr)
