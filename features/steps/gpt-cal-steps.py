from behave import given, when, then
from features.pages.simple_calculator import SimpleCalculator

@given('I have two number {num1} and {num2} into the calculator')
def step_given_have_numbers(context, num1, num2):
    context.num1 = float(num1)
    context.num2 = float(num2)
    context.calculator = SimpleCalculator(context.num1,context.num2)  # Instantiate the Calculator object


@when('I perform {operator}')
def step_when_perform_operation(context, operator):
    if operator == 'addition':
        context.result = context.calculator.addition()
    elif operator == 'subtraction':
        context.result = context.calculator.subtraction()
    elif operator == 'multiplication':
        context.result = context.calculator.multiplication()
    elif operator == 'division':
        context.result = context.calculator.division()

@then('the result should be {expected_result} on the screen')
def step_then_check_result(context, expected_result):
    assert context.result == float(expected_result), f"Expected result to be {expected_result}, but got {context.result}"
