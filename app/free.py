from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

router_p = APIRouter(tags=['Free'])

@router_p.get("/health")
async def health_check():
    return{
        'Detail': 'Service is running'
    }

@asynccontextmanager
async def lifespan(app):
    print('Appllication started')

    app.state.service_name = 'Analizator Documentov'
    app.state.version = '1.0.0'

    yield

    print('Application closed')

def create_app() -> FastAPI:
    xxx = FastAPI(
        title='Analizator Documentov',
        version='1.0.0',
        lifespan=lifespan
    )

    xxx.include_router(router_p)

    return xxx

yyy = create_app()


# 1. Импорт модулей
# from fastapi import FastAPI, APIRouter
# from contextlib import asynccontextmanager

# FastAPI — основной класс для создания веб-приложения.APIRouter —
# инструмент для группировки маршрутов (эндпоинтов), который позволяет разделять логику по разным
# файлам и модулям.asynccontextmanager — декоратор из стандартной библиотеки Python для создания
# асинхронных контекстных менеджеров. Здесь он нужен для управления запуском и остановкой приложения.
# 2. Создание роутера и эндпоинтаpythonrouter_p = APIRouter(tags=['Free'])
#
# @router_p.get("/health")
# async def health_check():
#     return {
#         'Detail': 'Service is running'
#     }
# router_p — экземпляр роутера. Параметр tags=['Free'] группирует
# этот и сопутствующие маршруты в автоматической документации Swagger UI под тегом "Free".@router_p.get("/health") —
# декоратор, который регистрирует GET-запрос по адресу /health.health_check() — асинхронная функция (хендлер). Она
# возвращает JSON-ответ, подтверждающий, что сервис работает. Это стандартный эндпоинт для мониторинга (Health Check).
# 3. Управление жизненным циклом (Lifespan)python@asynccontextmanager
# async def lifespan(app):
#     print('Appllication started')
#
#     app.state.service_name = 'Analizator Documentov'
#     app.state.version = '1.0.0'
#
#     yield
#
#     print('Application closed')
# Функция lifespan управляет процессами, которые должны происходить при старте и
# завершении работы сервера.Код до yield выполняется при запуске приложения. В консоль выводится строка
# 'Appllication started' (в слове допущена опечатка, но на работу это не влияет).app.state — это глобальное хранилище
# состояний FastAPI. В него записываются метаданные сервиса (service_name и version), к которым потом можно будет
# обратиться из любого хендлера запросов.yield — разделяет логику старта и остановки. В этот момент приложение
# запускается и начинает принимать запросы.Код после yield выполняется при выключении сервера. В консоль выводится
# 'Application closed'. Здесь обычно закрывают соединения с базами данных или очищают кэш.
# 4. Фабрика приложения (Application Factory)
# create_app() -> FastAPI:
#     xxx = FastAPI(
#         title='Analizator Documentov',
#         version='1.0.0',
#         lifespan=lifespan
#     )
#
#     xxx.include_router(router_p)
#
#     return xxx
# Использование функции для создания объекта приложения (create_app) — это отличный паттерн проектирования.
# Он упрощает тестирование и масштабирование.xxx = FastAPI(...) — инициализация главного объекта приложения с
# указанием названия, версии и логики жизненного цикла (lifespan).xxx.include_router(router_p) — подключение ранее
# созданного роутера со всеми его эндпоинтами к главному приложению.Функция возвращает настроенный объект xxx.
# 5. Точка входа
#
# yyy = create_app()
