print ('hello')

top_html = open ('./templates/top.html').read()
bottom_html = open ('./templates/bottom.html').read()
middle_html = open ('./content/index.html').read()

combined = top_html + bottom_html + middle_html

open ('./docs/index.html', 'w+').write(combined)


top_html = open ('./templates/top.html').read()
bottom_html = open ('./templates/bottom.html').read()
middle_html = open ('./content/order.html').read()

combined = top_html + bottom_html + middle_html

open ('./docs/order.html', 'w+').write(combined)


top_html = open ('./templates/top.html').read()
bottom_html = open ('./templates/bottom.html').read()
middle_html = open ('./content/prices.html').read()

combined = top_html + bottom_html + middle_html

open ('./docs/prices.html', 'w+').write(combined)
