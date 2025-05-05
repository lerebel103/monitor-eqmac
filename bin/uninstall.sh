#!/usr/bin/env sh
# Uninstall this utility from the system

# check if we are running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

bin_dir=/usr/local/bin/monitor_eqmac

launchctl unload -w /Library/LaunchDaemons/com.willc.monitor_eqmac.plist
rm -f /Library/LaunchDaemons/com.willc.monitor_eqmac.plist
rm -rf $bin_dir
