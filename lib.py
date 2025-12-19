import time

# constants
TAB = "	"
SPACE = " "
BR = "\n"
INSERT = "INSERT INTO [TABLE] VALUES"


# functions
def inputs(prompt: str = "") -> str:
    data = ""
    chunk = input(prompt)
    while chunk != "":
        data += chunk + BR
        chunk = input()
    return data


def time_ms() -> int:
    """Get time now in milliseconds since Unix epoch (Jan 1, 1970)."""
    return int(time.time() * 1000)


def excel2grid(data: str) -> list[list[str]]:
    """
    parse data copied from excel sheet to 2D list.

    row is separated by line break, column in separated by tabulation
    """
    return [
        [col.strip() for col in row.split(TAB)]
        for row in data.split(BR)
        if row.strip() != ""
    ]


def row2value(row: list[str]) -> str:
    return f"({', '.join([col if col == 'NULL' else f"'{col.replace("'", "''")}'" for col in row])})"


def row2column(row: list[str]) -> str:
    return f"({', '.join([f'[{col}]' for col in row])})"


def excel_insert(
    table: str, data: str, named: bool, atomic: bool = True, ignores: set[int] = set()
) -> str:
    """
    create insert query based on excel data

    `named` - whether to use fist row as header

    `atomic` - whether to insert 1 row of values at a time, easier for troubleshooting
    """
    grid = excel2grid(data)

    # remove ignored columns
    if ignores:
        indexes = list(ignores)
        if len(indexes) > 1:
            indexes.sort(reverse=True)
        for index in indexes:
            for row in grid:
                if index <= len(grid):
                    row.pop(index)

    header = None
    if named:
        header = grid.pop(0)
    query = INSERT.replace(
        "[TABLE]", f"[{table}] {row2column(header)}" if header else f"[{table}]"
    )
    result = ""

    isFirstRow = True
    for row in grid:
        if row.count("NULL") == len(row):
            continue

        value = row2value(row)
        if atomic:
            result += query + " " + value + ";\n"
        else:
            if not isFirstRow:
                result += ","
            result += "\n    " + value
            if isFirstRow:
                isFirstRow = False
    if not atomic:
        result = f"{query} {result};"

    return result
