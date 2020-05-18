from flask import Flask, render_template
from forms import searchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ivke.2303990'
headline = "Rečnik rodno-ravnopravnih zanimanja"

data = {
   'administratorka' : 'administrator',
   'admiralica, admiralka' : 'admiral',
   'advokatica, advokatkinja' : 'advokat',
   'agentkinja, agentica' : 'agent',
   'akupresuristkinja' : 'akupresurist(a)',
   'dezinsektorka' : 'dezinsektor',
   'hematološkinja' : 'hematolog',
   'abcde' : 'abcdef'
}

def search(data, searchFor):
   for key, val in data.items():
      if key in searchFor:
         return val
      elif val in searchFor:
         return key
      else:
         inputLentgh = len(searchFor)
         dataLentgh = len(key) * 100 / 50
         print('key is ->', key)
         print('data lentgh -> ', dataLentgh)
         matchedCharacters = set(searchFor).intersection(key)
         print('matched characters -> ', len(matchedCharacters)*6)
         if len(matchedCharacters) * 7 >= dataLentgh:
            matchedItems = []
            matchedItems.append([key, val])
            print(matchedItems)
   return 'nije pronadjen rezultat'

def searchFilter(searchFor, key):
   counter = 0
#   for character in key:
#      for char in searchFor


   return 'TO-DO'

s = search(data, 'administrator')
print(s)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
   form = searchForm()
   term = search(data, format(form.search.data))
   if form.validate_on_submit():
      return render_template('recnik.html', headline=headline, headline2=term, form=form)
   return render_template('recnik.html', headline=headline, form=form)

if __name__ == '__main__':
   app.run()