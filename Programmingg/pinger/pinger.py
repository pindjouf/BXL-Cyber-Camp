import threading
from pythonping import ping
import ipaddress
from progress.bar import Bar

def generate_ip(a):
    for b in range(256):
        for c in range(256):
            for d in range(256):
                ip = ipaddress.ip_address(f"{a}.{b}.{c}.{d}")
                if not ip.is_private:
                    response = ping(str(ip), count=1)
                    with open("ips.txt", "a") as f:
                        f.write(f"{ip}: {str(response)}\n")

threads = []
for i in range(256):
    thread = threading.Thread(target=generate_ip, args=(i, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Well done ;)")


