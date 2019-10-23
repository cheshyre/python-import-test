# python-import-test

This exists to test some problems I am having with Python imports.

Executing the command

```sh
python3 -m package
```

gives the following error:

```
Traceback (most recent call last):
  File "/usr/lib/python3.6/runpy.py", line 183, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/usr/lib/python3.6/runpy.py", line 142, in _get_module_details
    return _get_module_details(pkg_main_name, error)
  File "/usr/lib/python3.6/runpy.py", line 109, in _get_module_details
    __import__(pkg_name)
  File "/home/mheinz/Documents/workspace/python-import-test/package/__init__.py", line 5, in <module>
    from package import subpackageA
  File "/home/mheinz/Documents/workspace/python-import-test/package/subpackageA/__init__.py", line 6, in <module>
    from package.subpackageA import moduleA
  File "/home/mheinz/Documents/workspace/python-import-test/package/subpackageA/moduleA.py", line 5, in <module>
    import package.subpackageA.moduleB as mB
AttributeError: module 'package' has no attribute 'subpackageA'
```


The problem seems to lie in using `import` for absolute imports between modules in the repository
instead of `from-import`, which is what is used in `package2`.
This package imports without problems:

```sh
python3 -m package2
```

yielding:

```
/usr/bin/python3: No module named package2.__main__; 'package2' is a package and cannot be directly executed
```

The only difference is that imports of the form

```python3
import package.subpackageA.moduleB as mB
```

were changed to

```python3
from package.subpackageA import moduleB as mB
```

These should intuitively be doing the same thing,
that is importing `package` and then aliasing `package.subpackageA.moduleB` to `mB` in the namespace.
Clearly, in this case, something quite different is happening, so there must be some underlying difference between `import` statements and `from-import` statements.

It is also worth noting that the flatter structure of `package3` means that the standard `import` approach (as opposed to `from-import`) works fine:

```sh
python3 -m package3
```

yielding

```
/usr/bin/python3: No module named package3.__main__; 'package3' is a package and cannot be directly executed
```
