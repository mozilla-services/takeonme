from typing import Any, Dict, Generator, Iterable


def records_to_sorted_unique_domains(
    records: Iterable[Dict[str, Any]], name_field: str
) -> Generator[str, None, None]:
    """
    From an iterable of DNS record dicts, look up name_field to find domain names, then sort and yield unique DNS names

    >>> list(records_to_sorted_unique_domains([{"Name": "foo.example.com"},{"Name": "bar.example.com"}, {}, {"Name": "bar.example.com"}], name_field="Name"))
    ['bar.example.com', 'foo.example.com']
    """
    record_names = [
        record.get("Name", None)
        for record in records
        if record and record.get("Name", None)
    ]
    yield from sorted(set(record_names))
