import pytest
from library.models import Author,Book

# Тест с использованием фикстуры для автора и книги
# Тест без фикстуры
# Тест с несколькими авторами - параметризорованный тест
# Тест на удаление CASCADE
# Тест связанных запросов(тестируем ForgenKey)

# Тест автора, через фикстуру
def test_author_fixture(author):
    assert author.name == 'Тестовый Автор'
    assert Author.objects.count() == 1

# Тест книги, через фиксутуру
def text_book_fisture(book,author):
    assert book.title == 'Горе от ума'
    assert book.author == author
    assert author.books.count() == 1

# 
