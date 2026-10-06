from Task_manager.db import cursor, mydb

cursor.execute("""

    create table if not exists tasks(
    id int auto_increment primary key, 
    task varchar(50),
    status varchar(50)
    )

""")

print("table created successfully..")