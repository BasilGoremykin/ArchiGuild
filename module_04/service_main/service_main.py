from fastapi import Depends, FastAPI, HTTPException, Request
import requests

requests.adapters.DEFAULT_RETRIES = 5

class Author(object):
    def __init__(self, id, first_name, last_name, email, title, birth_date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.birth_date = birth_date
    pass
pass

class PresentationWithAuthor:
    def __init__(self, title, author, date):        
        self.title = title
        self.author = author
        self.date = date
    pass
pass

class Presentation(object):
    def __init__(self, title, author_id, date, author_last_name):        
        self.title = title
        self.author_id = author_id
        self.date = date
        self.author_last_name = author_last_name
    pass
pass

# Start FastAPI
app = FastAPI()

@app.get("/presentationsAndAuthor/{title}")
async def read_presentation(title: str):
    responsePresentation = requests.get(f"http://service_presentation:8082/presentations/{title}")
    if responsePresentation.status_code != 200:
        raise HTTPException(status_code=404, detail="No presentations for this title")
    
    presentation_data = responsePresentation.json()[0]
    #presentation_data = {k: v for k, v in presentation_data.items() if k != 'author_last_name'}
    presentation = Presentation(**presentation_data)

    responseAuthor = requests.get(f"http://service_author:8081/authors/{presentation.author_id}")
    if responseAuthor.status_code != 200:
        raise HTTPException(status_code=404, detail="No authors for this id")

    author_data = responseAuthor.json()
    author = Author(**author_data)

    presentation_with_author = PresentationWithAuthor(
        title=presentation.title,
        author={
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "email": author.email,
            "title": author.title,
            "birth_date": author.birth_date
        },
        date=presentation.date
    )
    
    return presentation_with_author
pass


