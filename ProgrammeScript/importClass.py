import ExcelTest.classExcelRead as cxl

path="C:\MSDE\PythonProject\ProgrammeScript\ExcelTest\ExcelOutputExampleRead.xlsx"
print(path)
exl=cxl.ExcelOperation(path)

exl.readExcel()
