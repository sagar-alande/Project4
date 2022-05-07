"""This test the aboutpage"""


def test_fpatpage(client):
    """This makes the index page"""
    response = client.get("/")
    assert b'Index' in response.data
