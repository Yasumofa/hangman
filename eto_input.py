year_str = input('あなたの西暦')
year = int(year_str)
number_of_eto = (year + 8) % 12
eto_tuple = ('子', '牛', '寅', '兎', '辰', '巳年', '午', '羊', '申年', '酉年', '戌', 'いのしし')
eto_name = eto_tuple[number_of_eto]
print('あなたの干支の順番は', eto_name, '番目なのだよ。')
