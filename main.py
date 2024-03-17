from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from scraper import scrape_data
from save_data import save_to_db

app = FastAPI()

@app.post("/scrape/{page_name}")
async def scrape_page(page_name: str):
    try:
        posts = scrape_data(page_name)
        save_to_db(posts, page_name)
        return JSONResponse(content={"page_name": page_name, "posts": posts})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
