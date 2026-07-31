from fastapi import FastAPI

app = FastAPI(
    title="CableCalc",
    description="Professional Electrical Cable Sizing Software",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CableCalc",
        "version": "0.1.0",
        "status": "Running"
    }