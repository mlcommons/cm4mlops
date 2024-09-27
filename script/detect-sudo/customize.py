from cmind import utils
import os, subprocess

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if prompt_sudo() == 0:
        env['CM_SUDO_USER'] = "yes"

    return {'return':0}

def reset_terminal():
    """Reset terminal to default settings."""
    subprocess.run(['stty', 'sane'])

def prompt_retry(timeout=10):
    """Prompt the user with a yes/no question to retry the command, with a 10-second timeout."""
    print(f"Timeout occurred. Do you want to try again? (y/n): ", end='', flush=True)
    
    # Use select to wait for user input with a timeout
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    
    if ready:
        answer = sys.stdin.readline().strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'  # Return True if 'y', False if 'n'
        print("\nInvalid input. Please enter 'y' or 'n'.")
        return prompt_retry(timeout)  # Re-prompt on invalid input
    else:
        print("\nNo input received in 10 seconds. Exiting.")
        return False  # No input within the timeout, so don't retry

def prompt_sudo():
    if os.geteuid() != 0:  # No sudo required for root user
        msg = "[sudo] password for %u:"
        while True:
            try:
                r = subprocess.check_output(["sudo", "-p", msg, "echo", "Check sudo"],
                                            stderr=subprocess.STDOUT, timeout=5)
                print(r.decode('utf-8'))  # Decode bytes to string
                return 0
            except subprocess.TimeoutExpired:
                reset_terminal()  # Reset terminal to sane state
                if not prompt_retry():  # If the user chooses not to retry or times out
                    return -1
            except subprocess.CalledProcessError as e:
                print(f"Command failed: {e.output.decode('utf-8')}")
                reset_terminal()  # Reset terminal in case of failure
                return -1
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                reset_terminal()  # Always reset terminal after error
                return -1

    return -1

def postprocess(i):

    env = i['env']

    return {'return':0}
