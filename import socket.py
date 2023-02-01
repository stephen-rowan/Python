import socket

def get_ip():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Attempt to connect to an IP address on port 1
        s.connect(('10.255.255.255', 1))
        # Retrieve the local IP address of the socket
        IP = s.getsockname()[0]
    except:
        # If the connection is not successful, return the default IP address for localhost
        IP = '127.0.0.1'
    finally:
        # Close the socket
        s.close()
    return IP

def write_ip_to_file():
    # Retrieve the local IP address
    ip = get_ip()
    # Open a file named "ip.txt" in write mode
    with open("ip.txt", "w") as file:
        # Write the IP address along with the explanatory text to the file
        file.write("This is your IP Address: " + ip)

# Call the function to write the IP address to the file
write_ip_to_file()



