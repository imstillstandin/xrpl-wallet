from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.xrpl_fetcher import get_wallet_tokens
from services.nft_fetcher import get_wallet_nfts
from services.price_fetcher import get_token_price
from services.fx_converter import convert_currency
from services.pnl_calculator import calculate_pnl

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change "*" to just your Vercel URL for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 Add this block right after app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ You can lock this down later to your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wallet/{address}")
def fetch_wallet(address: str):
    return get_wallet_tokens(address)

@app.get("/nfts/{address}")
def fetch_nfts(address: str):
    return get_wallet_nfts(address)

@app.get("/price/{currency}/{issuer}")
def fetch_price(currency: str, issuer: str):
    return get_token_price(currency, issuer)

@app.get("/convert")
def fx(amount: float, to: str):
    return convert_currency(amount, to)

@app.post("/pnl")
def pnl(data: dict):
    return calculate_pnl(data)
