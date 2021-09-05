#PLease feel free to use the code and make comments
#  Date: 2021.08.03
#  Author: eugenex
from pydantic import Field,BaseModel

class WealthngIn(BaseModel):
    product_name: str = Field(..., example="Tresaury Bills")
    minimum_investment: int = Field(..., example=10000 )
    investment_return:  int = Field(..., example=27)
    product_tenor: str = Field(..., example="30Days")
    activate_rollover: bool

class Wealthng(BaseModel):
    product_id: int
    product_name: str
    minimum_investment: int
    investment_return: int
    product_tenor: str
    activate_rollover: bool
