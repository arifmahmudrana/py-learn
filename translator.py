from translate import Translator
to_lang = 'it'
translator = Translator(to_lang=to_lang)

with open(f'translate-{to_lang}.txt', mode='w') as writer:
    writer.write('')

try:
    with open('translate.txt', mode='r') as reader:
        # print(reader.read())
        while True:
            line = reader.readline()
            if line is '':
                break
            translated_text = translator.translate(line)
            print(line, translated_text)
            with open(f'translate-{to_lang}.txt', mode='a') as writer:
                print(translated_text, file=writer)
except Exception as err:
    print(err)
