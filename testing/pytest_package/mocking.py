"""
mocking is an essential part of testing but is quite difficult to get it right.
Problems that arise with mocking.
1 - multiple people write the same mock objects, waist of time and resources,
if multiple people are working on the same repo then the mocks should all go
on the same module/file, then if someone needs to write a mock it should first
lock into that mocking module to see if is there.
2 - mock tells you what you want to hear. i.e we are mocking an amazing
function that Mark wrote on some package that is on codeartifact, it all goes
well because we wrote the mock, the problem is that the amazing function that
mark wrote is broken in the last version, we don't catch it on our testing
and BOOM the universe explodes.
3 - over mocking, you don't need to mock a dataclass that is just storing
data.

If you are interested there is a pycon talk about this topic

https://nedbatchelder.com/blog/201206/tldw_stop_mocking_start_testing.html

with pytest you can use the unittest.mock module or install the pytest-mock
package which is a wrapper over the unittest.mock at the end.


When you are mocking you have to ask yourself the following questions.
1 - Is it really necessary to mock this?
2 - Has this been mocked before?


1 - Am I mocking the correct object, function, module, method...? this can
be a major problem and something to consider specially if you are using 'patch'
is not important just to mock/patch but also where to patch.
2 - Is the mocking of that object the required mocking?


Typical mocking examples:
1 - Databases.
2 - http requests.
3 - communication with aws services like S3.
4 - very computational intensive calculations that you are not testing but just
need their result.

All the examples above can make your tests fail if for example the website
you request some data through their API is broken at the moment but that is
not fault of your code, is an external component you are using. BUT like I said
before this raises the problem of 'mocking tells you what you want to hear'
lets say that the website you request this data is broken forever, your test
will not catch this and your application will eventually fail, this should be
caught when you do end to end testing, so Mocking should be done sometimes, not
always.
"""
# First thing is am I mocking the correct object, is not important that you mock
# the function or object but that is mocked from the right path, this problem
# comes from the nature that Python uses pointers/references to objects, this
# is best explained on the following links, please read them because they
# can solve you a lot of pain.
# https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
# https://docs.python.org/3/library/unittest.mock.html#where-to-patch


# an example of mocking can be found on multiple occasions on the example application
# I wrote (online_shopping) specially at module online_shopping.tests.test_place_order.py

# Mocking can be used for more than just faking data or http response, mocking
# can be used also to Spy on functions/methods and assert they are being called
# with the right arguments, an example of this can be seen on
# online_shopping.tests.test_place_order.test_request_post_has_correct_payload_when_called_on_make_payment


# There is a very intensive literature on mocking easy accessible by anyone.
