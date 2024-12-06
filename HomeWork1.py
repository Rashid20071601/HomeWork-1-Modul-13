# Импорт библиотек
import asyncio

# Асинхронная функция для соревнований силача
async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):  # Цикл на 5 подходов
        await asyncio.sleep(8 - power)  # Задержка между подходами
        print(f"Силач {name} поднял {i}")  # Отчет о подходе
    print(f"Силач {name} закончил соревнования.")

# Асинхронная функция для проведения турнира
async def start_tournament():
    # Создание задач для каждого силача
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Ожидание завершения задачи каждого силача
    await task1
    await task2
    await task3

# Запуск асинхронного турнира
asyncio.run(start_tournament())
