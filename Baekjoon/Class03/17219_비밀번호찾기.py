import sys
n, m = map(int, sys.stdin.readline().split())
pwd = {}
for _ in range(n):
    site_pwd = sys.stdin.readline().split()
    if site_pwd[0] not in pwd:
        pwd[site_pwd[0]] = site_pwd[1]
for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(pwd[site])