from fastapi import FastAPI

app = FastAPI(title="H.B-SYST API")

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "system": "H.B-SYST",
        "message": "Welcome to Hamid Bolhasani's Knowledge Base"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
