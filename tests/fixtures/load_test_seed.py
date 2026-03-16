import pathlib


def load_sql_file(session, filename):

    sql = pathlib.Path(filename).read_text()

    session.execute(sql)
    session.commit()
