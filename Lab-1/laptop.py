import csv
import datetime
import time


class Laptop:
    comparison_operations_amount_for_inserstion_sort = 0
    exchange_operations_amount_for_inserstion_sort = 0
    comparison_operations_amount_for_heapsort = 0
    exchange_operations_amount_for_heapsort = 0

    def __init__(self, cpu_speed: float, ram_amount: int, laptop_name: str):
        self.cpu_speed = cpu_speed
        self.ram_amount = ram_amount
        self.laptop_name = laptop_name

    def __str__(self):
        return f"CPU of speed: {self.cpu_speed} Amount of RAM: {self.ram_amount} Name of laptop: {self.laptop_name}"


def entry_data_from_csv(file_name):
    instances_of_laptops = []
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for line in reader:
            instances_of_laptops.append(
                Laptop(cpu_speed=float(line[0]), ram_amount=int(line[1]), laptop_name=str(line[2])))

    return instances_of_laptops


def algo_information_print(algoritm_name, work_time,
                           comparison_operations_amount, exchange_operations_amount):
    print()
    print(f"Algortim name: {algoritm_name}")
    print(f"Work time: {work_time}")
    print(f"Comparison operations: {comparison_operations_amount}")
    print(f"Exchange operations: {exchange_operations_amount}")
    print()


def insertion_sort(laptops_for_insertion_sort):
    start_time = datetime.datetime.now()
    for laptop_index in range(len(laptops_for_insertion_sort)):
        Laptop.comparison_operations_amount_for_inserstion_sort += 1
        ram_amount_item = laptops_for_insertion_sort[laptop_index].ram_amount
        laptop_to_sort = laptop_index - 1
        while laptop_to_sort >= 0 and laptops_for_insertion_sort[laptop_to_sort].ram_amount < ram_amount_item:
            Laptop.comparison_operations_amount_for_inserstion_sort += 1
            Laptop.exchange_operations_amount_for_inserstion_sort += 1
            laptops_for_insertion_sort[laptop_to_sort + 1].ram_amount = laptops_for_insertion_sort[
                laptop_to_sort].ram_amount
            laptop_to_sort -= 1
        laptops_for_insertion_sort[laptop_to_sort + 1].ram_amount = ram_amount_item

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    algo_information_print("Insertion sort", time_diff, Laptop.comparison_operations_amount_for_inserstion_sort,
                           Laptop.exchange_operations_amount_for_inserstion_sort)

    return laptops_for_insertion_sort


def heap_sort(laptop_objects):
    def binary_tree(laptops_for_sort, max, index):
        big_index = index
        child_l = 2 * index + 1
        child_r = child_l + 1

        Laptop.comparison_operations_amount_for_heapsort += 1
        if child_l < max and laptops_for_sort[child_l].cpu_speed > laptops_for_sort[index].cpu_speed:
            big_index = child_l

        Laptop.comparison_operations_amount_for_heapsort += 1
        if child_r < max and laptops_for_sort[child_r].cpu_speed > laptops_for_sort[big_index].cpu_speed:
            big_index = child_r

        Laptop.comparison_operations_amount_for_heapsort += 1
        if big_index != index:
            Laptop.exchange_operations_amount_for_heapsort += 1
            laptops_for_sort[index], laptops_for_sort[big_index] = laptops_for_sort[big_index], laptops_for_sort[index]

            binary_tree(laptops_for_sort, max, big_index)

    start_time = datetime.datetime.now()
    list_length = len(laptop_objects)

    for j in range(list_length // 2 - 1, -1, -1):
        Laptop.comparison_operations_amount_for_heapsort += 1

        binary_tree(laptop_objects, list_length, j)

    for k in range(list_length - 1, 0, -1):
        Laptop.exchange_operations_amount_for_heapsort += 1
        laptop_objects[k].cpu_speed, laptop_objects[0].cpu_speed = laptop_objects[0].cpu_speed, laptop_objects[
            k].cpu_speed

        binary_tree(laptop_objects, k, 0)

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time

    algo_information_print("Heapsort", time_diff, Laptop.comparison_operations_amount_for_heapsort,
                           Laptop.exchange_operations_amount_for_heapsort)

    return laptop_objects


input_data = entry_data_from_csv("laptops.csv")
print()
print("Input data")
for item in input_data:
    print(item.__str__())

insertion_result = insertion_sort(input_data)
for notebook_pc in insertion_result:
    print(notebook_pc.__str__())

heapsort_result = heap_sort(input_data)
for notebook_pc in heapsort_result:
    print(notebook_pc.__str__())
