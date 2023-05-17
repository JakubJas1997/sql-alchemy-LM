from sqlalchemy import create_engine

def main():
    engine = create_engine("mysql+pymysql://root:qwerty@localhost:3306/")

    sql = " CREATE SCHEMA IF NOT EXISTS champ_league;"

    with engine.connect() as con:
        con.execute(sql)



if __name__ == "__main__":
    main()