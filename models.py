from pydantic import BaseModel
from typing import Optional


class ProductRequest(BaseModel):
    url: str


class ProductInfo(BaseModel):
    url: str
    title: Optional[str] = None
    price: Optional[str] = None
    seller: Optional[str] = None
    description: Optional[str] = None
    ingredients: Optional[str] = None


class AnalysisResponse(BaseModel):
    success: bool
    message: str
    product: ProductInfo