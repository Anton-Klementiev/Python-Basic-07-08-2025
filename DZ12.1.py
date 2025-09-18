import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned = ''
    tag = False
    for c in html:
        if c == '<':
            tag = True
        elif c == '>':
            tag = False
        elif not tag:
            cleaned += c

    final = ''
    current_line = ''
    for char in cleaned:
        if char == '\n':
            if any(c not in (' ', '\t') for c in current_line):
                final += current_line + '\n'
            current_line = ''
        else:
            current_line += char

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final)

    return result_file

delete_html_tags('draft.html')
