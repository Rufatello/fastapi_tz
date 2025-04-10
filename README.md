Запустите приложение:
docker-compose up --build

Применить все миграции**:
docker-compose exec app alembic upgrade head

После запуска приложение будет доступно:
API: http://localhost:8000
Документация Swagger: http://localhost:8000/docs
