#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Tests the Bowling Scoring Engine python script.

Author:
Alexander Schultz
alexhschultz@gmail.com
"""

import bowlingscoringengine

_test_cases = [
        # [score, raw score input]
        [0,   '-- -- -- -- -- -- -- -- -- --'],
        [20,  '11 11 11 11 11 11 11 11 11 11'],
        [149, '8/ 54 9- X- X- 5/ 53 63 9/ 9/X'],
        [6,   '11 11 11'],
        [12,  '11 64'],
        [85,  'X- X- X- 55'],
        [47,  '11 11 11 11 11 11 11 11 11 X- X- 9'],
        [173, '73 73 73 73 73 73 73 73 73 73 X-'],
        [300, 'X- X- X- X- X- X- X- X- X- X- X- X- X-'],
        [240, 'X- X- X- -- X- X- X- X- X- X- X- X-'],
        [245, 'X- X- X- X- X- X- X- X- X- 11']]

def run_tests():
    """run test cases and show results
    """
    for test in _test_cases:
        expected = test[0]
        raw_input = test[1]
        parsed_input = bowlingscoringengine.parse_input(raw_input)
        result = bowlingscoringengine.calculate_score(parsed_input)
        print('input: ' + str(raw_input))
        print('result = ' + str(result) + '\texpected = ' + str(expected))
        print('PASS' if result == expected else 'FAIL')
        print()


if __name__ == "__main__":
    run_tests()