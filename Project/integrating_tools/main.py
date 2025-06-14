from fastapi import FastAPI
from statsmodels.base.covtype import descriptions

from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return  {"message": "Developer created successfully", "developer": developer}

@app.post("/projects/")
def create_project(project: Project):
    return{"message": "Project created successfully", "Project": project}


@app.get("/projects/")
def get_projects():
    sample_project = Project(
        title = "Sample Project",
        description = "This is a sample project",
        language = ["Python", "JavaScript"],
        lead_developer = Developer(name="John Doe", experience=5)
    )
    return {"Projects": [sample_project]}



















