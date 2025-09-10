# Contributing

First of all, thank you for reading here to contribute! I really appriciate that. <br />

## Share experience
If you want to share your interview experience, use [md generator](https://mo1ein.github.io/jobname/mdgen.html) then download `.md` file. <br />
Create a directory with company name (if not exist) and put your `md` file in it.
Just like this:
```
src/snapp
├── snapp_cab_1.md
└── snapp_cab_2.md
```
Then for compile, you need to add your `md` file path to `SUMMARY.md`.
You can add your name (if you like) after the company name like: `snapp_moein.md` and that's good to write it in the file otherwise, write `unknown`.

## Install
You need to install mdbook. Just install binaries if you are not familiar with `rust` and `cargo`. <br />
Watch this [link](https://github.com/rust-lang/mdBook/releases) for releases. <br />
For mermaid charts, install [this](https://github.com/badboy/mdbook-mermaid).

## Build
For building after your changes in the root dir of project:
```
mdbook build .
```

Or you can build and serve to watch your changes:

```
mdbook serve --open
```
