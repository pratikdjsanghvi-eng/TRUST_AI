from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import ProductRequest, ProductInfo, AnalysisResponse
from scraper import scrape_product
import requests


app = FastAPI(
    title="TrustCheck API",
    description="Online product and seller verification API",
    version="1.0.0"
)


# Allow our frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "TrustCheck API is running"
    }


@app.post(
    "/analyze",
    response_model=AnalysisResponse
)
def analyze_product(request: ProductRequest):

    try:

        product = scrape_product(
            request.url
        )

        return {
            "success": True,
            "message": "Product page analyzed successfully.",
            "product": product
        }

    except requests.exceptions.RequestException:

        raise HTTPException(
            status_code=400,
            detail="Could not access the product page."
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )