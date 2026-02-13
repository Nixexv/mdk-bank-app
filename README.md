# Bank App (Tkinter)

Макет банковского приложения на Tkinter окна на МДК.

## Требования

- Python 3.10+
- Tkinter (обычно идет вместе с Python)
- Pillow для отображения изображений

Установка Pillow:

```bash
pip install pillow
```

## Запуск

```bash
python main.py
```

## Структура

- `main.py` — точка входа.
- `ui/app.py` — главное окно приложения.
- `ui/layout.py` — отрисовка статичного макета.
- `ui/draw.py` — вспомогательные функции рисования.
- `ui/assets.py` — загрузка изображений.
- `asset/` — изображения интерфейса.
## Установка шрифтов
Windows (PowerShell, админ)

# Путь к папке со шрифтами
$src = "C:\path\to\fonts"

# Установить все ttf
```bash
Get-ChildItem $src -Filter *.ttf | ForEach-Object {
  $font = $_.FullName
  $dest = "$env:WINDIR\Fonts\$($_.Name)"
  Copy-Item $font $dest -Force
  New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" `
    -Name $_.Name -PropertyType String -Value $_.Name -Force | Out-Null
}
```
macOS (Terminal)
```bash
# Для всех пользователей (нужен sudo)
sudo mkdir -p /Library/Fonts/Poppins
sudo cp /path/to/fonts/*.ttf /Library/Fonts/Poppins/
```
Или только для текущего пользователя:
```bash
mkdir -p "$HOME/Library/Fonts"
cp /path/to/fonts/*.ttf "$HOME/Library/Fonts/"
```
Linux
Ubuntu/Debian:
```bash
mkdir -p ~/.local/share/fonts
cp /path/to/fonts/*.ttf ~/.local/share/fonts/
fc-cache -f -v
```
Системно (нужен sudo):
```bash
sudo mkdir -p /usr/local/share/fonts
sudo cp /path/to/fonts/*.ttf /usr/local/share/fonts/
sudo fc-cache -f -v
```
