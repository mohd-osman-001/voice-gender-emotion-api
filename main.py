from fastapi import FastAPI
import os
import uvicorn

# Routers
from Emotion_Detection.emotion_api import router as emotion_router
from voice_gender2.api.gender_api import router as gender_router

app = FastAPI(
    title="Unified Voice Gender and Emotion API",
    version="1.0.0",
    description="This API can predict gender from audio and emotion from text."
)

# Register routers
app.include_router(gender_router, prefix="/gender", tags=["Gender Prediction"])
app.include_router(emotion_router, prefix="/emotion", tags=["Emotion Detection"])

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to the Unified Voice Gender and Emotion API!",
        "available_endpoints": {
            "Gender Prediction": "/gender/predict",
            "Emotion Detection": "/emotion/predict",
            "Docs": "/docs"
        }
    }

# Entry point for running with uvicorn
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
