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
def get_token_price(symbol: str = Query(..., openapi_examples="SOL")):
    price = fetch_token_price(symbol)
    if price is None:
        raise HTTPException(status_code=404, detail="Token not found or no price available")
    return {"symbol": symbol.upper(), "price_usd": price}

@router.get("/portfolio/value")
def get_portfolio_value():
    assets = get_assets()
    total_value = 0.0
    total_pnl = 0.0
    breakdown = []
    warnings = []

    for asset in assets:
        price = fetch_token_price(asset.symbol)
        if price is None:
            breakdown.append({
                "symbol": asset.symbol,
                "quantity": asset.quantity,
                "average_price": round(asset.average_price, 2),
                "live_price_usd": None,
                "value_usd": None,
                "pnl_usd": None,
                "error": "Price not found"
            })
            warnings.append(f"Price not found for {asset.symbol}")
            continue
        value = round(asset.quantity * price, 2)
        pnl = round((price - asset.average_price) * asset.quantity, 2)
        total_value += value
        total_pnl += pnl
        breakdown.append({
            "symbol": asset.symbol,
            "quantity": asset.quantity,
            "average_price": round(asset.average_price, 2),
            "live_price_usd": round(price, 2),
            "value_usd": round(value, 2),
            "pnl_usd": round(pnl, 2)
        })


    response = {
        "total_portfolio_value_usd": round(total_value, 2),
        "total_portfolio_pnl_usd": round(total_pnl, 2),
        "assets": breakdown
    }
    if warnings:
        response["warnings"] = warnings
    return response