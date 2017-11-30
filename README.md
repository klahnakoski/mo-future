# mo-future

More future!  Make Python 2/3 compatibility a little bit easier

## Details

All the data types that have changed, and all the libraries that have moved, are put into the `mo-future` top-level module so it is easy to find.

**This module is only intended for the `mo-*` series of libraries, but pull requests are welcome**


### Replaces `future` or `six`

Many of the compatibility types declared by `future` or `six` are in `mo-future`


### Flat namespace

All compatibility types are top-level

Instead of 

```python
	from future.utils import text_type
```

you get the same, but without having to discover what sub-module the `text_type` is hiding:  

```python
	from mo_future import text_type
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


