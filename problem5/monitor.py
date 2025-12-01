import paramiko
import time
import re
 
# SSH connection details
HOST = "10.81.1.116"
USERNAME = "interns"
PASSWORD = "123123"
ALERT_LOG = "alerts.log"
 
CPU_THRESHOLD = 80
DISK_THRESHOLD = 90
 
def get_cpu_usage(output):
    for line in output.splitlines():
        if "%Cpu(s)" in line:
            match = re.search(r'(\d+\.\d+)\s*id', line)
            if match:
                idle = float(match.group(1))
                return 100 - idle
    return 0
 
def get_disk_usage(output):
    parts = output.split()
    if len(parts) >= 5:
        usage_str = parts[4]
        if usage_str.endswith("%"):
            return float(usage_str.strip("%"))
    return 0
 
def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST, username=USERNAME, password=PASSWORD)
 
    channel = ssh.invoke_shell()
    time.sleep(1)
    channel.recv(9999)
 
    while True:
        try:
            channel.send("top -bn1 | head -5\n")
            time.sleep(1)
            output = channel.recv(9999).decode()
            cpu_usage = get_cpu_usage(output)
 
            channel.send("free -m\n")
            time.sleep(1)
            mem_output = channel.recv(9999).decode()
 
            channel.send("df -h | tail -1\n")
            time.sleep(1)
            disk_output = channel.recv(9999).decode()
            disk_usage = get_disk_usage(disk_output)
 
            print(f"CPU Usage: {cpu_usage:.2f}%")
            print(mem_output)
            print(f"Disk Usage: {disk_usage:.2f}%")
 
            alerts = []
            if cpu_usage > CPU_THRESHOLD:
                alerts.append(f"CPU usage high: {cpu_usage:.2f}%")
            if disk_usage > DISK_THRESHOLD:
                alerts.append(f"Disk usage high: {disk_usage:.2f}%")
 
            if alerts:
                with open(ALERT_LOG, "a") as f:
                    for alert in alerts:
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {alert}\n")
                print("Alerts written to log!")
 
            time.sleep(5)
 
        except KeyboardInterrupt:
            print("Monitoring stopped.")
            break
        except Exception as e:
            print("Error:", e)
            break
 
    channel.close()
    ssh.close()
 
if __name__ == "__main__":
    main()
 