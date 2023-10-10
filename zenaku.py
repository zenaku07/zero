#!/usr/bin/env python3

import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        exit(1)

def main():
    # Update, upgrade, autoclean, and autoremove
    update_upgrade_cmds = [
        "sudo apt update",
        "sudo apt upgrade -y",
        "sudo apt autoclean",
        "sudo apt autoremove -y"
    ]

    for cmd in update_upgrade_cmds:
        run_command(cmd)

    # Check if Neofetch is installed
    neofetch_check = "neofetch --version"
    try:
        subprocess.run(neofetch_check, shell=True, check=True)
        print("Neofetch is already installed.")
    except subprocess.CalledProcessError:
        print("Neofetch is not installed. Installing...")
        # Install Neofetch
        run_command("sudo apt install neofetch -y")

    # Display system information using Neofetch
    run_command("neofetch")

if name == "main":
    main()
