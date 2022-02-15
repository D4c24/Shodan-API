from shodan import Shodan
import json, ipaddress, time

### Reference - https://developer.shodan.io/api/clients
api = Shodan('<API-Key>')
PSEARCH = 3389 ## Port to search as a int

def run():
  print("IP Address   | Open Port")
  for x in range(1, 255):
    value = str(x)
    ipSeg = '85.269.'+value+'.0/24' ### example 85.269.45.0/24
    ipMask = [str(ip) for ip in ipaddress.IPv4Network(ipSeg)]
    time.sleep(1)
    for item in ipMask:
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
