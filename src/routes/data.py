import logging
import os

import aiofiles
import uvicorn
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse

from controllers import DataController, ProjectController
from helpers.config import Settings, get_settings
from models import ResponseSignal

logger = logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api/v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    
    
    # validate the file properties 
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
    
    file_path = data_controller.generate_unique_file_name(
        original_file_name=file.filename,
        project_id=project_id
    )
    
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
                
    except OSError as e:
        
        logger.error(f"Error occurred while uploading file: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
        
    return JSONResponse(
    content={
        "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
    }
)