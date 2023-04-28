# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     print(p1)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parse import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
#     pars.get_html()
#     pars.parsing()
#
#
# if __name__ == '__main__':
#     main()


# import socket
#
# URLS = {
#     '/': 'index page',
#     '/blog': 'blog page'
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Non Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     return headers.encode()
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#
#         print(f'Клиент: {addr} => \n{request.decode("utf-8")}\n')
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()

# d = {
#     'a': 45,
#     'b': 2,
#     'c': 17,
#     'd': 3000
# }
#
# def max_zn(obj):
#     l = dict(sorted(obj.items(), key=lambda x: x[1], reverse=True))
#     return list(l.keys())[:2]
#
# print(*max_zn(d))


# import sqlite3
#
# # con = sqlite3.connect('profile.db')
# # cur = con.cursor()
# #
# # con.close()
#
# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data TEXT
#     # )""")
#     cur.execute('DROP TABLE users')

#

# import sqlite3

# with sqlite3.connect('db_4.db') as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5
#     """)
#
#     # res = cur.fetchall()
#     # # print(res)
#     #
#     # for res in cur:
#     #     print(res)
#
#     res = cur.fetchone()
#     print(res)

import sqlite3

cars = [
    ('BMW', 54000),
    ('Chevrolet', 34000),
    ('Daewo', 17000),
    ('Lada', 4000),
    ('Honda', 24000)
     ]

with sqlite3.connect('cars.db') as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)

    for car in cars:
        cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)


    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Bently', 35000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")