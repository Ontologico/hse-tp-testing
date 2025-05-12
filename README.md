Примеры того, как использовать pytest и Github Actions

## Запуск

Для использования рекомендуется сначала создать и активировать виртуальное окружение:

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

Linux/Mac:
```bash
# Для Ubuntu нужно установить дополнительный пакет
sudo apt update
sudo apt install python3-venv

python3 -m venv .venv
.venv/bin/activate
```

Далее нужно установить необходимые библиотеки:
```bash
pip install -r requirements.txt
```
