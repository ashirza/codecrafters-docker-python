import subprocess
import sys


def main():    
    # pipe programs stdout and stderr to parent process
    command = sys.argv[3]
    args = sys.argv[4:]
    
    completed_process = subprocess.run([command, *args], capture_output=True)
    if completed_process.stdout:
        stdout = completed_process.stdout.decode("utf-8")
        print(stdout)
    # elif completed_process.stderr:
    #     print(completed_process.stderr.decode("utf-8"), file=sys.stderr)


if __name__ == "__main__":
    main()
