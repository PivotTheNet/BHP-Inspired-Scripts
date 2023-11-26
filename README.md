# BHP-Inspired-Scripts
Python scripts inspired by the book "Black Hat Python".

1. [TCP Client](https://github.com/PivotTheNet/BHP-Inspired-Scripts/blob/main/tcp-client.py) script inspired from BHP book.
    1. Added arguments, error handling, ssl, input validation, etc
    2. Planning to add UDP capabilities to this script, which will cover the UDP script in BHP.

2. [TCP-UDP-Client](https://github.com/PivotTheNet/BHP-Inspired-Scripts/blob/main/TCP-UDP-client.py) script is an updated version of the previously made TCP-Client script but includes:
    1. UDP capability.
    2. Removal of 443 if condition. -s, -ssl option is now required if running on any port requiring ssl(e.g. 443).
    3. Forced requirements for hostname/IP and port number.
    4. Optional arguments: -u, -UDP and -s, -ssl added.

3. [TCP-Server](https://github.com/PivotTheNet/BHP-Inspired-Scripts/blob/main/tcp-server.py) script is based off the version from the BHP book.

