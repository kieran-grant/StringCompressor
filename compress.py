def compress(uncompressed):
	if len(uncompressed) == 0:
		return ('')
		
	else:
		codebook = {chr(i):i for i in range(128)}
		new_entry = 128
		buffer = ''
		output = []
		
		for char in uncompressed:
			buffer += char
			if buffer not in codebook:
				codebook[buffer] = new_entry
				output.append(codebook[buffer[:-1]])
				buffer = char
				new_entry += 1
				
		output.append(codebook[buffer])
		return(output)
			

						
def decompress(compressed):
	c = compressed[:]
	if len(c) == 0:
		return('')
	else:
		codebook = {i:chr(i) for i in range(128)}
		new_entry = 128
		decoded_string = codebook[c.pop(0)]
		output = [decoded_string]
		buffer = ''
		
		for item in c:
			buffer = decoded_string
			if item in codebook:
				decoded_string = codebook[item]
				codebook[new_entry] = (buffer + decoded_string[0])
				new_entry += 1
			else:
				decoded_string = buffer +buffer[0]
				codebook[new_entry] = decoded_string
				new_entry += 1
			output.append(decoded_string)
			
		return(''.join(output))
			
to_compress = 'abcdaaa010201.  63628111abcd'
print(to_compress)
compressed = compress(to_compress)
print(compressed)
decompressed = decompress(compressed)
print(decompressed)
				
