# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
  html_1 = '<'+tag+'>'
  html_2 = '</'+tag+'>'
  return html_1+word+html_2
