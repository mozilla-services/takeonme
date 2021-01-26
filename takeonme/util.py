from typing import Any, Dict, Generator, Iterable


def sorted_unique_by_key(
    records: Iterable[Dict[str, Any]], key_field: str
) -> Generator[str, None, None]:
    """
    From an iterable of dicts, get non-None values from key_field, then sort and yield unique entries:

    >>> list(sorted_unique_by_key([{"Name": "foo.example.com"},{"Name": "bar.example.com"}, {}, {"Name": "bar.example.com"}, {"Name": None}], key_field="Name"))
    ['bar.example.com', 'foo.example.com']

    """
    record_names = [record.get(key_field, None) for record in records if record]
    yield from sorted(set(record_names) - {None})
