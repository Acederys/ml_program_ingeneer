# Переводчик с английского на русский

Проект разработан как итогое задание по дисциплине "Программная инженерия"

### Цель проекта 

разработать Web или API приложение машинного обучения и развернуть его в облаке

Приложение реализовано с помощью готовой модели **Helsinki-NLP/opus-mt-en-ru**
Было реализование приложение с помощью streamlit на платформе streamlit.io  и доступно по ссылке : ![ https://appmainpy-mbbh62xrjoaxv9udvsthwj.streamlit.app/)](https://appmainpy-mbbh62xrjoaxv9udvsthwj.streamlit.app/)

### Использование

Было преализовано с помощью библиотеки Streamlit прикрепление файла, который необходимо перевести. Файл в формате *.txt* перемещается или ищется через поле Browse file.
![Browse file](https://github.com/Acederys/ml_program_ingeneer/blob/master/image_readme/%D0%9A%D0%BE%D0%BF%D0%B8%D1%8F%202023-10-30_11-45-50.png)
Отображается содержимое файла и при нажании на кропку *TRANSLATE* осуществляется передача текста в готовую модель **Helsinki-NLP/opus-mt-en-ru** (использование через применение pipeline). Отображение результата происходит в *.caption* ниже.
![Перевод](https://github.com/Acederys/ml_program_ingeneer/blob/master/image_readme/2023-10-30_11-46-08.png)

#### Примечание

В проекте применены тесты *streamlit.testing.v1*

## Было реализование приложение с помощью fastAPI с методом POST.

### Запуск
- Запустить терминал. Зайти в папку, где расположен файл API_main.py
- Используй в консоли команду python *-m pip install -r requirements.txt* для установки необходимых библиотек
- У вас дожен быь установлен uvicorn. *(pip install uvicorn)*
- Введите в командной строке *uvicorn API_main:app*
- Выведется что открылся на *http://127.0.0.1:8000*
- Используйте в командной строке *curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text":"I live in Moscow"}'*
- "text": "Можно вводит произвольный текст"
