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

        output_array = []

        # Calculate highest integer equal split lengths and remainder
        self.__determine_split_segment_length_and_count()

        # Padding width for output Cable(s)
        pad_width = len(str(self.total_segments))

        # Loop for self.equal_segments, create Cable of self.equal_length length
        for i in range(self.equal_segments):
            cable_name = self.input_cable.name + "-" + str(i).rjust(pad_width, "0")
            output_array.append(Cable(self.equal_length, cable_name))

        # If self.remainder, append Cable of self.remainder length
        if self.remainder:
            cable_name = self.input_cable.name + "-" + str(self.total_segments - 1).rjust(pad_width, "0")
            output_array.append(Cable(self.remainder, cable_name))

        return output_array

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

    def __determine_split_segment_length_and_count(self):
        # Find highest integer segment length and remainder
        inital_segments = self.times + 1
        split_length, remainder_length = divmod(self.input_cable.length, inital_segments)

        # If remainder, check if we can create extra equal segments
        extra_segments, final_remainder = divmod(remainder_length, split_length)

        # Determine final segment count and equal segment length
        self.equal_length = split_length
        self.equal_segments = inital_segments + extra_segments

        if (final_remainder):
            self.total_segments = self.equal_segments + 1
            self.remainder = final_remainder
        else:
            self.total_segments = self.equal_segments
            self.remainder = 0
