# linqp
Simple LINQ implementation for python.

### Usage example:
```python
Linqp(foo).where(lambda x: x.bar == 'bar').select_all()
```

or

```python
Linqp(foo).where(lambda x: x.bar == 'bar').select(lambda x: x.foobar)
```