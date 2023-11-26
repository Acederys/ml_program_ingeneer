<p>Учебное задание</p>  
<h1 align="center">Применение существующей ML модели</h1> <br>

<p>Данный репозиторий написан для выполнения учебно-практической работы по дисциплине "Программная инженерия".</p>
<h2>Задание 3:</h2>
<ul>
<ol>1) С помощью библиотеки FastAPI разработайте API для приложения машинного обучения по вашему выбору.  </ol>
<ol>2) Создайте репозиторий на GitHub, который содержит код реализации API для вашего приложения машинного обучения. Можно использовать репозиторий, который вы создали на предыдущих практических занятиях.  </ol>
<ol>3) В репозитории на GitHub создайте файл requirements.txt со списком всех библиотек, которые необходимо установить для работы API вашего приложения машинного обучения. </ol>
</ul>
<h2>Задача:</h2>
<ul>
<li>Перевод текста с английского на русский, используя готовую модель</li>
</ul>
<p>Было реализование приложение с помощью fastAPI с методом POST.</p>
<h5>Запуск</h5>
<ul>
  <li>Запустить терминал. Зайти в папку, где расположен файл API_main.py</li>
  <li>Используй в консоли команду <code>python -m pip install -r requirements.txt</code> для установки необходимых библиотек</li>
  <li>У вас дожен быь установлен uvicorn. (<code>pip install uvicorn</code>)</li>
  <li>Введите в командной строке <code>uvicorn API_main:app</code></li>
  <li>Выведется что открылся на <code>http://127.0.0.1:8000</code></li>
  <li>Используйте в командной строке 
  <code>curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text":"I live in Moscow"}'</code>
  </li>
  <p>"text": "Можно вводит произвольный текст"</p>
</ul>
<h2>Задание 2:</h2>
<ul>
<ol>1) Выберите предварительно обученную модель машинного обучения, которую вы хотите использовать в своем приложении. </ol>
<ol>2) Разработайте Web-приложение на основе библиотеки Streamlit, которое использует выбранную вами модель. </ol>
<ol>3) Опубликуйте код Web-приложения в репозитории на GitHub </ol>
</ul>
<h2>Задача:</h2>
<ul>
<li>Перевод текста с английского на русский, используя готовую модель</li>
</ul>
<p>Было преализовано с помощью библиотеки Streamlit прикрепление файла, который необходимо перевести. Файл в формате  <code>.txt</code>  перемещается или ищется через поле <code>Browse file</code>. </p>
![Browse file](https://github.com/Acederys/ml_program_ingeneer/raw/master/1.png)
<p>Отображается содержимое файла и при нажании на кропку <code>TRANSLATE</code> осуществляется передача текста в готовую модель <code>Helsinki-NLP/opus-mt-en-ru</code> (использование через применение pipeline). Отображение результата происходит в <code>.caption</code> ниже.</p>
![Перевод](https://github.com/Acederys/ml_program_ingeneer/raw/master/2.png)
<h2>Задание 1:</h2>
<ul>
<ol>1) Изучите возможности готовых библиотек машинного обучения. </ol>
<ol>2) Сформулируйте задачу, которую вы хотите решить с помощью машинного обучения. </ol>
<ol>3) Реализуйте решение выбранной вами задачи в коде с использованием готовой библиотеки машинного обучения. </ol>
<ol>4) Отправьте реализованное решение в репозиторий на GitHub. </ol>
<ol>5) Оформите документацию на ваше решение в репозитории. </ol>
</ul>
<h2>Задача:</h2>
<ul>
<li>Перевод текста с английского на русский, используя готовую модель</li>
<li>Структуризация и классификация текста на русском языке. Синтаксический разбор предложения и вычленения именованных сущностей.</li> 
</ul>
<p>Для перевода текста используется модель <code>blanchefort/rubert-base-cased-sentiment-rurewiews</code> (код оригинальный) или <code>Helsinki-NLP/opus-mt-en-ru</code> (использование через применение pipeline)</p>
<p>Для решения второго пункта задачи лучше всего подходит natasha.</p> 

<h2><b>Применение</b></h2>

<p>Введите текст в консоли. Строка проходит обработку в готовой модели и в Doc объект передается ее перевод.</p>

<h4>Сегментация.</h4> 

<p>Введенный текст будет разделен на токены и предложения. </p>

<h4>Морфология.</h4> 

<p>Для токена будет проведена морфологическая разметка. </p>

<h4>Синтаксис.</h4> 

<p>Для каждого предложена будет предложена схема синтаксической модели.</p> 

<h4>Извлечение именнованных сущностей. </h4>

<p>Предоставляет именнованные сущности по именам, местоположениям и организациям. </p>
