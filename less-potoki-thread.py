# result = (2+3)*(5+6)



# pip install threading                                  # поток
#
from threading import Thread
from time import sleep, monotonic

#
# def func1():
#     for i in range(5):
#         tmp = 1
#         sleep(tmp)
#         print('\tthread No.1 (', tmp, ') :', i+1, '->', (i+1)*tmp, 'sec')
#     print('< the thread No.1 (', tmp, ') ----- FINISH ----- >')
#
#
# def func2():
#     for i in range(5):
#         tmp = 1.7
#         sleep(tmp)
#         print('\t\tthread No.2 (', tmp, ') :', i+1, '->', (i+1)*tmp, 'sec')
#     print('< the thread No.2 (', tmp, ') ----- FINISH ----- >')
#
#
# start_pr = monotonic()
#
#
# # func1()
# # func2()
#
# th1 = Thread(target=func1)
# th2 = Thread(target=func2)
# # th2 = Thread(target=func2, daemon=True) # Прервати при закінченні програми
# # th1 = Thread(target=func1, daemon=True) # Прервати при закінченні програми
# th1.start()
# # th1.join()   # Приєднання до пріоритетного процесу!
# # # #                 # Очікування поки не завершиться !
# th2.start()
# th1.join() # Приєднання до пріоритетного процесу!
# th2.join() # Приєднання до пріоритетного процесу!
# # # # # # print("-----------------> stop")
# print("< main thread STARTS >\n")
# for i in range(5):
#     tmp = 0.55
#     sleep(tmp)
#     print('main thread (', tmp, ') :', i+1, '->', (i+1)*tmp, 'sec')
#     print(f"thread 1 status: {th1.is_alive()}")
#     print(f"thread 2 status: {th2.is_alive()}")
#     print()
# print('< the main thread (', tmp, ') ----- FINISH ----- >')
# print('!!!!!!!! ALL Finish !!!!!!!!!!')
#
# print(monotonic() - start_pr)



##############################################################################
# ===================================================
#        Semaphore
# ===================================================
#
# from threading import Thread, BoundedSemaphore
# from time import sleep, time
#
#
# ticket_office = 3
# clients = 11
#
#
# ticket = BoundedSemaphore(value=ticket_office)
#
#
# def client(number):
#     start = time()
#     with ticket:
#         # for i in range(10000):
#         #     a = i**2
#         sleep(1)
#         print(f"client {number}, service time: {time() - start}\n", end='')
#
#
# customer = [Thread(target=client, args=(i,)) for i in range(1, clients+1)]
# # print(customer)
# # breakpoint()
# for user in customer:
#     user.start()

# ==================================
#        Timer
# ==================================
# from threading import Timer
# from time import sleep, ctime
#
#
# def foo():
#     print('Я думаю! Не заважай!....')
#     print('Start функції', ctime()[10:19])
#     for i in range(9, 0, -1):
#         sleep(1)
#         print('Реклама завершиться через', i, 'секунд...')
#     print("Придумав! Зараз у нас на годиннику", ctime()[10:19])
#
#
# # timer = Timer(interval=5.5, function=lambda: print("Message from Timer! >>>", ctime()[10:19]))
# timer = Timer(interval=3.5, function=foo)
# print('Start', ctime()[10:19])
# # # print('Start', ctime())
# timer.start()
# print('Finish', ctime()[10:19])


# ======================================================
#      Barrier
# ======================================================
# from threading import Barrier, Thread
# from time import sleep, time
#
#
# start_time = time()
# br = Barrier(3)  # кількість потоків (головний + f1() + f2())
# result = []
#
#
# def f1(x):
#     res = 3 * x ** 2  #  3*x**2+2*x=  sum[f1, f2]
#     sleep(2)
#     result.append(res)
#     print('Calc part1 3 *', x, '^ 2 =', res)
#     br.wait()  # При застосуванні br.wait()
#
#
# def f2(x):
#     res = 2 * x
#     sleep(1)
#     print('Calc part2   2 *', x, ' =', res)
#     result.append(res)
#     br.wait()  # При застосуванні br.wait()
#
#
# x = 3
# # f1(x)  # Звичайна послідовність (синхронний режим)
# # f2(x)  # Звичайна послідовність (синхронний режим)
#
# Thread(target=f1, args=(x,)).start()
# Thread(target=f2, args=(x,)).start()
# br.wait()  # Очікує на сигнали з обоїх потоків від їх br.wait()
#
# print(result)
# print("=====   Result:  3 * ", x, '^2 + 2 * ', x, ' = ', sum(result), '    ======', sep='')
# print(time() - start_time)
# # print(*dir(br), sep='\n')