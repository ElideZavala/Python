import webbrowser

# Lista de URLs
urls = [
    'http://google.com',
    'http://github.com',
    'http://python.org'
]

# Abre cada URL en una nueva pestaña
for url in urls:
    webbrowser.open_new_tab(url)

# Buscar algo en Google
search_query = 'Python programming'
webbrowser.open(f'https://www.google.com/search?q={search_query}')
