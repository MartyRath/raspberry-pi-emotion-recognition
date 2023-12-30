#!/bin/bash

# Start bluetoothctl and execute commands
bluetoothctl << EOF
devices
scan on
pair 30:50:75:8F:A1:B8
exit
EOF
