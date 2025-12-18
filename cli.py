import lib

print("""
+----------------------------------+
| Generate INSERT query from Excel |
+----------------------------------+
""")
while True:
    table = input("Table name: ")
    named = None
    while named is None:
        value = input("Has header? ").lower()
        named = (
            True if value in ("y", "yes") else False if value in ("n", "no") else None
        )
    while True:
        try:
            ignore = [int(val) for val in input("Ignores: ").split()]
        except Exception:
            print("Error, try again.")
        else:
            break

    data = lib.inputs("Data rows:\n")
    try:
        query = lib.excel_insert(
            table,
            data,
            named,
        )
        with open(f"out/{lib.time_ms()}.sql", "wb") as f:
            f.write(query.encode("UTF-8"))
    except Exception:
        pass
