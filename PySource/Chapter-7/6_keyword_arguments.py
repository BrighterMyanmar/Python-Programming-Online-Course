def connect(ipAddress,protocol,port):
    base_url = f"{protocol}://{ipAddress}:{port}"
    print(base_url)

connect("http","192.168.100.9","3000")
connect(ipAddress="192.68.100.9",port="3000",protocol="http")
connect(port="3000",protocol="WSS",ipAddress="192.168.100.9")
connect("192.168.100.9",protocol="http",port="3000")