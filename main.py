from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import logging
import urllib3

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

app = FastAPI()

http = urllib3.PoolManager()

@app.get("/")
def getPage(url: str):
    r = http.request('GET', url)
    return HTMLResponse(content = r.data, status_code=200)
    