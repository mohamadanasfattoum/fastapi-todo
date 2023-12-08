from fastapi import FastAPI, Depends, Request, Form, status

from starletts.respnses import RedirectResponse
from starletts.templating import Jinja2Templates

app = FastAPI()


@app.get('/')
def home():
    return{'Hello':'Todo API '}