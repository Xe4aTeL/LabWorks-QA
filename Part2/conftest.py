import paramiko
from subprocess import Popen, PIPE
import pytest


# Config
server_ip = ''
username = ''
password = ''


@pytest.fixture(scope='function')
def server():
	""" Connects to a server via SSH and starts iperf server """
	client = paramiko.client.SSHClient()
	client.load_system_host_keys()
	try:
		client.connect(hostname=server_ip, username=username, password=password)
		assert client, "Client is empty"
		stdin, stdout, stderr = client.exec_command('iperf -s -t 10')
		error = stderr.read().decode('utf-8', errors='replace')
	except paramiko.ssh_exception.AuthenticationException:
		assert False, "Misconfigured SSH data"
		exit(1)
	finally:
		client.close()

	return error if error else None


@pytest.fixture(scope='function')
def client(server):
	""" Opens termainal with subprocess.Popen and runs iperf command """
	server_error = server
	command = ["iperf", "-c", server_ip, "-i", "1", "-t", "5"]
	# print(command)
	proc = Popen(command, stdout=PIPE, stderr=PIPE)
	output, error = proc.communicate()
	return output, error, server_error
