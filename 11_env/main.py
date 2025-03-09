# 11.1. Wstęp do Zmiennych Środowiskowych
# Zmienne środowiskowe to dynamiczne wartości, które mogą wpływać na zachowanie procesów w systemie operacyjnym.
# Są przechowywane poza kodem programu i mogą być używane do konfiguracji aplikacji.

# 13.2 Czym są pliki .env
# Plik .env to prosty plik tekstowy, który przechowuje pary klucz-wartość,
# reprezentujące zmienne środowiskowe.  Jest to popularny sposób na zarządzanie
# konfiguracją aplikacji, szczególnie w projektach webowych.
# Zamiast przechowywania wrażliwych danych (jak hasła, klucze API) bezpośrednio
# w kodzie, umieszczamy je w pliku .env, a następnie odczytujemy w Pythonie.

# 11.3. Dlaczego Używamy Zmiennych Środowiskowych?

# - Bezpieczeństwo:  Wrażliwe dane (hasła, klucze API) nie są przechowywane w kodzie źródłowym.
# - Konfiguracja:  Możemy łatwo zmieniać konfigurację aplikacji (np. adres bazy danych) bez modyfikacji kodu.
# - Przenośność:  Aplikacja może działać w różnych środowiskach (lokalne, testowe, produkcyjne)
#                  z różnymi konfiguracjami, bez zmiany kodu.  Każde środowisko ma swój plik .env.
# - Współpraca:  Ułatwiają współpracę w zespole, ponieważ każdy programista
#                  może mieć własny plik .env z lokalnymi ustawieniami.

# 11.4. Odczytywanie Zmiennych Środowiskowych w Pythonie (bez .env)
# Do odczytywania zmiennych środowiskowych *ustawionych w systemie operacyjnym*
# używamy modułu `os`.

import os

# Odczyt zmiennej środowiskowej (np. PATH, USERNAME, itp. - zależą od systemu)
print(os.environ.get("PATH"))  # Wypisze ścieżkę PATH
print(os.environ.get("USERNAME"))  # Wypisze nazwę użytkownika (Windows)
print(os.environ.get("USER"))      # Wypisze nazwę użytkownika (Linux/macOS)

# Jeśli zmienna nie istnieje, get() zwraca None (domyślnie).
print(os.environ.get("NIEISTNIEJACA_ZMIENNA"))  # None

# Możemy podać wartość domyślną:
print(os.environ.get("NIEISTNIEJACA_ZMIENNA", "Wartość domyślna"))

# Możemy też użyć os.environ['ZMIENNA'], ale to spowoduje błąd KeyError,
# jeśli zmienna nie istnieje.  Dlatego *lepiej* używać get().
# print(os.environ["NIEISTNIEJACA_ZMIENNA"])  # To spowoduje błąd!


# 11.5. Instalacja i Użycie `python-dotenv`
# Do łatwego zarządzania zmiennymi środowiskowymi z pliku .env używamy
# biblioteki `python-dotenv`.

# 1. Instalacja:  `pip install python-dotenv`
# 2. Utwórz plik .env w głównym katalogu projektu (obok pliku .py).
#    Przykładowa zawartość pliku .env:
#    ```
#    BAZA_DANYCH_URL=postgres://uzytkownik:haslo@localhost:5432/nazwa_bazy
#    KLUCZ_API=tajnykluczapi123
#    DEBUG=True
#    ```

# 3. Załaduj zmienne z .env do os.environ:

from dotenv import load_dotenv

load_dotenv()  # To ładuje zmienne z .env *do* os.environ

# Teraz możemy używać zmiennych z .env tak, jakby były ustawione w systemie:
baza_danych_url = os.environ.get("BAZA_DANYCH_URL")
klucz_api = os.environ.get("KLUCZ_API")
debug_mode = os.environ.get("DEBUG")

print(f"BAZA_DANYCH_URL: {baza_danych_url}")
print(f"KLUCZ_API: {klucz_api}")
print(f"DEBUG: {debug_mode}")


# 11.6.  `load_dotenv()` - Szczegóły

