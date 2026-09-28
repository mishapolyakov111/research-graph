import logging

from research_graph.logging_setup import setup_logging


def test_setup_logging_does_not_duplicate_handlers() -> None:
    setup_logging("DEBUG")
    setup_logging("DEBUG")
    root = logging.getLogger()
    assert len(root.handlers) == 1
    assert root.level == logging.DEBUG
