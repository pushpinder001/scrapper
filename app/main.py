from fastapi import FastAPI
from app.routers.scrapper_router import ScrapperRouter
from app.containers.app_container import AppContainer
from dependency_injector import containers, providers
import logging


app = FastAPI()
container = AppContainer()

# Create an instance of the UserRouter class


@app.on_event("startup")
def setup_container():
    container.init_resources()
    container.wire(modules=["app.routers.scrapper_router"])

# Include the user router
scrapper_router = ScrapperRouter()
app.include_router(scrapper_router.router)

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s  ',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
  )