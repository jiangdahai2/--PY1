from random import randint

def get_unique_list_numbers() -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    unique_list = {randint(-10,10) for _ in range(16)}
    return list(unique_list)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
