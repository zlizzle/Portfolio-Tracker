from fastapi import APIRouter
from typing import List
from ..schemas import AssetCreate, AssetRead
from ..crud import create_asset, get_assets

router = APIRouter()

@router.post("/", response_model=AssetRead)
def add_asset(asset: AssetCreate):
    return create_asset(asset=asset)

@router.get("/", response_model=List[AssetRead])
def list_assets():
    return get_assets()
