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


class NotCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        pass


    def listen(self):
        pass

def main():
    parser = argparse.ArgumentParser(
        description='RJAG Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
            Example:
                notcat.py -t 192.168.1.108 -p 5555 -l -c  # command shell
            All commands:
                -c shell
                -e execute
                -l listen
                -p port
                -t target
                -u upload
        ''')
    )
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('l', '--listen', action='store_true', help='listen')
    parser.add_argument('p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('t', '--target', default='192.168.1.203)', help='speicifed ip')  # Why this default?
    parser.add_argument('u', '--upload', help='upload file')

    args = parser.parse_args()

    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

        nc = NotCat(args, buffer.encode())
        nc.run()


if __name__ == "__main__":
    main()