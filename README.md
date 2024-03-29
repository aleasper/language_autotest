# language_autotest
## Autotest for multilingual online store with Pytest+Selenium
Testing for site: http://selenium1py.pythonanywhere.com/ru/  
This is the solution of the [problem](https://stepik.org/lesson/237240/step/9?unit=209628) on [Stepik course](https://stepik.org/course/575/)  
Original problem:  
>Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.  
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.  
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.  
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.   Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.  
Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.  

Strat test: pytest --browser_name=browser --language=language test_items.py  
Example: pytest --browser_name=firefox --language=ru test_items.py
