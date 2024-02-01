import os

cryptid_sqlite_database = os.getenv("CRYPTID_SQLITE_DATABASE")

if cryptid_sqlite_database is not None:
    print(f"CRYPTID_SQLITE_DATABASE is set to: {cryptid_sqlite_database}")
else:
    print("CRYPTID_SQLITE_DATABASE is not set.")
