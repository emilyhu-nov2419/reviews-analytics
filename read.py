data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是餘數
			print(len(data)) #把進度顯示出來
print('檔案讀取完了,總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #len(d)每一筆多少字
print('平均每筆留言長度', sum_len/len(data)) #len(data)這份檔案有多少筆

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])