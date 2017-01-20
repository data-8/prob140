test = {
'name': "Question",
'points': 1,
'suites': [
{
'cases': [

{
'code': r"""
>>> round(p_m1_2 - 1/N, 6) == 0
True
>>> correct_p_m1_3 = ((N-1)/N)*(2/N)
>>> round(p_m1_3 - correct_p_m1_3, 6) == 0
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
