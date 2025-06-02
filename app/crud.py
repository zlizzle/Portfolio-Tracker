from typing import Optional
from typing import List
from sqlmodel import Session, select
from .database import engine
from .models import Asset
from .schemas import AssetCreate

def create_asset(*, asset: AssetCreate) -> Asset:
    asset_obj = Asset.from_orm(asset)
    with Session(engine) as session:
        session.add(asset_obj)
        session.commit()
        session.refresh(asset_obj)
        return asset_obj

def get_assets() -> List[Asset]:
    with Session(engine) as session:
        return session.exec(select(Asset)).all()

def update_asset(asset_id: int, asset_data: AssetCreate) -> Optional[Asset]:
    with Session(engine) as session:
        asset = session.get(Asset, asset_id)
        if not asset:
            return None
        asset.symbol = asset_data.symbol
        asset.quantity = asset_data.quantity
        asset.average_price = asset_data.average_price
        session.add(asset)
        session.commit()
        session.refresh(asset)
        return asset

def delete_asset(asset_id: int) -> bool:
    with Session(engine) as session:
        asset = session.get(Asset, asset_id)
        if not asset:
            return False
        session.delete(asset)
        session.commit()
        return True
