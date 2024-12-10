from assertpy import assert_that

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()

# Input sanity checks
def test_should_raise_error_none_provided_for_times():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), None)


def test_should_raise_error_when_float_provided_for_times():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 15.5)


def test_should_raise_error_when_string_provided_for_times():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), "2")


def test_should_raise_error_when_cable_object_not_provided():
    assert_that(Splitter().split).raises(ValueError).when_called_with("coconuts", 2)


# Input range validation
def test_should_raise_error_when_negative_provided_for_times():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), -2)


def test_should_raise_error_when_zero_provided_for_times():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 0)


def test_should_raise_error_when_times_is_greater_than_maximum():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 65)


def test_should_raise_error_when_provided_cable_has_length_less_than_two():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(1, "coconuts"), 1)


def test_should_raise_error_when_provided_cable_has_length_greater_than_maximum():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(2048, "coconuts"), 1)
