import xml.etree.ElementTree as et


# 生成元素Student
stu = et.Element("Student1")


# 生成 Student 的子元素 Name
name = et.SubElement(stu, 'Name')

# 生成 Name 属性 lang：en
name.attrib = {'lang','en'}

# Name 值
name.text = 'maozedong'

# 生成 Student 的子元素 Age
age = et.SubElement(stu, 'Age')
age.text = 18

et.dump(stu)
