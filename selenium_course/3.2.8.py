def test_substring(full_string, substring):
    try:
        assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
    except AssertionError as e:
        print(e)

test_substring('fulltext', 'some_value')
test_substring('1', '1')
test_substring('some_text', 'some')