# 1. Sklonowanie repozytorium z GitHub (lub innego systemu kontroli wersji)
git clone https://github.com/takzen/python-dla-inzynierow-AI.git

# 2. Przejście do sklonowanego katalogu
cd python-dla-inzynierow-AI

# 3. Utworzenie środowiska wirtualnego (venv) w katalogu projektu dla Python 3.13.2
python -m venv venv

# 4. Aktywowanie środowiska wirtualnego:
# Na systemie Windows (PowerShell)
venv\Scripts\Activate

# Na systemie Windows (cmd)
venv\Scripts\activate.bat

# Na systemie Linux/macOS
source venv/bin/activate

# 6. Update pip 
python.exe -m pip install --upgrade pip

# 7. Instalacja zależności z pliku requirements.txt (jeśli istnieje)
pip install -r requirements.txt

# 8. Sprawdzenie zainstalowanych pakietów w środowisku wirtualnym
pip list

# 9. Uruchomienie aplikacji Python (przykładowo, jeśli projekt zawiera plik main.py)
python main.py

# 10. Dezaktywowanie środowiska wirtualnego po zakończeniu pracy
deactivate
