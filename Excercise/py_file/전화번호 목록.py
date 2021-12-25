def solution(phone_book):
    book = sorted(phone_book)
    for p1, p2 in zip(book, book[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution(phone_book):
    book = sorted(phone_book):
    for i in range(len(book)-1):
        if len(book[i]) < len(book[i+1]):
            if book[i+1][:len(book[i])] == book[i]:
                return False
    return True