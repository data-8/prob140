test = {
'name': "Question",
'points': 1,
'suites': [
{
'cases': [

{
'code': r"""
>>> round(match2_marginal.prob_event(3) - 1/365**2, 6) == 0
True
>>> match2_marginal.prob_event(2) == 0
True
>>> round(sum(match2_marginal.column(1)), 6) == 1
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
