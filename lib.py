# constants
TAB = "	"
SPACE = " "
BR = "\n"
INSERT = "INSERT INTO [TABLE] VALUES"


# functions
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
    return f"({', '.join([col if col == 'NULL' else f"'{col}'" for col in row])})"


def row2column(row: list[str]) -> str:
    return f"({', '.join([f'[{col}]' for col in row])})"
