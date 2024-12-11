# LabWorks-QA


## Description
This is a project for Lab Work 8 for QA subject (GlobalLogic Certificate Program).

## Dependencies:
- Python3
- Standard libs: subprocess, re, copy
- paramiko
- pytest
- iperf

## Supported Features
- test network connectivity with iperf
- ssh into server(to bring up iperf server) via paramiko
- only tcp protocol

## TestCase
The program tests iperf connection between a client and a server. A server is accessed via SSH, which means configuring ip, username and password inside
conftest.py. Then, a client connects to a server, and output of stdout of client and stderr of both client and server is done.
Parser converts recieved values, and testcase checks for
- No server error has occured
- No client error has occured
- Client output has data
Lastly, the output data is printed and the test passes. Due to poor network condition while perfroming tests, program doesn't check for network bitrate
over the whole test period.

## Done by a student:
Skorobagatko Ivan IO-13