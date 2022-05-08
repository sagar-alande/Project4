"project/tests/test_config.py"

def test_development_config(application):
    """This makes the development cnf"""
    application.config.from_object('app.config.DevelopmentConfig')
    assert application.config['DEBUG']
    assert not application.config['TESTING']
