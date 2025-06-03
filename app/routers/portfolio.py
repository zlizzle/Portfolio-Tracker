from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..schemas import AssetCreate, AssetRead
from ..crud import create_asset, get_assets, update_asset, delete_asset
from ..utils import fetch_token_price

router = APIRouter()

@router.post("/", response_model=AssetRead)
def add_asset(asset: AssetCreate):
    return create_asset(asset=asset)

@router.get("/", response_model=List[AssetRead])
def list_assets():
    return get_assets()

@router.put("/{asset_id}", response_model=AssetRead)
def edit_asset(asset_id: int, asset: AssetCreate):
    updated = update_asset(asset_id, asset)
    if not updated:
        raise HTTPException(status_code=404, detail="Asset not found")
    return updated

@router.delete("/{asset_id}")
def remove_asset(asset_id: int):
    success = delete_asset(asset_id)
    if not success:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"ok": True}

@router.get("/price/")
def get_token_price(symbol: str = Query(..., example="SOL")):
    price = fetch_token_price(symbol)
    if price is None:
        raise HTTPException(status_code=404, detail="Token not found or no price available")
    return {"symbol": symbol.upper(), "price_usd": price}