html = open(r'login_template.txt', encoding='utf-8').read()
open(r'login.html', 'w', encoding='utf-8').write(html)
print('Done')
