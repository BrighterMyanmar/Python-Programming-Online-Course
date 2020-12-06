# positional Parameter
# optional Parameter
def connect(ipAddress,protocol="https",port="3000"):
    BASE_URL = f'{protocol}://{ipAddress}:{port}'
    print(f"Base URL is {BASE_URL}")

connect("192.168.100.9",'http',"4200")