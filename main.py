#!/usr/bin/env python3
import signal
from time import sleep
import os, pwd, subprocess

import psutil

threshold_time_over = 5.0
threshold_cpu = 50
username = 'willc'

def demote(user_uid, user_gid):
    """
    Returns a function that sets the user ID and group ID of the process.
    Used to run a process as a specific user.
    """

    def result():
        os.setgid(user_gid)
        os.setuid(user_uid)

    return result


def restart_eqmac(username):
    """
    Executes a shell command as a specific user.

    Args:
        username (str): The username of the user to run the command as.
    """
    # Get user info from username
    pw_record = pwd.getpwnam(username)
    homedir = pw_record.pw_dir
    user_uid = pw_record.pw_uid
    user_gid = pw_record.pw_gid
    env = os.environ.copy()
    env.update({'HOME': homedir, 'LOGNAME': username, 'PWD': os.getcwd(), 'FOO': 'bar', 'USER': username})

    # Execute the command
    proc = subprocess.Popen(['echo $USER; open -na eqMac'],
                            shell=True,
                            env=env,
                            preexec_fn=demote(user_uid, user_gid),
                            stdout=subprocess.PIPE)


def main():
    """
    Main function to monitor the CoreAudioD process and restart EqMac if necessary.
    """
    sleep_time = 1.0
    time_over = 0.0
    eqmac_pid = 0

    while True:
        # Get the list of all running processes
        processes = psutil.process_iter(['pid', 'name', 'status'])

        # Monitor the processes
        for process in processes:
            if process.name().lower() == 'coreaudiod':
                cpu = process.cpu_percent()
                print(f'CoreAudioD cpu={cpu}%, time_over={time_over} seconds')
                if cpu > threshold_cpu:
                    time_over += sleep_time
                else:
                    time_over -= sleep_time
                    if time_over < 0:
                        time_over = 0
            elif 'eqmac' == process.name().lower():
                eqmac_pid = process.pid

        if time_over > threshold_time_over:
            print(f"CoreAudioD is running high for more than {threshold_time_over} seconds, restarting EqMac")
            try:
                os.kill(eqmac_pid, signal.SIGKILL)
                time_over = 0
                restart_eqmac(username)
            except OSError:
                print(f"Error restarting EqMac: {eqmac_pid}")
                pass

        # Sleep for a while to avoid busy waiting
        sleep(sleep_time)


# Entry point of the script
if __name__ == "__main__":
    main()