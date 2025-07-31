import sqlite3

def fix_schema():
    conn = sqlite3.connect("coletas.db")
    cursor = conn.cursor()
    
    # Get current schema
    cursor.execute("PRAGMA table_info(coletas)")
    current_columns = [col[1] for col in cursor.fetchall()]
    print("Current columns:", current_columns)
    
    try:
        # Add the new column if it doesn't exist
        cursor.execute("ALTER TABLE coletas ADD COLUMN numero_cotacao TEXT")
        print("Added numero_cotacao column successfully!")
        conn.commit()
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Column numero_cotacao already exists")
        else:
            print(f"Error adding column: {e}")
    
    conn.close()
    print("Schema update completed!")

if __name__ == "__main__":
    fix_schema()
