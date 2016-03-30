MSGLEN = 64

def pad(message, length=MSGLEN):
	assert len(message) <= length, 'Message is longer than the provided length! %d > %d' % (len(message), length)

	pad_len = length - len(message)
	tokens = [' ' for x in range(pad_len)]
	
	return message + ''.join(tokens)
