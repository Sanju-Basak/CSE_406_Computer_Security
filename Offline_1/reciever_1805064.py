import socket
import diffie_hellman_1805064 as dh
import aes_1805064 as aes_1805064

# Receiver configuration
HOST = '127.0.0.1'  
PORT = 12345  

# Create a socket object
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
receiver_socket.bind((HOST, PORT))

print('Receiver is listening for incoming connections...')

# Listen for incoming connections
receiver_socket.listen()

# Accept a connection from a sender
sender_socket, sender_address = receiver_socket.accept()
print('Accepted connection from:', sender_address)

# Receive three initial values from the sender
received_values = []
for _ in range(3):
    received_data = sender_socket.recv(1024)
    decoded_value = received_data.decode('utf-8')
    received_values.append(decoded_value)
   
print("Received p, g, A")
p= int(received_values[0])
g= int(received_values[1])
A= int(received_values[2])


b= dh.generate_safe_prime_number(128/2)
B= dh.calculate_public_key(g,p,b)
sender_socket.sendall(str(B).encode('utf-8'))
print("Sent B")

key= dh.calculate_shared_key(A,b,p)
key= str(key)
message= "Ready to receive message"
sender_socket.sendall(str(message).encode('utf-8'))
recieved_message= sender_socket.recv(1024)
recieved_message= recieved_message.decode('utf-8')
print(recieved_message)
while True:


    # Receive the encrypted message from the sender
    encrypted_message = sender_socket.recv(1024)
    encrypted_message = encrypted_message.decode('utf-8')
    print('Received encrypted message:', encrypted_message)

    # Decrypt the message
    [decrypted, decrypted_hex, sum_time_decryption] = aes_1805064.decrypt_text(encrypted_message, key)
    # Print the decrypted message
    print('Decrypted message:', decrypted)

    if decrypted == "exit":
        break

# Close the sender socket
sender_socket.close()

# Close the receiver socket
receiver_socket.close()
