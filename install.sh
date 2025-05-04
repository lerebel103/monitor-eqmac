#!/usr/bin/env sh
# Installs the files require to run as a laucnh daemon on MacOS

# check if we are running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

bin_dir=/usr/local/bin/monitor_eqmac

# copy exec environment to /usr/local bin dir
if [ ! -d $bin_dir ]; then
  mkdir $bin_dir | true
fi
cp -r .venv main.py monitor_eqmac.sh $bin_dir/
chmod +x $bin_dir/monitor_eqmac.sh
chown -R root:wheel $bin_dir

# create the launch daemon and run it
cp com.willc.monitor_eqmac.plist /Library/LaunchDaemons/
chown -R root:wheel /Library/LaunchDaemons/com.willc.monitor_eqmac.plist
launchctl load -w /Library/LaunchDaemons/com.willc.monitor_eqmac.plist

