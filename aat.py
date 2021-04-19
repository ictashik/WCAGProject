import automated_accessibility_testing
filename ="colortest.html"
with open(filename, "r", encoding='utf-8') as f:
    text= f.read()
print(text)
print((automated_accessibility_testing.check_accessibility(text)))
