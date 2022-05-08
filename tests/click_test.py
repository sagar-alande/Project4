"click test"

import os

from click.testing import CliRunner

from app import create_database

runner = CliRunner()

def test_create_database():
    """This makes the click test"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
