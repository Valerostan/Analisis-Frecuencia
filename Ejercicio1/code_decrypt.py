##frecuencia obtenida
message_freq_order=[['A', 5.845771144278607], ['B', 0.0], ['C', 8.45771144278607], ['D', 2.36318407960199], ['E', 11.691542288557214], ['F', 0.12437810945273632], ['G', 0.6218905472636816], ['H', 3.9800995024875623], ['I', 8.706467661691542], ['J', 6.8407960199004965], ['K', 9.203980099502488], ['L', 0.12437810945273632], ['M', 0.24875621890547264], ['N', 3.9800995024875623], ['O', 1.616915422885572], ['P', 2.736318407960199], ['Q', 1.616915422885572], ['R', 5.099502487562189], ['S', 0.8706467661691543], ['T', 6.7164179104477615], ['U', 0.3731343283582089], ['V', 0.6218905472636816], ['W', 0.0], ['X', 12.810945273631841], ['Y', 0.0], ['Z', 4.72636815920398]] 


file_path = '/home/valentina/lab2/eje1/mensaje.txt'

spanish_freq_order = [['e',16.78],['a',11.96],['o', 8.69],['l',8.37],['s',7.88],['n',7.01],['d',6.87],['r',4.94],['u',4.80],['i',4.15],['t',3.31],['c',2.92],['p',2.776],['m',2.12],['y',1.54],['q',1.53],['b',0.92],['h',0.89],['g',0.73],['f',0.52],['v',0.39],['j',0.30],['ñ',0.29],['z',0.15],['x',0.06],['k',0],['w',0]]


# Las paso a minuscula para evitar conflicto entre letras cambiadas y letras originales
##spanish_freq_order = list(map(str.lower, spanish_freq_order))

lettersUsed = []
minimun = 100
selectedLetter = 'A'
with open(file_path, 'r') as msj:
	message = msj.read()
	message = message.replace('v', '0')
	message = message.upper() 
	message = message.replace('0', 'v')
with open(file_path, 'w') as msj:
	msj.write(message)

for realLetter in spanish_freq_order:
	with open(file_path, 'r') as file :
		data = file.read()
	minimun=100
	for messageLetter in message_freq_order:
		if(messageLetter[0] not in lettersUsed):
			difference = abs(realLetter[1]-messageLetter[1])
			print(messageLetter[0], difference)
			if(difference < minimun): # busca el que tiene mas probabilidad cercana al de la tabla
				minimun = difference
				selectedLetter = messageLetter[0]
				print(selectedLetter)
	lettersUsed.append(selectedLetter)
	print(selectedLetter, realLetter[0]) #cuando encuentra el mas cercano lo remplaza
	data = data.replace(selectedLetter, realLetter[0].lower())
	with open(file_path, 'w') as file:
		file.write(data)


with open(file_path, 'r') as file :
	data = file.read()
	data = data.replace('t','M')
	data = data.replace('k','R')
	data = data.replace('c','P')
	data = data.replace('v','X')
	data = data.replace('b','Q')
	data = data.replace('h','J')	
	data = data.replace('y','B')
	data = data.replace('i','T')
	data = data.replace('l','I')
	data = data.replace('m','P')
	data = data.replace('p','F')
	data = data.replace('j','Z')
	data = data.replace('f','H')
	data = data.replace('r','C')
	data = data.replace('s','N')
	data = data.replace('b','Q')
	data = data.replace('h','J')	
with open(file_path, 'w') as file:
	file.write(data)

