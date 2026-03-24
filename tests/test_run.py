from src.yatl.run import Runner
from src.yatl.extractor import DataExtractor
from src.yatl.render import TemplateRenderer
from src.yatl.utils import create_context


def test_create_context_with_valid_data_returns_context():
    data = {
        "base_url": "https://yandex.ru",
        "name": "ping",
        "steps": [
            {
                "expect": {"status": 200},
                "name": "ok_test",
                "request": {"method": "GET"},
            },
            {
                "expect": {"status": 404},
                "name": "not_found_test",
                "request": {"method": "GET", "url": "/not_found"},
            },
        ],
    }
    context = create_context(data)
    assert context is not None
    assert context["base_url"] == "https://yandex.ru"
    assert context["name"] == "ping"


def test_create_context_with_empty_data_returns_empty_context():
    context = create_context({})
    assert len(context) == 0


def test_is_skipped_test_returns_true_if_test_is_skipped():
    data = {"skip": True}
    runner = Runner(DataExtractor(), TemplateRenderer())
    context = create_context(data)
    assert runner._is_skipped_test(context) is True


def test_is_skipped_test_returns_false_if_test_is_not_skipped():
    data = {"skip": False}
    runner = Runner(DataExtractor(), TemplateRenderer())
    context = create_context(data)
    assert runner._is_skipped_test(context) is False
