from coding_exercise.domain.model.cable import Cable


class Splitter:

    INPUT_CABLE_LENGTH_MIN = 2
    INPUT_CABLE_LENGTH_MAX = 1024
    TIMES_MIN = 1
    TIMES_MAX = 64

    def __validate(self):
        self.__validate_times_input()
        self.__validate_cable_input()

        # Check resulting cable length will not be less than one
        if self.input_cable.length // self.times == 0:
            raise ValueError

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.times = times
        self.input_cable = cable
        self.__validate()

        return []

    def __validate_times_input(self):
        # Check self.times value is an integer in range
        if (not isinstance(self.times, int)
            or self.times < self.TIMES_MIN
            or self.times > self.TIMES_MAX):

            raise ValueError

    def __validate_cable_input(self):
        # Check input Cable valid and length is in range
        if (not isinstance(self.input_cable, Cable)
            or self.input_cable.length < self.INPUT_CABLE_LENGTH_MIN
            or self.input_cable.length > self.INPUT_CABLE_LENGTH_MAX):

            raise ValueError
