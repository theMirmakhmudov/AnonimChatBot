from aiogram import Dispatcher
from handlers import start, plans, random_func, encryption


def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(random_func.router)
    dp.include_router(encryption.router)
    dp.include_router(plans.router)
