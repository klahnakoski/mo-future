# mo-future

More future!  Make Python 2/3 compatibility a little bit easier

### Problem 

`future` or `six` are hard to use: It is easy to google how to import an object in Python2, or Python3, but finding the full path in these compatibility libraries is difficult. 

## Solution

All the modules and types required for compatibility are put into the `mo-future` top-level module so they are  easy to find.


### Flat namespace

Instead of 

```python
    from future.utils import text
```

you get the same, but without having to discover what sub-module the `text` is hiding:  

```python
    from mo_future import text
```


### Simpler imports

Instead of writing conditional imports like 

```python
    try:
        from io import StringIO
    except:
        from StringIO import StringIO
```

or 

```python
    if PY3:
        from io import StringIO
    else:
        from StringIO import StringIO
```

you can use `mo-future`:

```python
    from mo_future import StringIO
```


