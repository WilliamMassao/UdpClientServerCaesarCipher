from socket import *
serverName = "127.0.0.1" # IPv4 // ::1 IPv6
serverPort = 12503
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")

def encrypt_cesar(message, shift):
    encrypted_message = ""

    for char in message:
        encrypted_char = chr((ord(char) + shift) % 0x10FFFF)  # Usando 0x10FFFF como limite superior da tabela Unicode
        encrypted_message += encrypted_char

    return encrypted_message

while 1:
    message = input("Input message: ")
    shift = 5
    encryptedMessage = encrypt_cesar(message, shift)
    print("Encrypted Message: ", encryptedMessage)
    if message == "exit":
            break
    clientSocket.sendto(bytes(encryptedMessage,"utf-8"), (serverName, serverPort))
clientSocket.close()

