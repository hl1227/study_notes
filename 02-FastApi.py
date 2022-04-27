from fastapi import FastAPI

app = FastAPI()

@app.get('/test/a={a}/b={b}')
def calculate(a: int = None, b: int = None):
    c = a + b
    res = {"res": c}
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="127.0.0.1",
                port=5656,
                workers=1)