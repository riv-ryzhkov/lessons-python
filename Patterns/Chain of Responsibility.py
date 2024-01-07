# Базовий клас для обробників
# class Handler:
#     def __init__(self, successor=None):
#         self._successor = successor
#
#     def handle_request(self, request):
#         if self._successor is not None:
#             return self._successor.handle_request(request)
#         return None
#
#
# # Конкретні обробники
# class ConcreteHandlerA(Handler):
#     def handle_request(self, request):
#         if request == "A":
#             return f"ConcreteHandlerA handled the request: {request}"
#         else:
#             return super().handle_request(request)
#
#
# class ConcreteHandlerB(Handler):
#     def handle_request(self, request):
#         if request == "B":
#             return f"ConcreteHandlerB handled the request: {request}"
#         else:
#             return super().handle_request(request)
#
# class ConcreteHandlerC(Handler):
#     def handle_request(self, request):
#         if request == "C":
#             return f"ConcreteHandlerC handled the request: {request}"
#         else:
#             return super().handle_request(request)
#
#
# class ConcreteHandlerD(Handler):
#     def handle_request(self, request):
#         if request == "D":
#             return f"ConcreteHandlerD handled the request: {request}"
#         else:
#             return super().handle_request(request)
#
#
# # Приклад використання
# if __name__ == "__main__":
#     handler_d = ConcreteHandlerD()
#     handler_c = ConcreteHandlerC(successor=handler_d)
#     handler_b = ConcreteHandlerB(successor=handler_c)
#     handler_a = ConcreteHandlerA(successor=handler_b)
#
#     requests = ["A", "D", "B", "G", "C", "D", "F"]
#
#     for request in requests:
#         result = handler_a.handle_request(request)
#         if result is not None:
#             print(result)
#         else:
#             print(f"No handler could process the request: {request}")


"""
Патерн "Ланцюжок відповідальності" дозволяє передавати запити 
по ланцюжку обробників, поки один з обробників не зможе обробити запит 
або поки ланцюжок не закінчиться.

У цьому прикладі є базовий клас Handler, 
який визначає основний інтерфейс для обробників 
та містить посилання на наступного обробника в ланцюжку.

ConcreteHandlerA, ConcreteHandlerB і ConcreteHandlerC - це конкретні обробники, 
які успадковуються від базового Handler. 
Кожен обробник може вирішувати, чи може він обробити запит, який отримав, 
і в разі неможливості передає запит наступному обробнику у ланцюжку.

У прикладі використання ми створюємо ланцюжок обробників, 
починаючи з ConcreteHandlerA, який має наступником ConcreteHandlerB, 
а той має наступником ConcreteHandlerC. 
Ми потім передаємо різні запити через цей ланцюжок. 
Якщо обробник може обробити запит, він це робить; 
в іншому випадку запит передається наступному обробнику у ланцюжку.

Цей приклад ілюструє використання патерну "Ланцюжок відповідальності" 
для створення ланцюжка обробників, які можуть обробляти запити послідовно, 
поки один з них не впорається з обробкою.
"""

# ==============================================
# Приклад обробки документів
# ==============================================


# Базовий клас обробника документа
# class DocumentHandler:
#     def __init__(self, name):
#         self.name = name
#         self.next_handler = None
#
#     def set_next_handler(self, next_handler):
#         self.next_handler = next_handler
#
#     def can_handle(self, document_type):
#         return False
#
#     def process_document(self, document_type):
#         pass
#
#     def handle_document(self, document_type):
#         if self.can_handle(document_type):
#             self.process_document(document_type)
#         elif self.next_handler:
#             self.next_handler.handle_document(document_type)
#         else:
#             print(f"No handler available for {document_type}")
#
#
# # Конкретні обробники документів
# class PDFHandler(DocumentHandler):
#     def can_handle(self, document_type):
#         return document_type == "PDF"
#
#     def process_document(self, document_type):
#         print(f"{self.name} handles {document_type} document")
#
#
# class WordHandler(DocumentHandler):
#     def can_handle(self, document_type):
#         return document_type == "Word"
#
#     def process_document(self, document_type):
#         print(f"{self.name} handles {document_type} document")
#
#
# class TextHandler(DocumentHandler):
#     def can_handle(self, document_type):
#         return document_type == "Text"
#
#     def process_document(self, document_type):
#         print(f"{self.name} handles {document_type} document")
#
#
# # Приклад використання
# if __name__ == "__main__":
#     pdf_handler = PDFHandler("PDF Handler")
#     word_handler = WordHandler("Word Handler")
#     text_handler = TextHandler("Text Handler")
#
#     pdf_handler.set_next_handler(word_handler)
#     word_handler.set_next_handler(text_handler)
#
#     # pdf_handler.handle_document("Word")   # Word Handler handles Word document
#     # pdf_handler.handle_document("PDF")    # PDF Handler handles PDF document
#     # pdf_handler.handle_document("Text")   # Text Handler handles Text document
#     # pdf_handler.handle_document("Excel")  # No handler available for Excel
#
#
#
#
#
#     # list_of_documents = [
#     #     'Word',
#     #     'PDF',
#     #     'Text',
#     #     'Excel',
#     #     'Word',
#     #     'PDF',
#     #     'PDF',
#     #     'Jpeg'
#     # ]
#     #
#     # for el in list_of_documents:
#     #     pdf_handler.handle_document(el)
#
#
#
#
#
#     while True:
#         doc = input('Введіть тип документу : ')
#         if doc != 'exit':
#             pdf_handler.handle_document(doc)
#         else:
#             break








"""
У цьому прикладі ми маємо три типи обробників документів: 
PDFHandler, WordHandler і TextHandler. 
Кожен обробник може обробити певний тип документа 
і має методи can_handle і process_document 
для визначення можливості обробки та обробки документу відповідно.

Ми встановлюємо ланцюжок обробників, 
де PDFHandler перевіряє, чи може він обробити документ. 
Якщо ні, він передає документ WordHandler, і так далі. 
У результаті, кожен документ обробляється відповідним обробником, 
або, якщо немає підходящого обробника, 
виводиться повідомлення про відсутність обробника.
"""