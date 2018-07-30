
welcome_str = '''
————————————————————————————————————————————————————————
我是数学小能手，我能帮你什么？

1) 计算圆
2) 计算长方体


请输入您的选择：
'''

PI = 3.14

def jisuan_yuan(banjin):
	mianji = round(PI * banjin * banjin, 2)
	zhouchang = round(2 * PI * banjin, 2)
	return mianji, zhouchang	

def read_danwei(shuruzhi):
	if 'cm' in shuruzhi:
		danwei = 'cm'
	elif 'dm' in shuruzhi:
		danwei = 'dm'
	elif 'm' in shuruzhi:
		danwei = 'm'
	else:
		danwei = ''
	return danwei

danwei_liebiao = {
	'm': '米',
	'dm': '分米',
	'cm': '厘米',
}

while True:
	xuanze = input(welcome_str)
	if xuanze == '1':
		banjin = input("请输入圆的半径：")
		danwei = read_danwei(banjin)

		if danwei != '':
			zheng_banjin = banjin.replace(danwei, '') 
			zhongwen_danwei = danwei_liebiao[danwei]
		else:
			zheng_banjin = banjin
			zhongwen_danwei = ''

		area, zhouchang = jisuan_yuan(float(zheng_banjin))
		print('半径为 {}{} 的圆，它的面积是： {} 平方{}，它的周长是： {} {}。'.format(
			zheng_banjin, zhongwen_danwei, area, zhongwen_danwei, zhouchang, zhongwen_danwei))

