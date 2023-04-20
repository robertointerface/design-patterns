"""We already saw how fixtures can help us on isolating the tests so the tests
only have code that is testing a specific functionality. Fixtures can help
us on avoiding repetitive code, but apart from building our own fixtures, pytest
gives us a lot of fixtures ready to use that are very useful, these are builtin
fixtures. If you type "pytest --fixtures" you can see a list of the builtin
fixtures that pytest gives you, for free."""



# the tmp_path or tmp_path_factory, these fixtures are used to create temporary
# directories that you might need to test functions that create files or that
# need dummy files for testing.

# tmp_path will return a pathlib.Path instance that points to a temporary
# directory that sticks around during your test and a bit longer just in case
# you want to inspect them later


import subprocess


def test_tmp_path(tmp_path):
    file = tmp_path / 'file.txt'
    # if you print the path you can see it is something like below
    # tmp/pytest-of-roberto-pupil/pytest-1/test_tmp_path0
    # you can see they are kept at the tmp directory
    print(f'temporary path {tmp_path.absolute()}')
    file.write_text("hello")
    assert file.read_text() == "hello"


# tmp_path_factory fixtures returns you an instance that has a method called
# mktemp(directory_name) that you can use to create temporary directory, in case
# you want to create multiple directories on your tests and have control over
# their names


def test_tmp_path_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp("darkroom-sub")
    file = path / 'file.txt'
    # this will be something like this /tmp/pytest-of-roberto-pupil/pytest-3/darkroom-sub0/file.txt
    print(f'file path {file.absolute()}')
    file.write_text("hello")
    assert file.read_text() == "hello"


# tmp_path_factory is session scope and tmp_path is function scope


"""Another useful builtin fixture is capsys which is useful for stdout or 
stderr, basically some tests are testing that specific output is printed
on the terminal, capsys helps us to do that."""


def print_dummy_statement_terminal():
    process = subprocess.run(["echo", "POKEMON"], capture_output=True)
    return process

# to get and compare/use what is displayed on the terminal we need to do a lot
# of program gymnastics as the example below
def test_dummy_print():
    process = print_dummy_statement_terminal()
    # need to remove the backspaces
    output = process.stdout.rstrip()
    # output is on bytes need to decode it
    assert output.decode("utf-8") == "POKEMON"

#with capsys is simple to extract terminals output
def test_dummy_print_with_capsys(capsys):
    print(f'faking printing')
    output = capsys.readouterr().out.rstrip()
    assert output == "faking printing"

"""There are other fixtures related to capsys, these are capsysbinary for
binary, or caplog wich is specialise on logs"""


"""There is a fixture for mocking, 'monkeypatch' which is for mocking but 
In my experience is much better to use the package python-mocking which is 
wrapper on unittest mocking, unittest is much much better for mocking that pytest
but with that extra package we get the best of both worlds."""


"""There are more builtin useful fixtures like 'cache' to cache data from
test to test, see those on documentation"""
