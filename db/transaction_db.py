from datetime import datetime
from pydantic import BaseModel

"""
aca estamos creando la clase TransactionInDB que hereda o extiende de la clase padre (BaseModel)
"""

class TransactionInDB(BaseModel):
    id_transaction: int = 0
    username: str
    date: datetime = datetime.now()
    value: int
    actual_balance: int


"""
aca estamos creando una lista vacia que iremos asignandole valores a cada uno de los atributos de la clase TransactionInDB, esta es la base de datos ficticia
"""

database_transactions = []
generator = {"id":0}
def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db