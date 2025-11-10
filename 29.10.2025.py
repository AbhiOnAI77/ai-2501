# Data Processing Code 1
from bs4 import BeautifulSoup

str1 = "<h1> Digital Edify - India 's #1 Premium Training Institute </h1>"

cleaned_text = BeautifulSoup(str1, 'html.parser').get_text()

print(cleaned_text)

#str2 = 

str3 = """<div class="brand">
          <img src="/img/logo.png" alt="Digital Edify logo">
          <h1>Digital Edify </h1> 
          <p> India's #1 Premium Training Institute </p>
        </div>
       """
