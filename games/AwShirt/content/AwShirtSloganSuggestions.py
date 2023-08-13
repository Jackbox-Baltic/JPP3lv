import json

# Открываем файл AwShirtSloganSuggestions1.json для чтения с явным указанием кодировки
with open('AwShirtSloganSuggestions1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразуем данные
converted_data = {
    "episodeid": 1266,
    "content": [
        {
            "suggestion": item["suggestion"],
            "id": int(item["id"]),
            "type": item["type"]
        }
        for item in data["content"]
    ]
}

# Записываем преобразованные данные в файл AwShirtSloganSuggestions3.json с отключенной экранировкой Unicode символов
with open('AwShirtSloganSuggestions3.json', 'w', encoding='utf-8') as file:
    json.dump(converted_data, file, ensure_ascii=False, indent=4)
