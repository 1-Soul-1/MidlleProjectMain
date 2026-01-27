import pytest
from library.models import Author,Book

# Тест с использованием фикстуры для автора и для книги
# Тест без фикстуры 
# тест с несколькими авторами 
# -параметризированый тест
# -тест на удаление Cascade
# Тест связанных запросов ( тестируем ForgenKey)


# Тест автора через фикстуру
@pytest.mark.django_db
def test_author_fixture(author):
    assert author.name == "Тестовый Автор"
    assert Author.objects.count() == 1

@pytest.mark.django_db
def test_book_fixture(book,author):
    # Тест книги через фикстуру
    assert book.title == "Горе от ума"
    assert book.author == author
    assert author.books.count() == 1
