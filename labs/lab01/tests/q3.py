test = {
'name': "Question",
'points': 1,
'suites': [
{
'cases': [

{
'code': r"""
>>> len(m1_values) == 365
True
>>> correct_answer = np.arange(2, N+2)
>>> np.array_equal(correct_answer, m1_values)
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
