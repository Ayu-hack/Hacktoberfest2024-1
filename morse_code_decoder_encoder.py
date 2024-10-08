MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

def encrypt(message): 
    """Encrypt the message to Morse code."""
    cipher = ''
    for letter in message: 
        if letter in MORSE_CODE_DICT:  # Check if letter is valid
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            print(f'This: {letter} could not be converted into Morse code, removing it from the message')
    return cipher.strip()  # Remove trailing space

def decrypt(message): 
	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 
		if (letter != ' '): 
			i = 0
			citext += letter 
		else: 
			i += 1
			if i == 2 : 
				decipher += ' '
			else: 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher 
switch = input("Enter 1 for encryption and 2 for decryption: ")
if switch == '1':
    message = input("Enter the message you want to encrypt(press enter for default input): ")
    if not message:
        print("No inputs detected so we are using default input 'Rohit'")
        message = 'Rohit'
    result = encrypt(message.upper()) 
    print (result)

else:
    message = input("Enter the message you want to decrypt(press enter for default message): ")
    if not message:
        print("No inputs detected so we are using default input '.--. -.-- - .... --- -.'")
        message = '.--. -.-- - .... --- -.'
    result = decrypt(message) 
    print (result)
	