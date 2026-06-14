from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Literal, Optional
from datetime import date as Date


TransactionType = Literal["Expense", "Income"]
PaymentModeType = Literal["Cash", "Card", "Bank Transfer", "UPI"]

class TransactionBase(BaseModel):
    date: Optional[Date] = None
    transaction_type: TransactionType = Field(...,description="The classification of the transaction.")
    category: Optional[str] = Field(None,description="The category of transaction.")
    amount: Decimal = Field(gt=0, max_digits= 10, decimal_places=2, description="The transaction amount.")
    payment_mode: Optional[PaymentModeType] = None  
    location: Optional[str] = Field(None, max_length=100, description="The location of transaction")
    notes: Optional[str] = Field(None, max_length= 512, description= "Transaction description")
    

class TransactionCreate(TransactionBase):
    user_id: str
    date: Date = Field(default_factory= Date.today)
    category: str = Field(..., description="The category of transaction.")
    payment_mode: PaymentModeType

class TransactionResponse(TransactionBase):
    transaction_id: str
    user_id: str

class TransactionUpdate(BaseModel):
    date: Optional[Date] = None
    transaction_type: Optional[TransactionType] = None
    category: Optional[str] = Field(None,description="The category of transaction.")
    amount: Optional[Decimal] = Field(None, gt=0, max_digits= 10, decimal_places=2, description="The transaction amount.")
    payment_mode: Optional[PaymentModeType] = None  
    location: Optional[str] = Field(None, max_length=100, description="The location of transaction")
    notes: Optional[str] = Field(None, max_length= 512, description= "Transaction description")
