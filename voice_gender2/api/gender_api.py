from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from .utils import predict_gender

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        gender = predict_gender(temp_path)
    except Exception as e:
        os.remove(temp_path)
        return JSONResponse(status_code=500, content={"error": str(e)})

    os.remove(temp_path)
    print(f"predicted_gender is: {gender}")
    return JSONResponse(content={"predicted_gender": gender})
