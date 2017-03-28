import requests

API_KEY = "trnsl.1.1.20170328T091606Z.27d989b564203909.e9dc3d53af21dfcfb3ac0bd40a711a13e0cb6624"
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"

news_files = {
    "DE.txt": "de",
    "ES.txt": "es",
    "FR.txt": "fr",
}


# функция осуществляющая перевод через API Яндекса (из лекции)
# пример использования: print(translate("Привет, как дела?", "ru", "en"))
def translate(text, from_lang, to_lang):
    parameters = {
        "key": API_KEY,
        "text": text,
        "lang": "{}-{}".format(from_lang, to_lang),
    }
    response = requests.get(URL, params=parameters)
    response_json = response.json()
    return "".join(response_json["text"])


# функция чтения строк из файла, перевода и записи результата в файл
# пример использования: print(file_to_translate("DE.txt", "de", "ru"))
def file_to_translate(file_name, from_lang, to_lang="ru", destination_file=""):
    if destination_file == "":
        destination_file = file_name + "." + from_lang + "-" + to_lang + ".txt"
    text = ""
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            text += translate(line, from_lang, to_lang)
    with open(destination_file, "w", encoding="utf-8") as file:
        file.write(text)
    return destination_file


# функция для перевода подготовленных файлов из задания №2
def news_files_translate(news_files):
    for file_name in news_files:
        from_lang = news_files[file_name]
        file_to_translate(file_name, from_lang)


# функция для ввода имени исходного файла, имени файла для результата, языка с какого на какой переводить
def translate_input():
    file_name = str(input("Введите имя файла для перевода:"))
    destination_file = str(input("Введите имя файла для результата:"))
    from_lang = str(input("Введите язык оригинала:"))
    to_lang = str(input("Введите язык перевода:"))
    file_to_translate(file_name, from_lang, to_lang, destination_file)


news_files_translate(news_files)

translate_input()


