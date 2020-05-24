import psycopg2


def todoDbAction(command, task, file):
    try:
        connection = psycopg2.connect(user="usertm",
                                      password="password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="TaskManager")

        cursor = connection.cursor()
        if task is None and file != ' ' and len(file) > 0:
            if command == 'Create':
                str = "insert into todo_list_name values('%s')"
            elif command == 'Delete':
                str = "delete from todo_list_name where list_name = '%s'"
            args = file
        elif task != ' ' and file != ' ' and len(file) > 0 and len(task) > 0:
            if command == 'Add':
                str = "insert into todo_names values('%s','%s',DEFAULT)"
            elif command == 'Delete':
                str = "delete from todo_names where list_name= '%s' and todo_name = '%s'"
            elif command == 'Check':
                str = "update todo_names set completed = true where list_name= '%s' and todo_name = '%s' "
            elif command == 'Uncheck':
                str = "update todo_names set completed = false where list_name= '%s' and todo_name = '%s'  "
            args = (file, task)
            if command == 'Clear All':
                str = "delete from todo_names where list_name= '%s'"
                args = (file)
        else:
            str= ""
        cursor.execute(str % args)
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        connection.rollback()
        connection.rollback()
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
