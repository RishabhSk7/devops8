from fastapi import FastAPI
app = FastAPI()
import uvicorn

@app.get("/")
def read_root():
    return dict(name = "Rishabh", Location = "Deheradun")

@app.get("/{data}")
def read_root(data):
    return dict(hi = data, Location = "Deheradun")

if __name__ == "main":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
