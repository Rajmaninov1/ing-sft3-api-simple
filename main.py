from fastapi import FastAPI
import translators as ts


app = FastAPI()

app.state.name = "usuario"
app.state.lang = "en"

@app.get("/demo/register")
async def read_item(name: str, lang: str):
    app.state.name = name
    app.state.lang = lang
    return {ts.google(query_text="completado con exito",to_language=lang): name}

@app.get("/demo/greeting")
async def read_item():
    return {ts.google(query_text="bienvenido",to_language=app.state.lang): app.state.name}