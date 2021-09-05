#PLease feel free to use the code and make comments
#  Date: 2021.08.03
#  Author: eugenex


from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import FastAPI, status
from typing import List
from schema import database, wealthng
import model as mdUser


app = FastAPI(title="Creating Endpoints Using FastAPI for Wealth.ng Products")

app.add_middleware(             #Middleware can connect to any server although not entirely optimal feel freee to customize
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)

@app.on_event("startup")                                            #HERE we start and disconnect the databasse with aync functions
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/wealthng/", response_model=mdUser.Wealthng, status_code = status.HTTP_201_CREATED)   #HERE HWE STATE OUR ENDPOINTS AND PERFORM CRUD OPERATIONS
async def create_product(wealth: mdUser.WealthngIn):
    """
        Here we try to create new wealthng product
    """
    query = wealthng.insert().values(product_name=wealth.product_name, minimum_investment=wealth.minimum_investment ,investment_return=wealth.investment_return, product_tenor=wealth.product_tenor, activate_rollover=wealth.activate_rollover)
    last_product_id = await database.execute(query)
    #here we connect to database

    return {**wealth.dict(), "product_id": last_product_id}

@app.put("/wealthng/{product_id}/", response_model=mdUser.Wealthng, status_code = status.HTTP_200_OK)
async def update_product(product_id: int, payload: mdUser.WealthngIn):
    """
        Here we try to overwite an existing wealthng product_ID
    """
    query = wealthng.update().where(wealthng.c.product_id == product_id).values(product_name=payload.product_name, minimum_investment=payload.minimum_investment,
                                                                                investment_return=payload.investment_return, product_tenor=payload.product_tenor, activate_rollover=payload.activate_rollover)
    await database.execute(query)
    return {**payload.dict(), "product_id": product_id}

@app.get("/wealthng/", response_model=List[mdUser.Wealthng], status_code = status.HTTP_200_OK)
async def read_products_list(skip: int = 0, take: int = 20):
    """
        Here we try to view the full list of products offered by
    """
    query = wealthng.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/wealthng/{product_id}/", response_model=mdUser.Wealthng, status_code = status.HTTP_200_OK)
async def read_notes(product_id: int):
    """
        Here we try to see a particuar product using product_id
    """
    query = wealthng.select().where(wealthng.c.product_id == product_id)
    return await database.fetch_one(query)

@app.delete("/wealthng/{product_id}/", status_code = status.HTTP_200_OK)
async def delete_note(product_id: int):
    """
        Delete product using product_id
    """
    query = wealthng.delete().where(wealthng.c.product_id == product_id)
    await database.execute(query)
    return {"message": "Servive with product_id: {} deleted successfully!".format(product_id)}

print('This is the sprint')