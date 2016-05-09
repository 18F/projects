### 18F Projects

**Work in progress!!!**

#### Dependencies

- Python 3.5.0
- [Postgresql](http://www.postgresql.org/download/)

#### Running Locally

```sh
$ virtualenv -p python3.5 venv
$ source venv/bin/activate
$ pip install -r requirements.txt

$ createdb 18fprojects

$ python manage.py migrate
$ python manage.py runserver
```

#### Public domain

This project is in the worldwide [public domain](LICENSE.md).   As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within   the United States, and copyright and related rights in the work worldwide are waived through   the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).  
>
> All contributions to this project will be released under the CC0 dedication. By submitting a   pull request, you are agreeing to comply with this waiver of copyright interest.
