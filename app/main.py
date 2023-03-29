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
    if command == "ls":
        tempfile_path = tempfile.mkdtemp()
        shutil.copy("/usr/local/bin/docker-explorer", tempfile_path)
    try:
        completed_process = subprocess.run([command, *args], capture_output=True)
        os.chroot(tempfile_path)
    finally:
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
