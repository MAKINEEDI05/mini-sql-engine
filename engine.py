def apply_where(rows, where_clause):
    """
    Filter rows based on WHERE clause.
    """
    if where_clause is None:
        return rows

    def row_matches(row):
        column = where_clause["column"]
        operator = where_clause["operator"]
        value = where_clause["value"]

        if column not in row:
            raise Exception(f"Column not found: {column}")

        cell_value = row[column]

        # Type conversion for numeric comparison
        try:
            if isinstance(value, (int, float)):
                cell_value = float(cell_value)
        except ValueError:
            raise Exception("Type mismatch in WHERE clause")

        if operator == "=":
            return cell_value == value
        if operator == "!=":
            return cell_value != value
        if operator == ">":
            return cell_value > value
        if operator == "<":
            return cell_value < value
        if operator == ">=":
            return cell_value >= value
        if operator == "<=":
            return cell_value <= value

        raise Exception("Unsupported operator")

    return [row for row in rows if row_matches(row)]


def apply_count(rows, target):
    """
    Apply COUNT aggregation.
    """
    if target == "*":
        return len(rows)

    return sum(1 for row in rows if row.get(target))


def apply_select(rows, select_clause):
    """
    Apply SELECT projection.
    """
    if select_clause == "*":
        return rows

    result = []
    for row in rows:
        projected = {}
        for column in select_clause:
            if column not in row:
                raise Exception(f"Column not found: {column}")
            projected[column] = row[column]
        result.append(projected)

    return result


def execute_query(parsed_query, data):
    """
    Execute parsed SQL query on in-memory data.
    """
    filtered_rows = apply_where(data, parsed_query["where"])

    if isinstance(parsed_query["select"], dict):
        return apply_count(filtered_rows, parsed_query["select"]["count"])

    return apply_select(filtered_rows, parsed_query["select"])
