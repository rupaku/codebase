from translate import Translator
translator=Translator(to_lang='ja')
try:
    with open('file1.txt','r') as file:
        text=file.read()
        translation=translator.translate(text)
        with open('./text-ja.txt','w') as my_file:
            my_file.write(translation)
except FileNotFoundError as err:
    print('check your file')