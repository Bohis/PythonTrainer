def Logger(message, nameFile):
    file = open(nameFile,"a")
    file.write(message + "\n")
    file.close()