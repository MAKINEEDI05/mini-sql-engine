def parse_query(query):
    """
    Parse a basic SQL SELECT query into structured components.
    """
    query = query.strip().rstrip(";")

    if not query.upper().startswith("SELECT"):
        raise Exception("Only SELECT queries are supported")

    # Split SELECT and rest
    select_part, rest = query.split("FROM", 1)
    select_part = select_part.replace("SELECT", "").strip()
    rest = rest.strip()

    where_clause = None

    # Handle WHERE clause
    if "WHERE" in rest:
        from_part, where_part = rest.split("WHERE", 1)
        where_clause = parse_where(where_part.strip())
    else:
        from_part = rest

    return {
        "select": parse_select(select_part),
        "from": from_part.strip(),
        "where": where_clause
    }


def parse_select(select_part):
    """
    Parse SELECT clause (columns or COUNT).
    """
    if select_part.upper().startswith("COUNT"):
        inside = select_part[6:-1].strip()
        return {"count": inside}

    if select_part == "*":
        return "*"

    return [col.strip() for col in select_part.split(",")]


def parse_where(where_part):
    """
    Parse WHERE clause with a single condition.
    """
    operators = [">=", "<=", "!=", "=", ">", "<"]

    for op in operators:
        if op in where_part:
            column, value = where_part.split(op)
            return {
                "column": column.strip(),
                "operator": op,
                "value": parse_value(value.strip())
            }

    raise Exception("Invalid WHERE clause")


def parse_value(value):
    """
    Convert value to int, float, or string.
    """
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]

    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value
