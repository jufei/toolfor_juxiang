
welcome_str = '''
————————————————————————————————————————————————————————
我是数学小能手，我能帮你什么？

1) 计算圆
2) 计算长方体


请输入您的选择：
'''

PI = 3.14

def bianhaokan(value):
	return round(value, 4)

def jisuan_yuan(banjin):
	mianji = round(PI * banjin * banjin, 2)
	zhouchang = round(2 * PI * banjin, 2)
	return mianji, zhouchang	

def jisuan_changfangti(chang, kuan, gao):
	biao_miaoji = bianhaokan((chang * kuan + chang * gao + kuan * gao) * 2)
	lengchang = bianhaokan((chang + kuan + gao) * 4)
	tiji = bianhaokan(chang * kuan * gao)
	return biao_miaoji, lengchang, tiji

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

def huan_danwei_to_cm(shuruzhi):
	danwei = read_danwei(shuruzhi)
	if danwei == '':
		return shuruzhi
	elif danwei == 'm':
		return float(shuruzhi.replace('m', '')) * 100
	elif danwei == 'dm':
		return float(shuruzhi.replace('dm', '')) * 10
	elif danwei == 'cm':
		return float(shuruzhi.replace('cm', ''))
	else:
		print('我不认识你的单位啊！')

danwei_liebiao = {
	'm': '米',
	'dm': '分米',
	'cm': '厘米',
}

while True:
	xuanze = input(welcome_str)
	if xuanze == '1':
		banjin = input("请输入圆的半径，如3cm，默认单位是cm：")
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
	elif xuanze == '2':
		chang = huan_danwei_to_cm(input('请输入长方体的长，如3cm，默认单位是cm：'))
		kuan = huan_danwei_to_cm(input('请输入长方体的宽，如3cm，默认单位是cm：'))
		gao = huan_danwei_to_cm(input('请输入长方体的高，如3cm，默认单位是cm：'))

		biao_miaoji, lengchang, tiji = jisuan_changfangti(chang, kuan, gao)
		print('长方体的表面积是：{}平方厘米，棱长之和是：{}厘米，体积是：{}立方厘米'.format(
			biao_miaoji, lengchang, tiji))
	else:
		print('！！！  你输错了，眼睛睁大点。 ！！！')

