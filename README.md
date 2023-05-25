__PyInstaller__ собирает приложение Python и все его зависимости в единый пакет. Пользователь может запускать упакованное приложение без установки интерпретатора Python или каких-либо модулей. PyInstaller поддерживает Python 3.7 и новее, и корректно собирает многие основные пакеты Python, такие как numpy, matplotlib, PyQt, wxPython и другие.

Установка PyInstaller не отличается от установки любой другой библиотеки Python.

__pip install PyInstaller__

Проверка версии PyInstaller.

__pyinstaller --version__

У меня установка была несколько другой. Саму библиотеку я установил через менеджер библиотек PyCharm, однако внутри него не удалось его адекватно запустить. Пришлось работать с pyinstaller непосредственно через Minicond-у.

PyInstaller собирает в один пакет Python-приложение и все необходимые ему библиотеки следующим образом:

1. Считывает файл скрипта.
2. Анализирует код для выявления всех зависимостей, необходимых для работы.
3. Создает файл spec, который содержит название скрипта, библиотеки-зависимости, любые файлы, включая те параметры, которые были переданы в команду PyInstaller.
4. Собирает копии всех библиотек и файлов вместе с активным интерпретатором Python.
5. Создает папку BUILD в папке со скриптом и записывает логи вместе с рабочими файлами в BUILD.
6. Создает папку DIST в папке со скриптом, если она еще не существует.
7. Записывает все необходимые файлы вместе со скриптом или в одну папку, или в один исполняемый файл.

Параметр --add-data позволяет добавить файлы с данными, которые нужно сохранить в одном бандле с исполняемым файлом. Этот параметр можно применить много раз.

Применение: __pyinstaller --add-data "Audio_player.py;." Unificator.py__

__Файл spec__ — это первый файл, который PyInstaller создает, чтобы закодировать содержимое скрипта Python вместе с параметрами, переданными при запуске.

PyInstaller считывает содержимое файла для создания исполняемого файла, определяя все, что может понадобиться для него.

Файл с расширением .spec сохраняется по умолчанию в текущей директории.

Если у вас есть какое-либо из нижеперечисленных требований, то вы можете изменить файл спецификации:

1. Собрать в один бандл с исполняемым файлы данных.
2. Включить другие исполняемые файлы: .dll или .so.
3. С помощью библиотек собрать в один бандл несколько программы.

__Дополнительные импорты с помощью Hidden Imports__

Исполняемому файлу требуются все импорты, которые нужны Python-скрипту. Иногда PyInstaller может пропустить динамические импорты или импорты второго уровня, возвращая ошибку ImportError: No module named…

Для решения этой ошибки нужно передать название недостающей библиотеки в hidden-import.

Например, чтобы добавить библиотеку wave, нужно написать вот так:

pyinstaller --onefile --add-data "Audio_player.py;." — hidden-import "wave" Unificator.py

Для иллюстрации работы pyinstaller было написано 4 простеньких скрипта, что объединятся в меню выбора 5-го. Чтобы сгенерировать .exe файл необходимо применить следующую команду находясь в директории, что содержит целевой скрипт.

__pyinstaller --onefile --add-data "Audio_player.py;." --add-data "Data_vizualizer.py;." --add-data "Image_filter.py;." --add-data "Website_scrapper.py;." Unificator.py__

В результате ее выполнения образуется файл расширения .spec и две папки __build__ и __dist__. В папке __dist__ и находится наше приложение. Впоследствии папку __build__ можно спокойно удалить, она не влияет на работоспособность приложения.

Следующим шагом закидываем _42.jpg_, _1000 Sales Records.csv_ и _Terentij.wav_ в папку __dist__ и запускаем полученный __Unificator.exe__. Антивирус может недолго ругаться, но не должен помешать повторно запустить .exe и посмотреть варианты в меню.
