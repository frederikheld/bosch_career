# bosch_career apt package

This is an educational apt package about the security implications of using install commands for marketing purposes without owning the corresponding package.

You can install it via `$ sudo apt install bosch_career` as you were instructed in some shady Insta ad by a self-proclaimed software company.

This project is also an artistic approach to spark the discussion about what "being a software company" actually means. It's certainly not about posting fancy Insta ads. But what is it then?

## Install Dev Tools

```sh
$ sudo apt-get install python3-stdeb dh-python
```

## Create Debian Package

```sh
$ python3 setup.py --command-packages=stdeb.command bdist_deb
```

## Install Debian Package

```sh
$ sudo dpkg -i deb_dist/python3-bosch-career_1.0.0-1_all.deb
```