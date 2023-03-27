import subprocess
import sys


def main():    
    # pipe programs stdout and stderr to parent process
    command = sys.argv[3]
    args = sys.argv[4:]
    
    try:
        completed_process = subprocess.run([command, *args], capture_output=True)
    except subprocess.CalledProcessError as e:
        exit_code = e.returncode
        print(exit_code)
        sys.exit(exit_code)        
    finally:
        print(completed_process)
        if completed_process.stdout:
            stdout = completed_process.stdout.decode("utf-8")
            stdout = stdout.replace("\n", "")
            print(stdout)
        elif completed_process.stderr:
            stderr = completed_process.stderr.decode("utf-8")
            stderr = stderr.replace("\n", "")
            print(stderr, file=sys.stderr)


if __name__ == "__main__":
    main()
