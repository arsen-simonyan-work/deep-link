import http.server
import ssl

# Определяем адрес и порт сервера
server_address = ('localhost', 4443)

# Создаем HTTP-сервер
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Настраиваем SSL-контекст
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.pem")

# Оборачиваем сервер в SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Запуск HTTPS-сервера на https://localhost:4443")
httpd.serve_forever()
