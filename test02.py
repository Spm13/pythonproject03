#การรับค่าข้อมูลทางแป้นพิมพ์ด้วย python
name = input('ป้อนชื่อ : ')
yearborn = input('ป้อนปีเกิด : ')
print('---------------')
#ฟังก์ชันในการแปลงข้อมูลจากข้อความเป็นตัวเลข int( ), float( )
#ฟังก์ชันในการแปลงข้อมูลจากข้อตัวเลขเป็นข้อความ str( ), float( )
print(f'ยินดีต้อนรับคุณ {name} เกิดปี {yearborn} อายุ {2023 - int(yearborn) }')
print('ยินดีต้อนรับคุณ',name,'เกิดปี' ,yearborn, 'อายุ' ,2023 - int(yearborn))
print('ยินดีต้อนรับคุณ '+name+' เกิดปี '+yearborn+' อายุ ' +str(2023-int(yearborn)))
print('ยินดีต้อนรับคุณ {} เกิดปี {} อายุ {}'.format(name,yearborn,2023 - int(yearborn)))
print('ยินดีต้อนรับคุณ %s เกิดปี %s อายุ %d'%(name,yearborn,2023 - int(yearborn)))