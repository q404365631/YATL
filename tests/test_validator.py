from src.yatl.validator import BodyFormat


def test_from_content_type_json():
    assert BodyFormat.from_content_type("application/json") == BodyFormat.JSON


def test_from_content_type_xml():
    assert BodyFormat.from_content_type("application/xml") == BodyFormat.XML


def test_from_content_type_text():
    assert BodyFormat.from_content_type("text/plain") == BodyFormat.TEXT
