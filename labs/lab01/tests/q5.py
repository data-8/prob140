test = {
'name': "Question",
'points': 1,
'suites': [
{
'cases': [

{
'code': r"""
>>> round(sum(first_match), 6) == 1
True
>>> round(first_match[0] - 1/N, 6) == 0
True
>>> round(first_match[1] - ((N-1)/N)*(2/N), 6) == 0
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
