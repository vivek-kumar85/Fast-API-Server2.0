from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import os
import pandas as pd
import time
from io import StringIO

router = APIRouter()

@router.post("/upload", status_code=201)
async def upload_csv(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode('utf-8')))
        os.makedirs('files', exist_ok=True)
        timestamp_str = time.strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"files/{timestamp_str}.csv"
        df.to_csv(file_path, index=False)
        return JSONResponse(content={"message": f"CSV file saved to {file_path}"}, status_code=200)
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=422, detail="The uploaded CSV file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
