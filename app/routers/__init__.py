from fastapi import APIRouter
from . import csv_handler, logging_handler

router = APIRouter()

router.include_router(csv_handler.router)
router.include_router(logging_handler.router)
