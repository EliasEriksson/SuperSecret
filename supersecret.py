# def base_n(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
# 	return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def encode(message,pin=1337):
	pin = str(pin)
	code_message = ""
	for letter_index in range(len(message)):
		if (letter_index) % 4 == 0:
			code_message+=hex(ord(message[letter_index])*(2**int(pin[0])))
		elif (letter_index+3) % 4 == 0:
			code_message+=hex(ord(message[letter_index])*(2**int(pin[1])))
		elif (letter_index+2) % 4 == 0:
			code_message+=hex(ord(message[letter_index])*(2**int(pin[2])))
		elif (letter_index+1) % 4 == 0:
			code_message+=hex(ord(message[letter_index])*(2**int(pin[3])))
	message = code_message
	code_message = ""
	for string in message.split("0x"):
		if string == "":
			pass
		else:
			code_message+= "h" + string
	return code_message

def decode(code_message,pin=1337):
	pin = str(pin)
	message = ""
	for string in code_message[1:].split("h"):
		message += "0x"+string
	code_message = message[2:].split("0x")
	message = ""
	for string_index in range(len(code_message)):
		if string_index % 4 == 0:
			message+=chr(int(int("0x"+code_message[string_index],16)/(2**int(pin[0]))))
		elif (string_index+3) % 4 == 0:
			message += chr(int(int("0x" + code_message[string_index], 16) / (2 ** int(pin[1]))))
		elif (string_index+2) % 4 == 0: #fuckar
			message += chr(int(int("0x" + code_message[string_index], 16) / (2 ** int(pin[2]))))
		elif (string_index+1) % 4 == 0:
			message += chr(int(int("0x" + code_message[string_index], 16) / (2 ** int(pin[3]))))
	return message

if __name__ == "__main__":
	# print(decode())
	pass