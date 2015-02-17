from nose.tools import assert_equals

from parse_web_content import parse_content

class TestParseWebContent:
    def test_true_if_has_keyword(self):
        assert_equals(parse_content(['red'], 'got red'), True)
    def test_false_if_doesnt_have_keyword(self):
        assert_equals(parse_content(['red'], 'got blue'), False)
    def test_multiple_keywords(self):
        assert_equals(parse_content(['red','yellow'], 'got yellow'), True)
    def test_missing_keyword(self):
        assert_equals(parse_content([], 'got nuffin'), False)