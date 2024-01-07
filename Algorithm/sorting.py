########################################################################
#################### 1. Bubble Sort (сортування бульбашкою) ###############

"""
Сортування "Bubble Sort" - це один з простих алгоритмів сортування,
який порівнює сусідні елементи і обмінює їх,
якщо вони не відсортовані у правильному порядку.
Алгоритм продовжує такі порівняння та обміни до тих пір,
поки весь масив не буде відсортований.
Основна ідея полягає в тому,
щоб найбільший (або найменший) елемент "спливав"
на своє правильне місце після кожної ітерації.
"""

#
# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         # Внутрішня петля для порівняння та обміну елементів
#         for j in range(0, n - i - 1):
#             print(arr[j], '-------', arr[j+1])
#             if arr[j] > arr[j + 1]:
#                 # Обмін елементів, якщо вони не відсортовані
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 print('зміна ', arr[j], '<->', arr[j + 1])
#                 print(arr)
#             print('Новий цикл:')
#             print(arr)
#
#
# # Приклад використання:
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("НЕвідсортований масив:", arr)
# bubble_sort(arr)
# print("Відсортований масив:", arr)

"""
У цій програмі bubble_sort приймає масив arr, який потрібно відсортувати. 
Зовнішня петля for i визначає кількість ітерацій, 
де після кожної ітерації найбільший елемент "спливає" 
на правильне місце в кінці масиву. 
Внутрішня петля for j порівнює сусідні елементи та обмінює їх, 
якщо вони не відсортовані.

Цей алгоритм має часову складність O(n^2), 
що робить його неефективним для великих масивів, 
але він є простим і легко зрозумілим для освоєння основ сортування."""





################################################################################
################# 2. Selection Sort (сортування вибором) #######################

"""
Сортування Selection Sort - це простий алгоритм сортування, 
який вибирає мінімальний (або максимальний) елемент з масиву 
і переміщає його на початок (або кінець) впорядкованої частини масиву. 
Процес повторюється для всього масиву, поки весь масив не буде впорядкований.
"""


# def selection_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         min_idx = i  # Припускаємо, що поточний елемент - найменший
#         print(arr[min_idx])
#
#         # Знаходимо індекс мінімального елемента у підмасиві arr[i+1:n]
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#
#         # Міняємо місцями поточний елемент та мінімальний елемент
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         print(arr[i], '<->', arr[min_idx])
#         print(arr)
#
#
# # Приклад використання
# arr = [64, 25, 12, 22, 11]
# print("НЕвпорядкований масив:", arr)
# selection_sort(arr)
# print("Впорядкований масив:", arr)


"""
1 - Ми проходимо через всі елементи масиву arr.
2 - Для кожного елемента ми знаходимо індекс найменшого елемента у підмасиві arr[i+1:n].
3 - Ми міняємо місцями поточний елемент і мінімальний елемент.
4 - Повторюємо цей процес для всіх елементів масиву.

Після виконання програми, масив arr буде впорядкованим в порядку зростання. 
Selection Sort - це один із найпростіших алгоритмів сортування, 
але він не є найбільш ефективним для великих масивів через свою квадратичну складність.
"""


###########################################################################
##################### 3. Insertion Sort (сортування вставками) ############


"""
Insertion Sort - це простий алгоритм сортування, 
який сортує масив шляхом послідовного вибору елементів 
та їх вставки на відповідні позиції в відсортовану частину масиву. 
Основна ідея полягає в тому, щоб проходити через вхідний масив, 
додавати кожний елемент до відсортованої частини 
і розміщувати його на відповідному місці, зберігаючи відсортовану послідовність.
"""


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]  # Поточний елемент для порівняння та вставки
#         j = i - 1
#         print('Встановлюємо', key, '->', end='')
#
#         # Порівнюємо key з попередніми елементами та зсуваємо їх вправо, якщо вони більше за key
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key  # Вставляємо key на відповідне місце
#         print(arr)
#
# # Приклад використання
# my_list = [12, 11, 13, 5, 6]
# print("HEвідсортований масив:", my_list)
# insertion_sort(my_list)
# print("Відсортований масив:", my_list)


"""
Ця програма реалізує алгоритм сортування Insertion Sort для списку my_list. 
Вона проходить через всі елементи масиву, 
порівнює їх та вставляє їх на відповідні позиції, 
утворюючи відсортовану послідовність.
"""



########################################################################
################# 4. Merge Sort (сортування злиттям) ###################

"""
Сортування Merge Sort - це алгоритм сортування, 
який використовує метод розбиття і об'єднання для впорядкування масиву даних. 
Він рекурсивно розбиває масив на менші підмасиви, сортує їх і об'єднує, 
створюючи відсортований масив. 
Основна ідея полягає в тому, щоб розбити масив на половини, 
відсортувати кожну половину окремо і потім об'єднати їх.
"""


# def merge_sort(arr):
#     if len(arr) > 1:
#         # Розділити масив навпіл
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#         print('Розділені масиви', left_half, right_half)
#
#         # Рекурсивно сортувати кожну половину
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         i = j = k = 0
#
#         print('Відсортовані масиви', left_half, right_half)
#         print()
#
#         # Злити дві відсортовані половини
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#
#
# # Приклад використання
# arr = [12, 11, 13, 5, 6, 7]
# print("Початковий масив:", arr)
# print('.' * 80)
# merge_sort(arr)
# print('.' * 80)
# print("Відсортований масив:", arr)


"""
Програма розбиває вхідний масив на половини, 
рекурсивно сортує кожну половину і потім об'єднує їх в один відсортований масив. 
Merge Sort є дієвим алгоритмом сортування, 
який має часову складність O(n log n), де n - кількість елементів у масиві.
"""


#######################################################################
################# 5. Quick Sort (швидке сортування) ###################


"""
Quick Sort - це швидкий та ефективний алгоритм сортування, 
який використовує стратегію "розділ і підкори, а потім об'єднай". 
Він базується на принципі розділення масиву на менші підмасиви, 
сортування цих підмасивів і їх об'єднання для отримання відсортованого масиву. 
Основна ідея полягає в виборі опорного елементу 
і розподілі елементів навколо нього так, 
щоб менші елементи були ліворуч від опорного, а більші - праворуч.

Алгоритм трохи складніший, але в стандартних реалізаціях він працює швидше, 
ніж сортування злиттям, а його складність в гіршому випадку рідко досягає O (n ^ 2). 

Це сортування складається з трьох етапів:
1. Вибирається один опорний елемент.
2. Всі елементи, які менші за опорний, переміщаються зліва від нього, інші — направо.
   Це називається операцією розбиття.
3. Рекурсивно 2 попередні кроки повторюються в кожному новому списку, 
   де нові опорні елементи будуть менші та більші за опорний елемент.
"""


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     print(left, middle, right)
#
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# # Приклад використання
# my_list = [3, 6, 8, 10, 1, 2, 1]
# print("НЕвідсортований масив:", my_list)
# sorted_list = quick_sort(my_list)
# print("Відсортований масив:", sorted_list)

"""
У цій програмі ми визначаємо функцію quick_sort, яка сортує масив arr. 
Програма рекурсивно ділить масив на менші та більші підмасиви 
навколо опорного елементу (в цьому прикладі, середнього елемента) 
і об'єднує їх після сортування.
"""
