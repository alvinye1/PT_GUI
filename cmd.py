#!/usr/bin/python3
import paramiko as pm
import os
import tkinter as tk
import tornado as tn

user = "root"
passwd = 'yelun007'
address = '192.168.31.213'
cmd = pm.SSHClient()
cmd.set_missing_host_key_policy(pm.AutoAddPolicy)
cmd.connect(hostname=address, port=22, username=user, password=passwd)
stdin, stdout, stderr = cmd.exec_command('ifconfig -a')
result = stdout.read()
print(result.decode())
cmd.close()


tk.Button