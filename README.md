# bosch_career apt package

This is an educational `apt` package about the security implications of using fancy dev lingo for marketing purposes without understanding what it means. In this specific case: using the command `apt install bosch_career` without owning the corresponding package.

It wouldn't be too hard to get a package with this name into some of the official apt repos of the various Linux distributions.

Even the Debian community, which has a notoriously strict policy about which packages get into their official repo, does not care if the package delivers the value that some HR department promised in their Insta ads. Why should they? They only care if the package provides _any_ value to the users. The package could serve the exact opposite purpose of what the Insta ad promised and the responsible HR department would happily promote it, ridiculing the whole company without even knowing about it.

The adverse effect could be even worse if the review mechanism of one of those repos does not effectively stop malicious packages from being published.

This project is also an artistic approach to spark the discussion about what "being a software company" actually means. It's certainly not about using fancy dev lingo in Insta ads. But what is it then?

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
$ sudo dpkg -i deb_dist/python3-bosch-career_1.0.1-1_all.deb
```

## Contribution

If you want to help making the point, try to get this package into the official apt repos of as many Linux distributions as possible ;-)

Also: if the HR or marketing people of your company use dev lingo without understanding what it means, please educate them about the possible implications.
