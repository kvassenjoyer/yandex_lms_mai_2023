# Обработка ошибок

try:
    func()
except Exception as e:
    print(e.__class__.__name__)
else:
    print("No Exceptions")
