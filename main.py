# Create hello world FastAPI app
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"MeSsAge": "Nothing's working - mark test commit! => Another test commit"}
