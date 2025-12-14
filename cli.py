from loader import load_csv
from parser import parse_query
from engine import execute_query


def main():
    print("Mini SQL Engine")
    print("Type 'exit' or 'quit' to quit\n")

    file_path = input("Enter CSV file path: ")

    try:
        data = load_csv(file_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    while True:
        query = input("sql> ")

        if query.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            parsed_query = parse_query(query)
            result = execute_query(parsed_query, data)

            print("Result:")
            print(result)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
