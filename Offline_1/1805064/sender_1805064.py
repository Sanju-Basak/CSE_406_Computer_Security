import socket
import diffie_hellman_1805064 as dh
import aes_1805064 as aes

# Sender configuration
HOST = '127.0.0.1' 
PORT = 12345 

# Create a socket object
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the receiver
sender_socket.connect((HOST, PORT))
print('Connected to receiver:', HOST, PORT)

p= dh.generate_safe_prime_number(128)
g= dh.generate_generator(p)
a= dh.generate_safe_prime_number(128/2)
b= dh.generate_safe_prime_number(128/2)
A= dh.calculate_public_key(g,p,a)
print("Generated p, g, a, A")


values= [p,g,A]

for value in values:
    encoded_value = str(value).encode('utf-8')
    sender_socket.sendall(encoded_value)
    print('Sent value:', value)

B= int(sender_socket.recv(1024).decode('utf-8'))
print("Received B")

key= dh.calculate_shared_key(B,a,p)
key= str(key)
message= "Ready to send message"
sender_socket.sendall(str(message).encode('utf-8'))
recieved_message= sender_socket.recv(1024)
recieved_message= recieved_message.decode('utf-8')
print(recieved_message)

while True:
    # Input the message to be encrypted
    message = input("Enter the message to be encrypted: ")

    [encrypted, encrypted_hex, encryption_time] = aes.cipher_text(message, key)

    encoded_message = encrypted_hex.encode('utf-8')
    print('Encrypted message:', encrypted_hex)

    # Send the encrypted message to the receiver
    sender_socket.sendall(encoded_message)

    if message == "exit":
        break

# Close the sender socket
sender_socket.close()
