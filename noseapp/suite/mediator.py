# -*- coding: utf-8 -*-


class TestCaseMediator(object):
    """
    Mediator class between noseapp.suite.Suite, TestLoader, TestSuite,
    TestCase. Provides between TestCase->TestLoader->TestSuite.
    """

    def __init__(self, require):
        self._test_cases = []
        self._require = require

    @property
    def test_cases(self):
        return self._test_cases

    def create_map(self):
        """
        {
            'class name': {
                'cls': 'link to class object',
                'tests': {
                    'method name': 'link to class method',
                },
            },
        }

        :return: dict
        """
        mp = {}

        for case in self._test_cases:
            mp[case.__name__] = {
                'cls': case,
                'tests': dict(
                    (atr, getattr(case, atr))
                    for atr in dir(case)
                    if atr.startswith('test')
                    or
                    atr.startswith('runTest'),
                ),
            }

        return mp

    def create_suite(self, nose_config, test_loader, class_factory):
        """
        Create suite instance
        """
        suite = class_factory.suite_class(config=nose_config)

        for case in self._test_cases:
            suite.addTests(
                test_loader.loadTestsFromTestCase(
                    case.with_require(self._require),
                ),
            )

        return suite

    def add_test_case(self, test_case):
        self._test_cases.append(test_case)
