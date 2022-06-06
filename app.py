from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
    return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href="/animals/dogs">Dogs</a></li>
        <li><a href="/animals/cats">Cats</a></li>
        <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"<h1>List of {pet_type}</h1>"
    html += "<ul>"
    i = 0
    for animal in pets[pet_type]:
        html += f"<li><a href='/animals/{pet_type}/{i}'>{animal['name']}</a></li>"
        i += 1
    html += "</ul>"
    return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return f'''
    <h1>{pet['name']}</h1>
    <img src="{pet['url']}" alt="{pet['name']}" width="400">
    <p>{pet['description']}</p>
    <ul>
        <li><B>BREED</B>: {pet['breed']}</li>
        <li><B>AGE</B>: {pet['age']}</li>
    </ul>
    '''
