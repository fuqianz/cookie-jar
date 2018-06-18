#!/usr/bin/env python

import socket
from random import randint
from time import sleep
import cookies

POSSIBLE_COOKIES = cookies.getcookies()

def send_request(cookie): 
    kukki = 'user=' + cookie
    try: 
        goofus_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        goofus_socket.connect(('172.21.3.200', 80))
        hdr_start = 'GET /admin.html HTTP/1.1\nHost: 192.168.1.7\nCookie: '
        request = hdr_start + kukki + '\n\n'
        goofus_socket.send(request)
    except socket.error: 
        print 'Could not connect...'
    sleep(1)

def pick_cookie():
    return POSSIBLE_COOKIES[randint(0, 49)]

if __name__ == '__main__':
    while True:  
        current_cookie = pick_cookie()
        for x in range(0, 10):
            send_request(current_cookie)
            sleep(5)
    print 'Finishing due to keyboard interrupt.'

