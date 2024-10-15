from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # вероятно в шаблоне ошибка, строка 23 изменена на get_books_genre
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("book_name", [
        "",
        "b" * 41
    ])
    def test_add_new_book_invalid_length(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize("book_name, book_genre", [
        ("1984", "Фантастика"),
        ("Дракула", "Ужасы"),
        ("Шерлок Холмс", "Детективы")
    ])
    def test_set_book_genre_three_genres(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_set_book_genre_invalid_name(self):
        collector = BooksCollector()

        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Неверный жанр")
        assert collector.get_book_genre("1984") == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.add_new_book('Марсианские хроники')
        collector.set_book_genre('Марсианские хроники', 'Фантастика')

        books = collector.get_books_with_specific_genre("Детективы")

        assert "Десять негритят" in books
        assert "Марсианские хроники" not in books

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Комедии")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")

        result = collector.get_books_for_children()
        assert "Книга1" in result
        assert "Книга2" not in result

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        assert "1984" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_exist(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Несуществующая книга")
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        collector.delete_book_from_favorites("1984")
        assert "1984" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_exist(self):
        collector = BooksCollector()

        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        collector.delete_book_from_favorites("Несуществующая книга")
        assert len(collector.get_list_of_favorites_books()) == 1
