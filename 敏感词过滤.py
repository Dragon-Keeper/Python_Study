def text_create(name, msg):   
    desktop_path = '/Users/Hou/Desktop/'    #设定文件位置
    full_path = desktop_path + name + '.txt' #设定文件位置+文件名+后缀名
    file = open(full_path,'w')             #打开文件并用参数w读取（打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。）
    file.write(msg) #写入内容到文件
    file.close() #文件打开了就要关闭
    print('Done')
text_create('hello','hello world') # 调用函数

def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):#分别设定censored_word（被替换）和changed_word（替换的词）
    return word.replace(censored_word, changed_word)#用replace方法将censored_word用changed_word替换
text_filter('Python is lame!')     # 调用函数

def censored_text_create(name, msg):
    clean_msg = text_filter(msg)#调用text_filter函数将单词lame过滤替换后赋值给clean_msg
    text_create(name,clean_msg)#调用text_create函数生成文件并写入过滤替换后的内容
censored_text_create('Try','lame!lame!lame!') # 调用函数 

'''
我们使用第一个函数，将传入的 msg 进行过滤后储存在名为 clean_msg 的变量中，再将传入的 name 文件名参数和过滤好的文本 clean_msg 作为参数传入函数 text_create 中，结果我们会得到过滤后的文本。
''' 