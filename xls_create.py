import xlwt
from datetime import datetime

wb = xlwt.Workbook()
ws = wb.add_sheet("Filatov's Sheet")
# style1 = xlwt(num_format_str='DD-MM-YY')
style1 = xlwt.XFStyle()
style1.num_format_str = 'DD-MM-YY'

ws.write(1, 1, 'Today is:')
ws.write(1, 2, datetime.now(), style1)
text = "and I'm a King :)"
text_length = len(text)
ws.write(1, 3, text)

wb.save('FVV.xls')
