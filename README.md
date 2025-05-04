# Automatically restarts EqMac when it becomes unresponsive

A Python-based utility to monitor the `CoreAudioD` process on macOS and restart the `EqMac` application if the CPU usage exceeds a defined threshold.

It appears that `EqMac` can become unresponsive and cause the `CoreAudioD` process to consume excessive CPU resources, leading to system slowdowns. This utility helps mitigate that issue by automatically restarting `EqMac` when necessary.
It is installed as a macOS launch daemon, ensuring it runs in the background and monitors the `CoreAudioD` process continuously.

As EqMac runs for the user currently logged in, the main.py must be adjusted for the right user. Please see `username` in `main.py`.

As to why this happens, it seems to be a bug in the `EqMac` application itself. The developer has been notified, and several tickets exist on their GitHub page. However, this issue remains unresolved at this time.

## Features

- Monitors the `CoreAudioD` process for high CPU usage.
- Automatically restarts `EqMac` when `CoreAudioD` exceeds the CPU threshold for a specified duration.
- Runs as a macOS launch daemon for continuous monitoring.

## Requirements

- macOS
- Python 3.x
- `psutil` Python library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lerebel103/monitor_eqmac.git
   cd monitor_eqmac
   ```

2. Install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the installation script as root:
   ```bash
   sudo ./install.sh
   ```

   This will:
   - Copy the necessary files to `/usr/local/bin/monitor_eqmac`.
   - Set up a macOS launch daemon using `com.willc.monitor_eqmac.plist`.

## Usage

The script runs automatically as a launch daemon after installation. It monitors the `CoreAudioD` process and restarts `EqMac` when necessary.

To manually start the script:
```bash
python3 main.py
```

## Configuration

You can adjust the following thresholds in `main.py`:

- `username`: The username of the user running `EqMac`. This is necessary to restart the application correctly.
- `threshold_time_over`: Time (in seconds) `CoreAudioD` can exceed the CPU threshold before restarting `EqMac`. Default: `5.0`.
- `threshold_cpu`: CPU usage percentage threshold for `CoreAudioD`. Default: `50`.

## Uninstallation

To remove the utility, run the uninstall script as root:
```bash
sudo ./uninstall.sh
```

This will:
- Unload and remove the launch daemon.
- Delete the installed files.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.