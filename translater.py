print("Loading Script..")

from deep_translator import GoogleTranslator


def print_languages():
    print("Доступные языки:")
    print("ru: русский")
    print("en: английский")
    print("eu: баскский")

def translate_text():
    print_languages()
    
    src_lang = input("Введите код языка оригинала (например, 'en' для английского): ")
    dest_lang = input("Введите код языка для перевода (например, 'ru' для русского): ")
    text = input("Введите текст для перевода: ")
    
    try:
        translation = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        print(f"Перевод: {translation}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    translate_text()
