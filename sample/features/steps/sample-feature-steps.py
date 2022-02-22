from behave import given, then, when


@given("we have behave installed")
def given_impl(context):
    pass


@when("we implement a test")
def when_impl(context):
    assert True is not False


@then("behave will test it for us!")
def then_impl(context):
    assert context.failed is False
