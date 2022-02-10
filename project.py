from shodan import Shodan
import json, ipaddress

### Reference - https://developer.shodan.io/api/clients
api = Shodan('<API-Key>')
IP = [str(ip) for ip in ipaddress.IPv4Network('<Public IP segment>')] ### example 85.269.45.0/24
PSEARCH = 3389 ## Port to search as a int

def run():
  print("IP Address   | Open Port")
  for item in IP:
    try:
      ipinfo = json.dumps(api.host(item))
      data = json.loads(ipinfo)['data']
      ipAddr = [ipinfo['ip_str'] for ipinfo in data]
      ports = [ipinfo['port'] for ipinfo in data]
      for ip, port in zip(ipAddr, ports):
        if port == PSEARCH:
          print(ip, "   | ", port)
    except:
      pass

if __name__ == '__main__':
  run()
