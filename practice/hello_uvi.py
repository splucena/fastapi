from fastapi import FastAPI

app = FastAPI()


# @app.get('/hi/{who}')
@app.get('/hi')
def greet(who):
    return f"Hello? World? from .... {who}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello_uvi:app", reload=True, port=8001)

# python ./hello_uvi.py
# http http://localhost:8001/hi/Sumilang
# Hello? World? from .... Sumilang
