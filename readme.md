## Терентьев Алексей Ильич ИКБО-20-24
### Вариант 28
#### Этап 1
Создан конфигурационный файл формата yaml с заданными параметрами:
### ![alt text](assets/1/image.png)
Написана программа на python, которая считывает файл config.yaml и выводит его параметры:
### ![alt text](assets/1/image-1.png)
Результат работы программы:
### ![alt text](assets/1/image-2.png)
Реализована обработка ошибок для параметров: ошибка пустого значения в параметре и неправильный тип параметра maxDepth
### ![alt text](assets/1/image-3.png)
### ![alt text](assets/1/image-4.png)

#### Этап 2
Написана функция получения зависимостей для реальных пакетов:
### ![alt text](assets/2/image.png)
Вывод при вызове функции с параметрами из конфигурационного файла:

Конфигурационный файл:
### ![alt text](assets/2/image-1.png)
Вывод программы:
### ![alt text](assets/2/image-2.png)
Пример ошибки при поиске зависимостей (взят прошлый пример с измененным именем пакета - yo):
### ![alt text](assets/2/image-3.png)

#### Этап 3
Добавлена функция получения графа зависимостей через алгоритм bfs:
#### ![alt text](assets/3/image.png)
Изменена функция get_dependencies, которая теперь может работать в тестовом режиме:
#### ![alt text](assets/3/image-1.png)
Реализация функции в тестовом режиме:
#### ![alt text](assets/3/image-2.png)
Примеры работы функции dependency_graph:

1:
#### ![alt text](assets/3/image-3.png)
#### ![alt text](assets/3/image-9.png)
2:
#### ![alt text](assets/3/image-5.png)
#### ![alt text](assets/3/image-6.png)
3:
#### ![alt text](assets/3/image-7.png)
#### ![alt text](assets/3/image-8.png)