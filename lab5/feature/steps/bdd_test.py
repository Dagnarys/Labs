from unique import Unique
from pytest_bdd import scenario, given, when, then
import ast
from behave import *


####################


@given('some data {LIST}')
def data(context, LIST):
    context.LIST = list(ast.literal_eval(LIST))
    print(LIST)


@when('data is getting unique and there is case {CASE}')
def unique_data(context, CASE):
    if CASE == 'True':
        uniq_list = list(Unique(context.LIST, ignore_case= True))
    if CASE == 'False':
        uniq_list = list(Unique(context.LIST))
    context.res = uniq_list


@then('data is unique {RESULT}')
def res_data(context, RESULT):
    assert list(context.res) == ast.literal_eval(RESULT)
    print(context.res)

###################


# @given('some data with letters', target_fixture='data')
# def data():
#     return ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
#
#
# @when('data is getting unique', target_fixture='unique_data')
# def unique_data(data):
#     return list(Unique(data))
#
#
# @then('data is unique')
# def res_data(unique_data):
#     assert unique_data == ['a', 'A', 'b', 'B']
#
#
# ####################
# @scenario('asd.feature', 'Getting list of unique letters with lower case')
# def testing_unique():
#     pass
#
#
# @given('some data with letters', target_fixture='data')
# def data():
#     return ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
#
#
# @when('data is getting unique', target_fixture='unique_data')
# def unique_data(data):
#     return list(Unique(data, ignore_case=True))
#
#
# @then('data is unique')
# def res_data(unique_data):
#     assert unique_data == ['a', 'b']
