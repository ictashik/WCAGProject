import subprocess

subprocess = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)

subprocess_return = subprocess.stdout.read()
print(subprocess_return)
