import mysql.connector
import random

# ---------- Database helpers ----------

def get_airports_30(db_conf):
    """
    Return a list of 30 random large EU airports.
    Each item is a dict: {'ident': 'EFHK', 'name': 'Helsinki-Vantaa', 'municipality': 'Helsinki'}
    """
    con = mysql.connector.connect(**db_conf)
    try:
        cur = con.cursor(dictionary=True)
        try:
            cur.execute("""
                SELECT ident, name, municipality
                FROM airport
                WHERE type = 'large_airport'
                  AND continent = 'EU'
                ORDER BY RAND()
                LIMIT 30
            """)
            rows = cur.fetchall()
            return rows
        finally:
            cur.close()
    finally:
        con.close()

def load_ascii_art_5(db_conf):
    """
    Get 5 ascii arts from table goals (name + code).
    Returns a list: [{'name': ..., 'code': ...}, ...]
    """
    con = mysql.connector.connect(**db_conf)
    try:
        cur = con.cursor(dictionary=True)
        try:
            cur.execute("SELECT name, code FROM goals ORDER BY id LIMIT 5")
            return cur.fetchall()
        finally:
            cur.close()
    finally:
        con.close()

# ---------- Game logic (functions only) ----------

def init_game(db_conf):
    """
    Build the initial game state.
    - Pick 30 airports from DB and shuffle them
    - Hide 5 codes at the first 5 shuffled airports
    - Choose a random start airport
    Returns a dict 'g' that holds all game data.
    """
    airports_list = get_airports_30(db_conf)        # list of dict rows
    # Build a dict for fast lookup by ident
    airports_by_ident = {}
    idents = []
    for row in airports_list:
        ident = row["ident"]
        airports_by_ident[ident] = row
        idents.append(ident)

    random.shuffle(idents)                           # random order of airports

    arts = load_ascii_art_5(db_conf)                 # 5 ascii arts
    # Hide codes at first 5 idents (no duplicates)
    code_positions = {}                              # ident -> {'name','code'}
    for i in range(5):
        ident = idents[i]
        code_positions[ident] = arts[i]

    start = random.choice(idents)

    g = {
        "airports_by_ident": airports_by_ident,      # dict for lookup
        "idents": idents,                            # list to iterate/list remaining
        "code_positions": code_positions,            # where codes live
        "start": start,
        "cur": start,
        "found_idents": set(),                       # set of idents where code found
        "visited": set([start]),                     # set of already visited idents
    }
    return g

def fmt(g, ident):
    """Make a readable line: IDENT - NAME - MUNICIPALITY (municipality may be None)."""
    row = g["airports_by_ident"][ident]
    muni = row.get("municipality") or ""
    return f"{ident} - {row['name']} - {muni}"

def move(g, dest_ident):
    """
    Move to an airport by its ident.
    - Update current location and visited set
    - If a code is hidden here and not collected yet, reveal it
    Returns a message to print.
    """
    if dest_ident not in g["airports_by_ident"]:
        return f"Airport {dest_ident} is not on the map!"

    g["cur"] = dest_ident
    g["visited"].add(dest_ident)

    msg = f"You are now at {fmt(g, dest_ident)}"

    if (dest_ident in g["code_positions"]) and (dest_ident not in g["found_idents"]):
        art = g["code_positions"][dest_ident]       # {'name':..., 'code':...}
        count_next = len(g["found_idents"]) + 1
        msg += f" | >>> CODE FOUND: {art['name']} ({count_next}/5) <<<\n"
        msg += (art["code"] or "")
        g["found_idents"].add(dest_ident)

    return msg

def is_win(g):
    """Win when we have found 5 codes."""
    return len(g["found_idents"]) == 5

def run_cli(db_conf):
    """Simple text UI."""
    # Optional: show intro if you have Intro.show_intro(); ignore if not present
    try:
        from Intro import show_intro
        show_intro()
    except Exception:
        pass

    g = init_game(db_conf)
    print(f"You are now at {fmt(g, g['start'])}")
    print("Commands: list  |  go <IDENT>  |  quit")

    # Main loop
    while not is_win(g):
        print(f"\nCodes found: {len(g['found_idents'])}/5 | Current location: {g['cur']}")
        parts = input("> ").split()     # split on spaces into tokens
        if not parts:
            continue

        cmd = parts[0].lower()          # accept LIST/Go/go, etc.

        if cmd == "list":
            # Build a list of unvisited airports (keep order of g['idents'])
            remaining = []
            for ident in g["idents"]:
                if ident not in g["visited"]:
                    remaining.append(ident)

            count = len(remaining)
            if count > 0:
                print(f"You only have {count} airports remaining:")
                # show the idents (you can replace with fmt(...) if you want names too)
                remaining_sorted = sorted(remaining)
                print(", ".join(remaining_sorted))
            else:
                print("(No more unvisited airports)")

        elif cmd == "go" and len(parts) >= 2:
            ident = parts[1].upper()    # airport codes are usually uppercase
            print(move(g, ident))

        elif cmd == "quit":
            break

        else:
            print("Invalid command.")

    if is_win(g):
        print(">>> WIN! You found all 5 codes. <<<")
        print(f'U have visited {g["visited"]}')


# ---------- Fill your DB config and run ----------

if __name__ == "__main__":
    db_conf = {
        "host": "127.0.0.1",
        "port": 3306,
        "database": "demogame",
        "user": "root",
        "password": "Giahung@!497",
        "autocommit": True,
        "auth_plugin": "mysql_native_password",
        "use_pure": True,
    }
    run_cli(db_conf)
