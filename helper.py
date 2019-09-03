#判断是isbn吗？是isbn13还是isbn10
def is_isbn_or_key(word):
    if len(word) == 13 and word.isdigit:
        isbn_or_key = 'isbn'
    short_word = word.replace( '-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
        return isbn_or_key