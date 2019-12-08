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
	sum_len = sum_len + len(d)
print('平均每筆留言長度', sum_len/len(data))