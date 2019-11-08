import paramiko
import threading
import subprocess

from config.chap2 import TEST_HOST_IP
from config.chap2 import TEST_HOST_USER
from config.chap2 import TEST_HOST_PASSWORD


def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # Authentication with keys
    # client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
    return


if __name__ == '__main__':
    ssh_command(TEST_HOST_IP, TEST_HOST_USER, TEST_HOST_PASSWORD, 'id')
