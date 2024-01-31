from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import os
import logging
import time

router = APIRouter()

logging.basicConfig(filename="server_logs.log", level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

@router.post("/receive-logfile", status_code=201)
async def receive_logfile(file: UploadFile = File(...)):
    try:
        content = await file.read()
        if not content:
            raise HTTPException(status_code=422, detail="The uploaded file is empty")
        os.makedirs('logs', exist_ok=True)
        timestamp_str = time.strftime("%Y-%m-%d_%H-%M-%S")
        log_file_path = f"logs/log_{timestamp_str}.log"
        with open(log_file_path, 'wb') as log_file:
            log_file.write(content)
        logging.info(f"Log file received and saved to {log_file_path}")
        return JSONResponse(content={"message": "Log file successfully received and saved"}, status_code=200)
    except Exception as e:
        logging.error(f"Error during log file reception: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
