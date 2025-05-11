from fastapi import FastAPI, Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = FastAPI()

@app.post("/execute")
async def execute_action(req: Request):
    data = await req.json()
    url = data.get("url")
    action = data.get("action")
    selector = data.get("selector")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    if action == "click" and selector:
        driver.find_element(By.CSS_SELECTOR, selector).click()

    driver.save_screenshot("/tmp/screenshot.png")
    driver.quit()

    return {"status": "ok", "message": "Action complete"}
