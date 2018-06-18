#!/usr/bin/env python

# chunks of this are directly from https://wiki.python.org/moin/BaseHttpServer

import time
import BaseHTTPServer
import cookies

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

    POSSIBLE_COOKIES = cookies.getcookies()

def main(): 
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

if __name__ == '__main__':
    main()
