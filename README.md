# django-invoices

A simple invoicing app made in Django for the "Scripting Languages" course at the School of Computing, Belgrade.

## Requirements

* Python 3
* [Django][django]
* MySQL 5.7+
  * The [`run-mysql.sh`][run-mysql] script can be used on Linux/macOS operating systems to run MySQL server in a
    Docker container.
    * Using this script in the production environments is heavily discouraged.
    * The script is used such as: `MYSQL_ROOT_PASSWORD=... ./hack/run-mysql.sh`.
    * The script creates `mysql` directory in the `./hack` directory mounted as `/var/lib/mysql` in the container. This
      directory is included in the `.gitignore` file.
* [MySQL Python client (`mysqlclient`)][mysqlclient]

Requirements regarding Python/Django dependencies can be found in the [`requirements.txt`][requirements] file.

### Generating The `requirements.txt` File

The `requirements.txt` file can be generated by running the following command:

```shell
pip3 freeze > requirements.txt
```

## Running Development Server

The development server can be started by running the following command from the project's root directory. The command
starts a server on the port `8000` by default.

```shell
python manage.py startserver
```

## License

This project is licensed under the Apache 2 license.

[django]: https://docs.djangoproject.com/en/3.1/topics/install/
[run-mysql]: hack/run-mysql.sh
[mysqlclient]: https://pypi.org/project/mysqlclient/
[requirements]: ./requirements.txt
