import pytest
from library.models import Author,Book

@pytest.fixture
def author():
    # Фикстура создания автора
    return Author.objects.create(name='Тестовый Автор')

@pytest.fixture
# Фикстура для создания книги
def book(author):
    return Book.objects.create(title='Горе от ума',author=author)

@pytest.fixture
# Фикстура с несколькими авторами 
def multiple_authors():
    authors = []
    for i in range(10):
        author = Author.objects.create(name=f'Автор {i}')
        authors.append(author)
    
    return authors

@pytest.fixture
# Фикстура автора с несколькими книгами 
def author_with_books():
    author = Author.objects.create(name='Шухрат')
    for i in range(10):
        Book.objects.create(title=f"Книга {i}",author=author)
    return author
