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


# Test resulting array of cables for count and cable length
def test_should_split_cable_length_of_ten_to_two_cables_of_five():
    cables = Splitter().split(Cable(10, "coconuts"), 1)

    assert_that(len(cables)).is_equal_to(2)
    assert_that(cables[0].length).is_equal_to(5)
    assert_that(cables[1].length).is_equal_to(5)


def test_should_split_cable_length_of_five_two_times_to_five_cables_with_length_of_one():
    cables = Splitter().split(Cable(5, "coconuts"), 2)

    assert_that(len(cables)).is_equal_to(5)
    assert_that(cables[0].length).is_equal_to(1)
    assert_that(cables[-1].length).is_equal_to(1)


def test_should_split_cable_legth_of_ten_three_times_to_five_cables_with_length_of_two():
    cables = Splitter().split(Cable(10, "coconuts"), 3)

    assert_that(len(cables)).is_equal_to(5)
    assert_that(cables[0].length).is_equal_to(2)
    assert_that(cables[-1].length).is_equal_to(2)

# Test remainder Cable length
# TODO Double check required functionality
def test_should_split_cable_legth_of_ten_two_times_to_four_cables_including_remainder():
    cables = Splitter().split(Cable(10, "coconuts"), 2)

    assert_that(len(cables)).is_equal_to(4)
    assert_that(cables[0].length).is_equal_to(3)
    assert_that(cables[-1].length).is_equal_to(1)

def test_should_split_cable_of_seventy_three_times_to_five_cables_including_remainder():
    cables = Splitter().split(Cable(70, "coconuts"), 3)

    assert_that(len(cables)).is_equal_to(5)
    assert_that(cables[0].length).is_equal_to(17)
    assert_that(cables[-1].length).is_equal_to(2)
