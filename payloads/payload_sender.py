import socket

def send_payload(jar_path, host, port=50000):
    with open(jar_path, 'rb') as f:
        data = f.read()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(data)
    sock.close()
    print(f"Sent {len(data)} bytes to {host}:{port}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        host = sys.argv[1]
        port = int(sys.argv[2]) if len(sys.argv) > 3 else 50000
        send_payload(sys.argv[3], host, port)
    else:
        print("Usage: python payload_sender.py <host> <port> <js_file>")
        print("Examples:")
        print("  python payload_sender.py 192.168.1.100 helloworld.js")
        print("  python payload_sender.py 192.168.1.100 50000 helloworld.js")
        print("  python payload_sender.py 192.168.1.100 9020 payload.bin")
