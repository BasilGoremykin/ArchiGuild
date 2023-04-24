from fastapi import Depends, FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
import json
import yaml
from datetime import date

class Author(object):
    '''Class Author'''
    id : int
    first_name : str
    last_name : str
    email : str
    title : str
    birth_date : date
#   birth_year = int
    def __init__(self, id, first_name, last_name, email, title, birth_date):
      self.id = id
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.title = title
      self.birth_date = birth_date
pass

# Start FastAPI
app = FastAPI()

#load data(Authors) from file
json_file_path = "ExportJson.json"  #file path \service_author\\
with open(json_file_path, 'r') as j:
    loadJsonAuthors = json.loads(j.read())
    print(type(loadJsonAuthors))    

    #convert json loadJsonAuthors to python object list of Author
    authors =  []
    for i, val in enumerate(loadJsonAuthors):
        authors.append(Author(**val))

with open("service_author.yml", "r") as yamlfile:
    spec = yaml.safe_load(yamlfile)

app.openapi_schema = spec

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Conference server API",
        version="1.0.0",
        description="API to retrieve information about main entities of Conference server",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

#get Author by id
@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    author = [val for (it, val) in enumerate(authors) if val.id == author_id]

    if not author:
        raise HTTPException(status_code=404, detail="No author for this id")
    return author[0]

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


