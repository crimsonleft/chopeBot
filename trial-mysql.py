from chopeDB import MySQLConnector


def main():
    db = MySQLConnector()
    args = []
    args.append(("USERNAME", 's', 'HOBO'))
    args.append(("PASSWORD", 's', 'mancay'))
    db.insert("LIBCHOP", args)
    db.close()


if __name__ == '__main__':
    main()