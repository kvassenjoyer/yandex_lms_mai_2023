# Ломать — не строить

try:
    func(None, {"один": "два"})
except Exception:
    print("Ура! Ошибка!")
