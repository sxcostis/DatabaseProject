from db.databaseConnector import engine

with engine.connect() as engine:
    try:
        print("Connesso")
    except Exception as e:
        print(e)




