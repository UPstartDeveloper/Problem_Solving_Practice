class Solution:
    """
    Source: InterviewQs Email Newsletter
    
    Given a time string that is in the following 12-hour format (hh:mm), determine the angle between the hour and the minute hands on an analog clock. An example input and output is shown below:

    Input: 12:45
    Output: 112.5 (aka, the "smaller" angle)

    Intuition:
        for loop traversal

    EC
        hr or min is not in range [1, 12], or [0, 59] inclusive --> ValueError
    
    """

    CP = CLOCK_POSITIONS = [degree for degree in range(0, 360, 30)]

    def compute_angle_between_hour_and_min(self, time: str) -> float:
        ### HELPERS:
        def _compute_angle(start, end):
            """TODO: for loop"""
            # A: start angle - convert to degree using the array
            start_int = int(start)  # truncate the fractional part
            start_index = start_int % len(self.CP)
            start_degrees = self.CP[start_index] + ((start - start_int) * 30)
            # B: end angle - convert to degree -->
            end_int = int(end)  # truncates the fraction
            target_index = end_int % len(self.CP)
            # start + "walking clockwise"
            hours_in_between, cur_index = 0, start_index
            while cur_index != target_index:
                cur_index += 1
                cur_index = cur_index % len(self.CP)
            end_degrees = start_degrees + (30 * ((end - end_int) + hours_in_between))
            # C: return diff
            return end_degrees - start_degrees

        def _convert(hr, minute):
            """TODO[refactor-remove_numbers]"""
            # minute: divide by 5
            hr_pos_min = float(minute) / 5
            # hr = hr + min / 60
            hr_pos_hr = hr + float(minute) / 60

            return hr_pos_hr, hr_pos_min

        ### EC: handle-invalid inputs
        if not isinstance(time, str) or ":" not in list(time):
            raise ValueError(
                f"Expected a time string in hh:mm format, actual is {time}."
            )

        hour_min = time.split(":")
        hr, minute = int(hour_min[0]), int(hour_min[1])

        if not 0 < hr < 13 or not isinstance(hr, int):
            raise ValueError(f"Expected an int hour in 12-hr time, actual is {hr}.")
        if not -1 < minute < 60 or not isinstance(minute, int):
            raise ValueError(
                f"Arg for minute = {minute} is not an int or outside of allowed range of 0-59."
            )

        ### DRIVER
        # A: place both hands
        hr_pos_hr, hr_pos_min = _convert(hr, minute)
        # B: compute the angle
        diff1 = (_compute_angle(hr_pos_hr, hr_pos_min),)
        # C: return the angle
        return min(diff1, 360 - diff1)
