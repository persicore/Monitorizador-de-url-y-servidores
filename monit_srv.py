import asyncio
import subprocess
import platform
import socket


servers = [
    {'ip': '192.168...', 'port':"Prueba" },
   
]

async def check_server_status(server):
   
    def ping_server(server):
       
        ping_param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        args = "ping " + " " + ping_param + " " + server['ip']
        need_sh = False if platform.system().lower() == "windows" else True

        return subprocess.call(args, shell=need_sh) == 0

    if ping_server(server):
        return f"{server['ip']}:{server['port']} - Status: UP"
    else:
        return f"{server['ip']}:{server['port']} - Status: DOWN (No response to ping)"
async def monitor_servers():
   
    while True:
        tasks = [check_server_status(server) for server in servers]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)
        await asyncio.sleep(60) 
if __name__ == '__main__':
    asyncio.run(monitor_servers())
