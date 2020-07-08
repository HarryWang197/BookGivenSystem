
def is_isbn_or_key(word):
    """
        用于判断是ISBN还是关键字
    """
    # word 包括关键字以及ISBN号
    # ISBN13 由13各0-9的数字组成
    # ISBN10 由10各0-9的数字组成，且包括‘-’
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key