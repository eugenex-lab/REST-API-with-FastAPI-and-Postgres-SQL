#PLease feel free to use the code and make comments
#  Date: 2021.08.03
#  Author: eugenex
from pydantic import Field,BaseModel

class WealthngIn(BaseModel):
    product_name: str = Field(..., example="Tresaury Bills")
    minimum_investment: int = Field(..., example="10,000 Naira")
    investment_return:  str= Field(..., example="2.13%")
    product_tenor: str = Field(..., example="30Days")
    activate_rollover: bool = Field(..., example=" Our Bespoke Service gurantee your investments")

class Wealthng(BaseModel):
    product_id: int
    product_name: str
    minimum_investment: int
    investment_return: str
    product_tenor: str
    activate_rollover: bool
