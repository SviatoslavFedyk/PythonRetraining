import functions.string_operations as task_func
from helper.custom_exceptions import *
import tests.unit.data.links_data as links
import pytest
import requests


@pytest.mark.parametrize("str, n, expected_result", [("123456987654", 6, "234561876549"),
                                                     ("123456987653", 6, "234561356789"),
                                                     ("66443875", 4,"44668753"),
                                                     ("66443875", 8, "64438756"),
                                                     ("664438769", 8, "67834466"),
                                                     ("123456779", 8, "23456771"),
                                                     ("563000655734469485", 4, "0365065073456944")])
def test_transforming_string(str, n, expected_result):
    assert task_func.transform_string(str, n) == expected_result

@pytest.mark.parametrize("str, n, expected_result", [("", 8, NonPositiveIntegerException),
                                                     ("432184876", -36, StringBufferOverflowException),
                                                     ("432184876", 0, StringBufferOverflowException)])
def negative_test_transforming_string(str,n,expected_result):
    with pytest.raises(expected_result) as e_info:
        task_func.transform_string(str, n)

@pytest.mark.parametrize("url, expected_result", [("https://en.wikipedia.org/wiki/Hideo_Ogata", links.hideo_ogata_wiki_links),("https://docs.python.org/3/", links.python_links)])
def test_extract_links_from_html(url,expected_result):
    response = requests.get(url)
    html = response.text
    assert task_func.extract_links_from_html(html) == expected_result
