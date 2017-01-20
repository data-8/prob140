test = {
'name': "Question",
'points': 1,
'suites': [
{
'cases': [

{
'code': r"""
>>> round(joint_func(2, 4) - (365/365) * (1/365) * (364/365) * (2/365), 6) == 0
True
>>> joint_func(2, 3) != 0
True
>>> joint_func(10, 10) == 0
True
>>> joint_func(1, 2) == 0
True
>>> round(joint_func(10, 11) - 0.0005504632723210921, 6) == 0
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
