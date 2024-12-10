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


def test_should_raise_error_when_resulting_cable_lengths_would_be_less_than_one():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(2, "coconuts"), 3)


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

def test_should_split_remainder_into_initial_split_length_if_possible():
    cables = Splitter().split(Cable(12, "coconuts"), 10)

    assert_that(len(cables)).is_equal_to(12)
    assert_that(cables[0].length).is_equal_to(1)
    assert_that(cables[-1].length).is_equal_to(1)

# Test returned Cable names are formatted to requirements
def test_returned_cable_names_have_single_digit_suffix_when_less_than_ten():
    input_name = "coconuts"
    cables = Splitter().split(Cable(5, input_name), 2)

    assert_that(cables[0].name).is_equal_to(input_name + "-0")
    assert_that(cables[-1].name).is_equal_to(input_name + "-4")

def test_returned_cable_names_have_double_digit_suffix_when_between_ten_and_one_hundred():
    input_name = "bananas"
    cables = Splitter().split(Cable(12, input_name), 10)

    assert_that(cables[0].name).is_equal_to(input_name + "-00")
    assert_that(cables[-1].name).is_equal_to(input_name + "-11")
