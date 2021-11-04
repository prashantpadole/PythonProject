from xml.dom import minidom

doc= minidom.parse("C:\MSDE\PythonProject\ProgrammeScript\XMLProcessing\staff.xml")

name=doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs=doc.getElementsByTagName("staff")
for staff in staffs:
    staff_id=staff.getAttribute("id")
    staff_name=staff.getElementsByTagName("name")[0]
    staff_salary=staff.getElementsByTagName("salary")[0]
    print(staff_id," ",staff_name.firstChild.data," ",staff_salary.firstChild.data)


doc= minidom.parse("C:\MSDE\PythonProject\ProgrammeScript\XMLProcessing\data.xml")
countries=doc.getElementsByTagName("country")
print("Run Test 2")
for country in countries:
	countryName=country.getAttribute("name") ## attribute of tag 
	countryRank=country.getElementsByTagName("rank")[0] # it return list so use firtChild.data or for loop
	countryGDP=country.getElementsByTagName("gdppc")[0]
	countryNeighbor=country.getElementsByTagName("neighbor")
	for cn in countryNeighbor:
		countryNeighborName=cn.getAttribute("name")
		countryNeighborDir=cn.getAttribute("direction")
		print(countryName,"|",countryRank.firstChild.data,"|",countryGDP.firstChild.data,"|",countryNeighborName,"|",countryNeighborDir)


