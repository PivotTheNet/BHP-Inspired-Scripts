#!/bin/python3

# import libraries needed
import socket
import argparse
import ssl
from urllib.parse import urlparse


### Script inspired by BHP book's simple tcp-client script.
### Added arguments, ssl, error handling, etc
## Uploaded to GitHub on 11-26-23


# cleanup user input and remove unneeded scheme, to avoid errors
def delete_scheme(remove_http):
	url = urlparse(remove_http)
	return url.netloc + url.path


# function for running sockets against user input. receives, decodes, and returns response. exception for catching errors
def run_tcp_client(host, port):
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
	parser = argparse.ArgumentParser()
	parser.add_argument("hostname_or_IP", help="Define Hostname or IP of target", type=str)
	parser.add_argument("host_port", help="Define Port of target", type=int)
	parser.add_argument("-ssl", "--ssl", help="Enable SSL. (Default: disabled)", action="store_true")
	args = parser.parse_args()

	# assign user inputs to variables
	target_host_host = args.hostname_or_IP
	target_host_port = args.host_port
	is_ssl_preset = args.ssl

	# run delete_scheme function to cleanup user input
	clean_url = delete_scheme(target_host_host)

	# run defined function above with user input
	response = run_tcp_client(clean_url, target_host_port)

	# print results of main function
	print(f"The response for {target_host_host} is:\n\n {response}")
