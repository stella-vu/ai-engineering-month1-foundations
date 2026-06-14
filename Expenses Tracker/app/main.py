from fastapi import FastAPI, Query, Depends, UploadFile, File, HTTPException
from schemas import TransactionCreate, TransactionResponse,TransactionUpdate
from transaction_service import TransactionService

app = FastAPI()

ALLOWED_FILE_TYPES = {
    "application/pdf",
    "text/plain",
    "text/csv"
}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()

    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="File type not supported"
        )
    
    return {
        "file_name": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(content)
    }


def get_transaction_service():
    return TransactionService()

@app.get("/transactions", response_model=list[TransactionResponse])
def get_transactions(
    user_id: str | None = None,
    transaction_type: str | None = None,
    category: str | None = None,
    min_amount: float | None = None,
    max_amount: float | None = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    service: TransactionService = Depends(get_transaction_service)
):
    return service.get_transactions(
        user_id=user_id,
        transaction_type=transaction_type,
        category=category,
        min_amount=min_amount,
        max_amount=max_amount,
        limit=limit,
        offset=offset
    )

@app.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def get_transactions_by_id(
    transaction_id: str,
    service: TransactionService = Depends(get_transaction_service)
):
    return service.get_transaction_by_id(transaction_id)


@app.post("/transactions", status_code=201)
def add_transaction(
    transaction: TransactionCreate,
    service: TransactionService = Depends(get_transaction_service)
):

    row = service.create_transaction(transaction)

    return {
        "message": "Add transaction successfully",
        "transaction_id": row["transaction_id"],
        "detail": transaction
    }

@app.put("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_transaction(
    transaction_id: str, 
    updated_tran: TransactionUpdate,
    service: TransactionService = Depends(get_transaction_service)
):
    return service.update_transaction(transaction_id, updated_tran)

@app.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: str,
    service: TransactionService = Depends(get_transaction_service)    
):
   row = service.delete_transaction(transaction_id.upper())
   return {"message": f"Successfully deleted transaction {row['transaction_id']}"}