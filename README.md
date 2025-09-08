# Эмулятор для языка оболочки ОС в форме консольного интерфейса (CLI)
Функции
---
- `cd <directory>` - сменить директорию на directory
- `ls` - показать содержимое текущей директории
- `echo <text>` - вывести в консоль text
- `$` - символ, с помощью которого реализован парсер (например $HOME)
- `exit` - выход из эмулятора
---
Запуск
---
```
python3 ./main.py ./vfs/test.csv ./vfs/.shitrc
```
- test.csv - файл с тестовой vfs;
- .shitrc - темплейт для запуска эмулятора
```
python3 ./scripts/default_script.py
```
- скрипт для быстрого запуска с использованием команд из .egrc
---
Пример использования
<img width="933" height="471" alt="image" src="https://github.com/user-attachments/assets/2fe49dcd-c608-414e-bcbf-63bee1de36d7" />
<img width="933" height="471" alt="image" src="https://github.com/user-attachments/assets/c0e58153-4245-49fc-b967-99f79caf2e15" />
