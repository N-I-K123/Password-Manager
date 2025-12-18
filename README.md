# Password Manager Web API

Aplikacja webowa do zarządzania hasłami zbudowana w FastAPI. Bezpieczne przechowywanie haseł z szyfrowaniem, autentykacją użytkowników i generatorem silnych haseł.

## 🚀 Funkcjonalności

- **Rejestracja i logowanie użytkowników** - Bezpieczna autentykacja z JWT tokenami
- **Zarządzanie hasłami** - Tworzenie, odczyt, aktualizacja i usuwanie haseł
- **Szyfrowanie haseł** - Hasła są szyfrowane przed zapisaniem w bazie danych
- **Generator haseł** - Generowanie silnych, losowych haseł
- **Autoryzacja** - Każdy użytkownik ma dostęp tylko do swoich haseł
- **RESTful API** - Czytelne i łatwe w użyciu endpointy

## 🛠️ Technologie

- **FastAPI** - Nowoczesny framework webowy dla Pythona
- **SQLAlchemy** - ORM do zarządzania bazą danych
- **SQLite** - Baza danych
- **JWT** - Autentykacja oparta na tokenach
- **bcrypt** - Hashowanie haseł użytkowników
- **Pydantic** - Walidacja danych

## 📋 Wymagania

- Python 3.8+
- pip

Aplikacja będzie dostępna pod adresem: `http://localhost:8000`

## 🔐 Endpointy API

### Użytkownicy

#### Rejestracja
```
POST /users/register
Body:
{
  "username": "string",
  "password": "string"
}
```

#### Logowanie
```
POST /users/token
Body:
{
  "username": "string",
  "password": "string"
}
Response:
{
  "access_token": "string",
  "token_type": "bearer"
}
```

#### Informacje o zalogowanym użytkowniku
```
GET /users/me
Headers:
  Authorization: Bearer {token}
```

### Hasła

Wszystkie endpointy haseł wymagają autoryzacji (Bearer token).

#### Utworzenie hasła
```
POST /passwords/
Headers:
  Authorization: Bearer {token}
Body:
{
  "site": "string",
  "password": "string"
}
```

#### Pobranie hasła
```
GET /passwords/{site}
Headers:
  Authorization: Bearer {token}
```

#### Aktualizacja hasła
```
PUT /passwords/{site}
Headers:
  Authorization: Bearer {token}
Body:
{
  "password": "string"
}
```

#### Usunięcie hasła
```
DELETE /passwords/delete/{site}
Headers:
  Authorization: Bearer {token}
```

## 📁 Struktura projektu

```
passwdManagerWeb/
├── main.py                 # Główny plik aplikacji FastAPI
├── models.py               # Modele SQLAlchemy (User, Password)
├── database.py             # Konfiguracja bazy danych
├── auth.py                 # Logika autentykacji i JWT
├── crypto.py               # Funkcje szyfrowania/deszyfrowania
├── Generator.py            # Generator silnych haseł
├── controller/
│   ├── passwords.py        # Endpointy dla haseł
│   └── users.py            # Endpointy dla użytkowników
├── service/
│   ├── crudPassword.py     # Operacje CRUD na hasłach
│   └── crudUser.py         # Operacje CRUD na użytkownikach
└── schema/
    ├── PasswordsSchema.py  # Schematy Pydantic dla haseł
    └── UserSchema.py       # Schematy Pydantic dla użytkowników
```

## 🔒 Bezpieczeństwo

- Hasła użytkowników są hashowane przy użyciu bcrypt
- Hasła do stron są szyfrowane przed zapisaniem w bazie
- Autoryzacja oparta na JWT tokenach
- Każdy użytkownik ma dostęp tylko do swoich haseł
- Unikalne ograniczenie na parę (user_id, site)

## ⚠️ Uwagi

- **SECRET_KEY** w pliku `auth.py` powinien być zmieniony na bezpieczny klucz w środowisku produkcyjnym
- Baza danych SQLite jest tworzona automatycznie przy pierwszym uruchomieniu
- Tokeny JWT wygasają po 30 minutach

## 📝 Przykład użycia

1. Zarejestruj nowego użytkownika:
```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

2. Zaloguj się i otrzymaj token:
```bash
curl -X POST "http://localhost:8000/users/token" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

3. Utwórz hasło (użyj tokenu z poprzedniego kroku):
```bash
curl -X POST "http://localhost:8000/passwords/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"site": "example.com", "password": "mySecurePassword123"}'
```

## 👤 Autor

[N-I-K123]

---

**Uwaga**: To jest projekt edukacyjny. W środowisku produkcyjnym należy zastosować dodatkowe środki bezpieczeństwa.

