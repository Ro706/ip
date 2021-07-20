import socket
def find_id():
  host = socket.gethostname()
  ip_add = socket.gethostbyname(host)
  
  print(f'host : {host}')
  print(f'ip address : {ip_add}')

if __name__ == '__main__':
  find_id()
