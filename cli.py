import lib

print("""
+----------------------------------+
| Generate INSERT query from Excel |
+----------------------------------+
""")
while True:
    hasHeader = None
    while hasHeader is None:
        value = input("Has header? ").lower()
        hasHeader = (
            True
            if value in ("y", "yes")
            else False
            if value in ("n", "no", "")
            else None
        )
    table = input("Table name: ")
    ignores = set()
    while True:
        try:
            ignores = {int(val) for val in input("Ignores (column indexes): ").split()}
        except Exception:
            print("Error, try again.")
        else:
            break

    nostrips = set()
    while True:
        try:
            nostrips = {
                int(val) for val in input("Don't Strip (column indexes): ").split()
            }
        except Exception:
            print("Error, try again.")
        else:
            break

    data = lib.inputs("Data rows:\n")
    try:
        query = lib.excel_insert(
            table, data, ignores, hasHeader=hasHeader, nostrips=nostrips
        )
        with open(f"out/{lib.time_ms()}.sql", "wb") as f:
            f.write(query.encode("UTF-8"))
        print("Done")
    except Exception as e:
        print(f"Error: {e}")
    print("")