# - `load_dotenv()` domyślnie szuka pliku `.env` w bieżącym katalogu.
# - Możemy podać ścieżkę do innego pliku `.env`:  `load_dotenv("/sciezka/do/mojego/pliku.env")`
# - `load_dotenv()` *nie* nadpisuje istniejących zmiennych środowiskowych.
#    Jeśli zmienna o tej samej nazwie już istnieje w `os.environ`,
#    wartość z `.env` zostanie *zignorowana*.
# - Istnieje funkcja `dotenv_values()`, która zwraca słownik
#    z wartościami z `.env`, *bez* modyfikowania `os.environ`.

from dotenv import dotenv_values

env_values = dotenv_values(".env")  # Zwraca słownik
print(env_values)
# {'BAZA_DANYCH_URL': 'postgres://uzytkownik:haslo@localhost:5432/nazwa_bazy', 'KLUCZ_API': 'tajnykluczapi123', 'DEBUG': 'True'}

# 11.7.  Przykłady Użycia

# - Konfiguracja połączenia z bazą danych:

# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# db_user = os.environ.get("DB_USER")
# db_password = os.environ.get("DB_PASSWORD")
# db_host = os.environ.get("DB_HOST")
# db_name = os.environ.get("DB_NAME")
#
# # Użyj tych zmiennych do połączenia z bazą danych (np. z biblioteką psycopg2):
# # conn = psycopg2.connect(user=db_user, password=db_password, host=db_host, database=db_name)


# - Ustawienia API:

# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# api_key = os.environ.get("API_KEY")
# api_secret = os.environ.get("API_SECRET")
#
# # Użyj tych zmiennych do autoryzacji w API:
# # client = ApiClient(api_key, api_secret)



# - Tryb debugowania:

# import os
# from dotenv import load_dotenv
# load_dotenv()

# if os.environ.get("DEBUG") == "True":
#     print("Aplikacja działa w trybie debugowania.")
    # Włącz dodatkowe logowanie, raportowanie błędów, itp.
# else:
#     print("Aplikacja działa w trybie produkcyjnym.")

# 11.8.  .env a Bezpieczeństwo

# - **Nigdy** nie umieszczaj pliku `.env` w repozytorium kodu (np. na GitHubie)!
# - Dodaj `.env` do pliku `.gitignore`, aby przypadkowo go nie wysłać.
# - W środowisku produkcyjnym, zamiast `.env`, możesz ustawić zmienne
#   środowiskowe bezpośrednio w systemie (np. przez panel administracyjny).
# - Rozważ użycie narzędzi do zarządzania sekretami (np. HashiCorp Vault, AWS Secrets Manager),
#    szczególnie w środowiskach produkcyjnych.

# 11.9  Najczęstsze błędy

# - Zapominanie o `load_dotenv()`:  Jeśli nie załadujesz `.env`, zmienne nie będą dostępne.
# - Literówki w nazwach zmiennych:  Upewnij się, że nazwy zmiennych w kodzie
#    zgadzają się z nazwami w pliku `.env`.
# - Używanie `os.environ[]` zamiast `os.environ.get()`:  To może prowadzić do błędów `KeyError`.
# - Przechowywanie `.env` w repozytorium:  To poważny problem bezpieczeństwa!
# - Nadpisywanie istniejących zmiennych : Uważaj, aby nie nadpisać zmiennych systemowych przez przypadek
# - Brak pliku .env: Upewnij się że plik .env istnieje

# 11.10  Alternatywy dla `python-dotenv`

# - `decouple`:  Podobna biblioteka, ale oferuje dodatkowe funkcje,
#   takie jak automatyczne rzutowanie typów (np. `config("DEBUG", cast=bool)`).
# - `environs`:  Bardziej zaawansowana biblioteka, która obsługuje
#   różne formaty (nie tylko `.env`), walidację i hierarchiczne konfiguracje.
# - Bezpośrednie ustawianie zmiennych w systemie:  W środowiskach produkcyjnych
#   często ustawia się zmienne bezpośrednio w systemie (np. w konfiguracji serwera).
#   To jest *bezpieczniejsze* niż używanie `.env`.

# 11.11 Podsumowanie
# Zmienne środowiskowe i pliki `.env` to standardowy sposób
# na zarządzanie konfiguracją aplikacji Python.  Zapewniają bezpieczeństwo,
# elastyczność i przenośność.  Biblioteka `python-dotenv` ułatwia
# korzystanie z plików `.env` w lokalnym środowisku developerskim.

print("Rozdział o zmiennych środowiskowych zakończony!")