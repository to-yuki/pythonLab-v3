from googletrans import Translator

translator = Translator()

# 英語 -> 日本語
result = translator.translate(text='Automate your work with Python.', dest='ja')
print(result.text)

# 日本語 -> 英語
result = translator.translate(text='Pythonで作業を自動化しましょう。', dest='en')
print(result.text)