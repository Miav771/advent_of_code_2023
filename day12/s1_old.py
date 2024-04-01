# Not feeling good about this one at all
# Stumbled a ton, had to look up hints for this one
# Here's some of my random code in my attempt for p1
# For p2, I didn't expect caching could be nearly this impactful
# So again, had to see a hint to try it

from math import comb
from collections import Counter

file = open("input.txt")


def filter_completed_records(records, lengths):
    length_counter = Counter(lengths)
    complete_records = Counter([len(record) for record in records if "?" not in record])
    for complete_record_length, occurences in complete_records.most_common():
        if length_counter[complete_record_length] == occurences:
            lengths = [length for length in lengths if length != complete_record_length]
            records = [
                record
                for record in records
                if "?" in record or len(record) != complete_record_length
            ]
    return records, lengths


def filter_invalid_optionals(records, lengths):
    min_valid_size = min(lengths)
    records = [
        record for record in records if "#" in record or len(record) >= min_valid_size
    ]
    return records, lengths


def optional_only_segment_combinations(segment, lengths):
    n = len(segment) - sum(lengths) + 1
    if n < 1:
        return 0
    return comb(n, len(lengths))


def single_length_segment_combinations(segment, length):
    start = min(position for position, spring in enumerate(segment) if spring == "#")
    end = max(position for position, spring in enumerate(segment) if spring == "#")
    wiggle_room = length - end + start - 1
    room_left = min(wiggle_room, start)
    room_right = min(wiggle_room, len(segment) - 1 - end)
    arrangaments = max(1 + room_left + room_right - wiggle_room, 0)
    return arrangaments


def fits(segment_length, lengths):
    idx = 0
    while segment_length and idx < len(lengths):
        if lengths[idx] <= segment_length:
            segment_length -= lengths[idx] + 1
            idx += 1
        else:
            break
    return idx


def multiple_length_segment_combinations(segment, lengths):
    if "#" not in segment:
        return optional_only_segment_combinations(segment, lengths)
    length = lengths[0]
    if len(lengths) == 1:
        return single_length_segment_combinations(segment, length)
    arrangements = 0
    for start in range(len(segment) - sum(lengths) - len(lengths) + 2):
        if "#" not in segment[:start] and segment[start + length] != "#":
            arrangements += multiple_length_segment_combinations(
                segment[start + length + 1 :], lengths[1:]
            )
    return arrangements


def multiple_segment_combinations(segments, lengths):
    if not lengths:
        return 0
    if len(segments) == 1:
        return multiple_length_segment_combinations(segments[0], lengths)

    arrangements = 0
    segment = segments[0]
    fits_count = fits(len(segment), lengths)
    if "#" not in segment:
        arrangements += multiple_segment_combinations(segments[1:], lengths)
    for cutoff in range(1, fits_count + 1):
        current_segment_arrangements = multiple_length_segment_combinations(
            segment, lengths[:cutoff]
        )
        other_segments_arrangements = multiple_segment_combinations(
            segments[1:], lengths[cutoff:]
        )
        arrangements += current_segment_arrangements * other_segments_arrangements
    return arrangements


arrangements = []
for line in file:
    records, lengths = line.strip().split()
    lengths = [int(length) for length in lengths.split(",")]
    records = records.strip(".")
    records = [record for record in records.split(".") if record]
    records, lengths = filter_completed_records(records, lengths)
    records, lengths = filter_invalid_optionals(records, lengths)
    arrangements.append(multiple_segment_combinations(records, lengths))
print(sum(arrangements))
