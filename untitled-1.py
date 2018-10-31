dic = {
    'age': 23,
    'city': 'beijing',
    'skill': 'python'
}

fw = open("test.txt", 'w+')
fw.write(str(dic))
fw.close()

fr = open("test.txt", 'r+')
dic = eval(fr.read())
print(dic)
fr.close()
print(dic['age'])
