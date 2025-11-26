🏥 Medical Information System (МИС)

Простой веб-сервис, реализующий базовый функционал Медицинской Информационной Системы (МИС):

Авторизация по JWT

CRUD консультаций врача

Фильтрация, поиск, сортировка

Изменение статуса консультации

Разграничение прав доступа по ролям: admin / doctor / patient

Работа доктора в нескольких клиниках

Построено на Django + Django REST Framework

Поддержка PostgreSQL

Docker + docker-compose

Интеграционные тесты (pytest)

🚀 Технологический стек

Python 3.12

Django 5

Django REST Framework

SimpleJWT

PostgreSQL

pytest

Docker / docker-compose

📦 Установка и запуск проекта
1. Клонирование:
git clone https://github.com/<ВАШ_НИК>/mis-medical-system.git
cd mis-medical-system

🐳 Запуск проекта через Docker
docker-compose up --build


После запуска API будет доступно по адресу:

👉 http://127.0.0.1:8000/api/consultations/
🔐 JWT Авторизация

Получение токена:

POST /api/auth/token/
{
  "username": "admin",
  "password": "yourpassword"
}


Обновление:

POST /api/auth/token/refresh/


Использование токена:

Authorization: Bearer <access_token>

📌 API эндпоинты
Консультации врача
Метод	URL	Описание
GET	/api/consultations/	Список консультаций
POST	/api/consultations/	Создание консультации
GET	/api/consultations/<id>/	Получение консультации
PATCH / PUT	/api/consultations/<id>/	Обновление
DELETE	/api/consultations/<id>/	Удаление
POST	/api/consultations/<id>/change_status/	Смена статуса
🔍 Фильтрация / Поиск / Сортировка
Поиск по ФИО врача и пациента:
?search=Иванов

Фильтр по статусу:
?status=pending

Сортировка по дате создания:
?ordering=created_at
?ordering=-created_at

👤 Модель ролей
admin

полный доступ ко всему

doctor

доступ только к своим консультациям

patient

доступ только к своим консультациям

🧪 Тесты

Запуск:

pytest


Пример теста:

@pytest.mark.django_db
def test_consultation_list_requires_auth():
    client = APIClient()
    url = reverse("consultation-list")
    response = client.get(url)
    assert response.status_code == 401

📂 Структура проекта
MIS_project/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── tests/
│
├── mis/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── setup.cfg
└── README.md
