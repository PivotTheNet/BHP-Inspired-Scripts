#!/bin/python3

# import libraries needed
import socket
import argparse
import ssl
from urllib.parse import urlparse


### Script inspired by BHP book's simple tcp script. Based off previously uploaded tcp-client.py but added:
### UDP and ssl options. Forced placements arguments.
## Uploaded to GitHub on 10-26-23


# cleanup user input and remove unneeded scheme, to avoid errors
def delete_scheme(remove_http):
	url = urlparse(remove_http)
	return url.netloc + url.path


# function for applying UDP or TCP socket, checking for ssl, and sending then receiving data
def run_tcp_client(host, port):
	if (UDP == True):
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	else:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		if (is_ssl_preset == True):
			client.connect((host, port))
			context = ssl.create_default_context()
			client = context.wrap_socket(client, server_hostname=host)
			client.send(f"GET / HTTP/1.1\r\nHost:{host}\r\n\r\n".encode())
		else:
			client.connect((host, port))
			client.send(b"GET / HTTP/1.1\r\nHOST:{host}\r\n\r\n")
		response = client.recv(4096)
		return response.decode("UTF-8")

	except Exception as error:
		return str(error)

# separate code for importing
if __name__ == "__main__":
	# define parser for user input arguments
	parser = argparse.ArgumentParser(add_help=True)
	parser.add_argument("hostname_or_IP", help="Define hostname or IP of target", type=str)
	parser.add_argument("target_port", help="Define target port", type=int)
	parser.add_argument("-u", "--UDP", help="Specify if running UDP protocol. (Default: disabled)", action="store_true")
	parser.add_argument("-s", "--ssl", help="Enable SSL. (Default: disabled)", action="store_true")
	args = parser.parse_args()

	# assign user inputs to variables
	target_host_host = args.hostname_or_IP
	target_target_port = args.target_port
	is_ssl_preset = args.ssl
	UDP = args.UDP

	# run delete_scheme function to cleanup user input
	clean_url = delete_scheme(target_host_host)

	# run defined function above with user input
	response = run_tcp_client(clean_url, target_target_port)

	# print results of main function
	print(f"The response for {target_host_host} is:\n\n {response}")
