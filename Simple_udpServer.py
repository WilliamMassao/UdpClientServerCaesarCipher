from socket import *
serverPort = 12503
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print ("UDP server\n")

def decrypt_cesar(encrypted_message, shift):
    decrypted_message = ""

    for char in encrypted_message:
        decrypted_char = chr((ord(char) - shift) % 0x10FFFF)
        decrypted_message += decrypted_char

    return decrypted_message


while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8") #cp1252 #utf-8
    shift = 5
    decryptedMessage = decrypt_cesar(text, shift)
    print("Encrypted Message: ", text)
    print ("Received from Client: ", decryptedMessage)