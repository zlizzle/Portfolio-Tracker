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
