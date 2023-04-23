from fastapi import Depends, FastAPI, HTTPException, Request
import json
import requests
from datetime import date

class Presentation:
    def __init__(self, title: str, author_id: int, date: str, author_last_name: str = ""):
        self.title = title
        self.author_id = author_id
        self.date = date
        self.author_last_name = author_last_name

def get_author_last_name(author_id: int) -> str:
    response = requests.get(f"http://service_author:8081/authors/{author_id}")
    if response.status_code == 200:
        author = response.json()
        return author["last_name"]
    else:
        raise HTTPException(status_code=404, detail="Author not found")

json_file_path = "ExportJsonPresentation.json"
with open(json_file_path, 'r') as j:
    loadJsonPresentations = json.loads(j.read())

    presentations =  []
    for val in loadJsonPresentations:
        author_last_name = get_author_last_name(val["author_id"])
        presentation = Presentation(
            title=val["title"],
            author_id=val["author_id"],
            date=val["date"],
            author_last_name=author_last_name
        )
        presentations.append(presentation)

app = FastAPI()

@app.get("/presentations/{title}")
async def read_presentation(title: str):
    presentation_list = [val for val in presentations if val.title == title]
    if not presentation_list:
        raise HTTPException(status_code=404, detail="No presentations for this title")

    result = []
    for presentation in presentation_list:
        author_last_name = get_author_last_name(presentation.author_id)
        presentation.author_last_name = author_last_name
        result.append(presentation)

    return result

@app.get("/presentations")
async def get_all_presentations():
    return presentations