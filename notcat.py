import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading


def execute(cmd: str) -> str:
    """Executes a command and returns the output as a string."""
    cmd = cmd.strip()
    if not cmd:
        return 'RJG Error'
    output = subprocess.check_output(shlex.slpit(cmd), stderr=subprocess.STDOUT)
    return output.decode()


def main():
    pass


if __name__ == "__main__":
    main()