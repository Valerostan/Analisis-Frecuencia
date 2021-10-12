file_path = '/home/valentina/lab2/eje1/original_message.txt'
freq = [0 for _ in range(26)]

length=0
for line in open(file_path).readlines():
	for word in line.split():
		for letter in word:
			if(letter.isalpha()):
				length=length + 1
				if (letter != 'v'):
					index = ord(letter) - ord('A')
					freq[index] = freq[index] + 1
print(freq)

message_freq_order = []

for i in range(26):
	porcentaje= (freq[i]/length)*100
	message_freq_order.append([chr(i + ord('A')), porcentaje])

print(message_freq_order)
