import sqlite3

def fix_cliente_schema():
    conn = sqlite3.connect("coletas.db")
    cursor = conn.cursor()
    
    try:
        # Add the inscricao_estadual column
        cursor.execute("ALTER TABLE clientes ADD COLUMN inscricao_estadual TEXT")
        conn.commit()
        print("Added inscricao_estadual column successfully!")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Column inscricao_estadual already exists")
        else:
            print(f"Error adding column: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    fix_cliente_schema()
