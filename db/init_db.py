from db.databaseConnector import Base, engine

def create_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_db()
    print("Database created")