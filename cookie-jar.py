#!/usr/bin/env python

# chunks of this are directly from https://wiki.python.org/moin/BaseHttpServer

import time
import BaseHTTPServer


HOST_NAME = '' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def get_hash_from_Cookie(self):
        the_cookie = self.headers.getheader("Cookie")
        try:
            the_cookie = the_cookie.split('=')
            print the_cookie
            return the_cookie[1]
        except AttributeError:
            return '0'
    def send_200_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_HEAD(self):
        self.send_200_response()
    def do_GET(self):
        """Respond to a GET request."""
        if self.path == '/index.html': 
            self.send_200_response()
            file_html = open('index.html')
            self.wfile.write(file_html.read())
            file_html.close()
        elif self.path == '/admin.html':
            if self.get_hash_from_Cookie() in self.POSSIBLE_COOKIES:
                self.send_200_response()
                file_html = open('admin.html')
                self.wfile.write(file_html.read())
                file_html.close()
            else: 
                self.send_error(403, 'Not Authorized')
        elif self.path == '/key.txt':
            if self.get_hash_from_Cookie() in self.POSSIBLE_COOKIES:
                print "KEY ACCESSED"
                self.send_200_response()
                file_html = open('key.txt')
                self.wfile.write(file_html.read())
                file_html.close()
            else: 
                self.send_error(403, 'Not Authorized')
        elif self.path == '/': 
            self.send_response(301)
            self.send_header("Location", "/index.html")
            self.end_headers()
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    POSSIBLE_COOKIES = ['YzgzZWM0MWViMzJhNGYzMzdmOTM5Y2MxZGE3MDRiZDMK', 
                        'NmMxZmIxYmUwYjE0ZDc4ZmNhNmYwNmI3ZGU4MDhkNGUK', 
                        'MjE4Njg4ZWEwMTUxM2JhODVkOWEzYzhkZWY2NGUyYWMK', 
                        'M2YxMzBhYWRiMTk0NjFkYjE0NjE5NzhjYmY3Y2EzZjcK', 
                        'ODg3MGI4OTNkNWY0YzUyYjQ2YmFkNTc2ZWMzYzEzMTAK', 
                        'NGIxYThiZTg2YmJmY2Q2YzY2MTVmNWZhZGI5NjAxYjkK', 
                        'NTEzOTdkMDFjMDhjMDRmYjllMTA5NGIxNDM1ODE5NWEK', 
                        'OTVhYTc4NjFlMzJmMWU2ODg1ODU2ODMyNmMzODg2MzUK', 
                        'M2YxNjg4ODg0NmFjNTc1MTU3NTNmNGY4MDc5NTBlZmMK', 
                        'MmIzZDNhOTJkMDM2NTIzMmJlNGY1ODNiMzYxNDdiNTcK', 
                        'MjY4YjNhNGQzZjg5ZDRmNTM4YjcyNjBhNDVjYTU2YWIK', 
                        'M2VjODA5Nzg4Y2Y0ZWVhZDZiMGNkMGFkMjllNGVkMmQK', 
                        'ZTRjZDY2M2ZmNzFjZmMzZjZhOTYxNjhlMDhhYjc4ZTYK', 
                        'NDNjM2Y1NjlmMjU3NzY2Njc5ODNkMDE0OTIxZDFmMGEK', 
                        'MmNkZTQyNzViY2MxYWJmYmMyMzI3ZjRiZjM2YWFmYTIK', 
                        'YTgxNGIwNDViNzhkZjg4N2M5NTU0OGMyNTI0NTM5NjQK', 
                        'NjQ1YzM0OWNmMjM0MWIwNDk0MmU1NzgwN2NhNGJmNzEK', 
                        'NzZiNjM0ZmVhZTNjZmE0ZGY4ZDEzMzA1MmUzNmZhZTIK', 
                        'ZmViNTBiOGJhYzIxMDhjNThkMDcyMmFkZWUxZWUwYzYK', 
                        'NDJhOGYyM2E1YWE5MGYxNTc3YmFkNzkwZTM3OWE5MjkK', 
                        'YjBlMmU4ODU5NmU0YjI0MmE4MjNhY2JjYTY3MWM3NWEK', 
                        'ZWYyNjc2ZTU1YmI0MDhjZTA1MzgxOGU3NDJkY2EzZGUK', 
                        'NWYyNDFlMjIyZGYyM2JlNmU5MWM1NzA5YmY2YTllOTQK', 
                        'YTA5NzVhZjA3ZjAyN2YwNzFhY2MxODUxYTM1NGNjNDMK', 
                        'YTE2OTlmODRlMjgzZTk4YzY1ODQ4MmRhNjFmZjhiMjcK', 
                        'NjVkZDEzYWIzN2ZiMDkxOTMzNjczNmE0ZjdjN2JiMzkK', 
                        'N2E2MDdmMWJhZGU0Nzc2ZWNhOTkwZTc3NDA1YzhhMjcK', 
                        'YjFhZDUwYjY4MDkwZWYwYjE5MDAzMDcxNzVjNWE1NTcK', 
                        'NzU4NTJkZTJhYmM2MjViODk2NWQ5YWIzNjY2YmMzYzgK', 
                        'NTVmYjBhYTA2YTIyNTA2MGU1YjU4ZjI1MWQ3NTdlMWEK', 
                        'ZjZlOGYwMTQ3MDhmMjg4NGNmMTc1YTgzNjEwYjU5NWYK', 
                        'MDA0MDFmNTExNzMzMmQwOTVjOTcwYmU0NjAyMjQzNTUK', 
                        'OGJmZDM5NDZjYzEzM2UzY2RhNWEyODc2NDE2NjMwOWIK', 
                        'NDZjYzE0OTFhODkzNjZhMDMxZjNmZjIzN2UxZmMxMmYK', 
                        'ZDVlYTJhNzQ3Y2QxNmYwYjdjOTQ0Yjg2NmMxZGQwNDMK', 
                        'ZjU3MDI5ZmY5ZmZlZGE2ODQ5MWNmZjk1MzJiZDZjN2YK', 
                        'ZDg1NzljN2U5YTI0NWMzMjcwMWQxYTNkYzZhMzY1ZDkK', 
                        'ZjFhMWMyYzZmMDU2ZmFjNTdhZmM5ZDg1ZThmMjAxZTEK', 
                        'MzRmY2VjN2QyYWQ0MGI1ZWY5OTdlZDU0MGQ3NDNmODAK', 
                        'YzQ0MzE1ZWUwMDhjOGNjN2QyYjg0ZTUyZDk1NGZkYmYK', 
                        'YjNhNGU3N2Y5MGZkMGY3OTViNzU4NTEwYzM4MjUyNDYK', 
                        'Njg4YzNlNDNkMWNlODQzYzZiMjFmMTM1NmUzN2YyMTUK', 
                        'NDczMTI4OGYxMjRiYTg1YmZkZjEwMDBlMzQ5MGMwOGIK', 
                        'OGVmZDBmZTI5ZTQxMzczNTI2MjUxNDVhMjZlYjdiYTQK', 
                        'Y2ViMTE5YjQ5MjBjNDU4MmVhMWI0NDE3MmM0MjBjYzAK', 
                        'MjdmYzY4MjM5OGVjNDdmZjJmZDVmYWMxZjRhZjY4YjQK', 
                        'ZTg5ZDUyNGMzYTI3ZGYyN2FkYTdiYTBmODFjNDk2MWQK', 
                        'ZjYyZjVkZDkwOWU2NzdkN2NjOWJhNzBmYjJkYTEyNzQK', 
                        'ZjNkMDBiYjg3NzhlMDhhYzI1YjdhYjRlYjY1YWQwOWQK', 
                        'MWNlOTcwOWI5YTUyYjIzMDk3MzJmYjQ3ODlmOWNlNGMK']

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)