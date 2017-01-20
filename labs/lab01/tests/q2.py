test = {
'name': "Question",
'points': 1,
'suites': [
{
'cases': [

{
'code': r"""
>>> no_matches(1) == 1
True
>>> no_matches(-1) == 0
True
>>> round(no_matches(2) - (N-1)/N, 6) == 0
True
>>> no_matches(8) == 0
True
>>> no_matches(7) == 0
True
>>> no_matches(6) != 0
True

""",
'hidden': False,
'locked': False
}

],
'scored': True,
'setup': '',
'teardown': '',
'type': 'doctest'
}
]
}
