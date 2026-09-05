def parse_minutes(raw):
    try:
        minutes = int(raw)
    except ValueError:
        return None
    if minutes <= 0:
        return None
    return minutes


def main():
    category = input("Category: ").strip()
    minutes = parse_minutes(input("Minutes: "))
    if not category or minutes is None:
        print("Use a category and positive whole minutes.")
    else:
        print(f"{category}: {minutes} minutes")


if __name__ == "__main__":
    main()
