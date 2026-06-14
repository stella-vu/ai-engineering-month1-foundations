import logging
from fastapi import HTTPException
from db import Database


TRANSACTION_FIELDS = """
    transaction_id,
    user_id,
    date,
    transaction_type,
    category,
    amount,
    payment_mode,
    location,
    notes
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TransactionService:

    def __init__(self):
        self.db = Database()

    def get_transaction_by_id(self, transaction_id: str):

        cursor = self.db.get_cursor()

        cursor.execute(
            f"""
            SELECT
                {TRANSACTION_FIELDS}
            FROM transactions
            WHERE transaction_id = %s
            """,
            (transaction_id.upper(),)
        )

        row = cursor.fetchone()

        cursor.close()

        if not row:
            raise HTTPException(
                status_code=404,
                detail="Transaction not found"
            )

        return row

    def get_transactions(
        self,
        user_id=None,
        transaction_type=None,
        category=None,
        min_amount=None,
        max_amount=None,
        limit=20,
        offset=0                        
        ):

        cursor = self.db.get_cursor()

        query = f"""
            SELECT
                {TRANSACTION_FIELDS}
            FROM transactions
            WHERE 1=1
            """
        
        params = []

        if user_id is not None:
            query += " AND user_id = %s"
            params.append(user_id.upper())
        
        if transaction_type is not None:
            query += " AND transaction_type = %s"
            params.append(transaction_type.title())
        
        if category is not None:
            query += " AND category = %s"
            params.append(category.title())
        
        if min_amount is not None:
            query += " AND amount >= %s"
            params.append(min_amount)
        
        if max_amount is not None:
            query += " AND amount <= %s"
            params.append(max_amount)

        query += "\nORDER BY transaction_number DESC \nLIMIT %s OFFSET %s "
        params.extend([limit, offset])

        cursor.execute(query,tuple(params))
        rows = cursor.fetchall()

        cursor.close()

        return rows

    def create_transaction(self, transaction):

        cursor = self.db.get_cursor()
        
        try:
            cursor.execute(
                """
                INSERT INTO transactions(
                    user_id,
                    date,
                    transaction_type,
                    category,
                    amount,
                    payment_mode,
                    location,
                    notes
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                RETURNING transaction_id
                """,
                (
                    transaction.user_id,
                    transaction.date,
                    transaction.transaction_type,
                    transaction.category,
                    transaction.amount,
                    transaction.payment_mode,
                    transaction.location,
                    transaction.notes
                )
            )

            row = cursor.fetchone()
            self.db.commit()
            logger.info(f"Transaction created: {row['transaction_id']}")
            return row
            
        except Exception as e:
            logger.error(f"Create transaction failed")
            raise HTTPException (
                status_code=500,
                detail= "Database error"
            )
        finally:
            cursor.close()
        

    def update_transaction(self, transaction_id: str, transaction_update):
        cursor = self.db.get_cursor()

        origin_tran = self.get_transaction_by_id(transaction_id)
        update_data = transaction_update.model_dump(exclude_none=True)

        merged = {**origin_tran, **update_data}
        
        cursor.execute(
            """
                UPDATE transactions
                SET 
                    date = %s,
                    transaction_type = %s,
                    category = %s,
                    amount = %s,
                    payment_mode = %s,
                    location = %s,
                    notes = %s
                WHERE transaction_id = %s
                RETURNING transaction_id;
            """,
            (merged["date"], 
            merged["transaction_type"],
            merged["category"],
            merged["amount"],
            merged["payment_mode"],
            merged["location"],
            merged["notes"],
            merged["transaction_id"],)
        )
        row = cursor.fetchone()
        self.db.commit()
        cursor.close()
        merged["transaction_id"] = row["transaction_id"]
        return merged

    def delete_transaction(self, transaction_id: str):

        cursor = self.db.get_cursor()

        cursor.execute(
            """
            DELETE FROM transactions
            WHERE transaction_id = %s
            RETURNING transaction_id
            """,
            (transaction_id.upper(),)
        )

        row = cursor.fetchone()

        if not row:
            cursor.close()

            raise HTTPException(
                status_code=404,
                detail="Transaction not found"
            )

        self.db.commit()

        cursor.close()

        return row