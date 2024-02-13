# `pype-rename`

A renaming utility that acts on pipes.

`pype-rename` is a replacement for `pipe-rename`, written in **Py**thon!

Inspired by [`pipe-rename`][pipe-rename] and made out of frustration trying to
get it to work without it breaking the
terminal[^pipe-rename54]<sup>,</sup>[^pipe-rename46].


# Usage

For now, add `pype-rename.py` to your path.

```
cd ~/.local/bin
curl -LO https://raw.githubusercontent.com/yyolk/pype-rename/main/pype-rename.py pype-rename
chmod +x pype-rename
```

Pipe in files that you'd like to be renamed (they're recognized as paths).

```
ls | pype-rename
```

Edit the list of files to the desired destination name, save the buffer and
close the editor.


# Planned
- published to pypi, installable
- feature parity with [`pipe-rename`][pipe-rename], e.g., work on globs or
  stdin
- brew formula
- xplr script


[^pipe-rename54]: https://github.com/marcusbuffett/pipe-rename/issues/54
[^pipe-rename46]: https://github.com/marcusbuffett/pipe-rename/issues/46

[pipe-rename]: https://github.com/marcusbuffett/pipe-rename
