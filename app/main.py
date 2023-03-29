import os
import tempfile
import subprocess
import sys
import shutil


def main():
    # pipe programs stdout and stderr to parent process
    command = sys.argv[3]
    args = sys.argv[4:]
    # (expecting that the directory won't be accessible)
    # Expected stdout to contain "No such file or directory", got: ""
    try:
        if args[0] == "ls":
            tempfile_path = tempfile.mkdtemp()
            script_path = tempfile_path + "/usr/local/bin"
            os.mkdir(tempfile_path + "/usr")
            os.mkdir(tempfile_path + "/usr/local")
            os.mkdir(tempfile_path + "/usr/local/bin")
            shutil.copy("/usr/local/bin/docker-explorer", script_path)
            os.chroot(tempfile_path)
            os.chdir("/")
        completed_process = subprocess.run([command, *args], capture_output=True)
    finally:
        if args[0] == 'ls':
            stdout = completed_process.stdout.decode("utf-8")
            stdout = stdout.replace("\n", "")
            print(stdout)
            sys.exit(completed_process.returncode)
        if completed_process.returncode != 0:
            stderr = completed_process.stderr.decode("utf-8")
            stderr = stderr.replace("\n", "")
            print(stderr, file=sys.stderr)
            sys.exit(completed_process.returncode)
        elif completed_process.stdout:
            stdout = completed_process.stdout.decode("utf-8")
            stdout = stdout.replace("\n", "")
            print(stdout)
        elif completed_process.stderr:
            stderr = completed_process.stderr.decode("utf-8")
            stderr = stderr.replace("\n", "")
            print(stderr, file=sys.stderr)


if __name__ == "__main__":
    main()
