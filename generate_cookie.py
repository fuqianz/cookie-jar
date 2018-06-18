#!/usr/bin/env python

import random

cookies = ['YzgzZWM0MWViMzJhNGYzMzdmOTM5Y2MxZGE3MDRiZDMK', 
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

print (len(cookies))
lens = len(cookies)
COOKIE_NUM = 100

for i in range(0, COOKIE_NUM - lens) :
    strlist = [a for a in cookies[i] ]
    random.shuffle(strlist)
    cookie = ''.join(strlist)
    print (cookies[i])
    print (cookie)
    cookies.append(cookie)

with open('./cookies.txt', 'w') as f:
    for cookie in cookies:
        f.write('\'' + cookie + '\',' + '\n')
