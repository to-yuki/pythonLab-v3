from googletrans import Translator

translator = Translator()

# 日本語 -> 英語
result = translator.translate('Automate your work with Python.', dest='ja')
print(result.text)

# 英語 -> 日本語
result = translator.translate('Pythonで作業を自動化しましょう。', dest='en')
print(result.text)