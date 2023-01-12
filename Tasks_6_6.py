# Создать таблицу Excel и конвертировать её в CSV при помощи Python.
import xlsxwriter
import pandas as pd

# открываем новый файл на запись
workbook = xlsxwriter.Workbook('Tasks_6_6.xlsx')

# создаем там "лист"
worksheet = workbook.add_worksheet()

# в ячейку A1 пишем текст
worksheet.write('A1', 'Hello world')

# сохраняем и закрываем
workbook.close()


# Конвертируем с помощью pandas

data_xls = pd.read_excel('Tasks_6_6.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('my_csv.csv', encoding='utf-8')