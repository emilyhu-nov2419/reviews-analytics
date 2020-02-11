data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是餘數
			print(len(data)) #把進度顯示出來
print('檔案讀取完了,總共有', len(data), '筆資料')
print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #len(d)每一筆多少字
print('平均每筆留言長度', sum_len/len(data)) #len(data)這份檔案有多少筆

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) #印出第一筆小於100的留言

good = []
for d in data: #if 後面放是非題
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0]) #印出第一筆有good的留言


#文字計數
wc = {}# word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進字典
for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input ('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')

