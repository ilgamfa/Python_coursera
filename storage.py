import argparse
import json
import os
import tempfile
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser("It is our storage!")
 
    parser.add_argument("--key", type=str, help="what is your key?")
 
    parser.add_argument(
        "--val", type=str, default=None, help="what is your value?")
 
    args = parser.parse_args()
    our_key = args.key
    our_value = args.val
   
    storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
 
    # В любом случае потребуется файл как для чтения так и для записи, поэтому
    # если файла не существует, то мы просто создаем открывая для записи.
    # Если файл существует, то берем из него данные в словарь, если не
    # существует или он пустой, то создаем пустой словарь
    if os.path.exists(storage_path):
        with open(storage_path) as f:
            # Обработка на случай если файл пустой
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = {}
    else:
        with open(storage_path, 'w') as f:
            data = {}
   
    if our_value:
        # Довольно удобный метод словаря, если ключа нет, то создается
        # ключ с пустым списком к которому добавляем значения
        data.setdefault(our_key, []).append(our_value)
        with open(storage_path, 'w') as f:
            json.dump(data, f)
    else:
        # Получаем список из словаря или пустую строку, если ключа нет,
        # это чтобы проще было работать с join
        result = ', '.join(data.get(our_key, ''))
        # Если result пустая строка, то выводим None
        print(result or None)