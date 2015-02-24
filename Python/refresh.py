import win32com.client
from time import sleep


print "Refreshing open_access.xlsx for latest data..."
xl = win32com.client.DispatchEx("Excel.Application")
wb = xl.workbooks.open("C:\Users\sayanigupta\Downloads\open_access.xlsx")
xl.Visible = True
wb.RefreshAll()
sleep(10)
wb.Save()
xl.Quit()
print "Workbook refreshed!"