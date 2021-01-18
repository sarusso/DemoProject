
def sanitize_string(string, encode=False):
    if encode:
        try:
            sanitized_string = string.encode('ascii')
        except UnicodeError:
            sanitized_string = string.encode('utf-8')
    else:
        sanitized_string = string

    return sanitized_string


# Demo usage
if __name__ == '__main__':
    print(sanitize_string(u'Hello World!', encode=True))
    print(sanitize_string(u'Hello World!', encode=False))
    print(sanitize_string(u'\u4f60\u597d', encode=True))
    print(sanitize_string(u'\u4f60\u597d', encode=False))
