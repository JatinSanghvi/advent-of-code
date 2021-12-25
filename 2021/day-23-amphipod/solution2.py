def dist(room_index, pos, space_index):
    if space_index <= room_index + 1:
        return 2 * (room_index - space_index + 2) + pos - (1 if space_index == 0 else 0)
    else:
        return 2 * (space_index - room_index - 1) + pos - (1 if space_index == 6 else 0)


def least_energy(rooms, spaces):

    to_amp = ['A', 'B', 'C', 'D']
    to_room_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    to_energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    least_energy_map = {}

    def next_move(least, room_index, pos, space_index):
        amp1 = rooms[room_index][pos]
        amp2 = spaces[space_index]
        rooms[room_index][pos] = amp2
        spaces[space_index] = amp1
        least = min(least, least_energy() + to_energy[max(amp1, amp2)] * dist(room_index, pos, space_index))
        rooms[room_index][pos] = amp1
        spaces[space_index] = amp2
        return least

    def least_energy():
        key = str((rooms, spaces))

        if (key not in least_energy_map):
            least = 1e6

            if all(rooms[index][0] == rooms[index][1] == rooms[index][2] == rooms[index][3] == to_amp[index] for index in range(4)):
                least = min(least, 0)

            for room_index, room in enumerate(rooms):
                dest_amp = to_amp[room_index]

                if room[0] in ['.', dest_amp] and room[1] in ['.', dest_amp] and room[2] in ['.', dest_amp] and room[3] in ['.', dest_amp]: continue
                elif room[0] != '.': pos = 0
                elif room[1] != '.': pos = 1
                elif room[2] != '.': pos = 2
                else: pos = 3

                src_amp = room[pos]

                for space_index in range(room_index + 1, -1, -1):
                    if spaces[space_index] != '.': break
                    least = next_move(least, room_index, pos, space_index)

                for space_index in range(room_index + 2, 7, 1):
                    if spaces[space_index] != '.': break
                    least = next_move(least, room_index, pos, space_index)

            for space_index in range(7):
                if spaces[space_index] != '.':
                    src_amp = spaces[space_index]
                    room_index = to_room_index[src_amp]

                    if rooms[room_index][3] == '.': pos = 3
                    elif rooms[room_index][3] != src_amp: continue
                    elif rooms[room_index][2] == '.': pos = 2
                    elif rooms[room_index][2] != src_amp: continue
                    elif rooms[room_index][1] == '.': pos = 1
                    elif rooms[room_index][1] != src_amp: continue
                    elif rooms[room_index][0] == '.': pos = 0
                    else: continue

                    if space_index <= room_index + 1 and all(spaces[index] == '.' for index in range(space_index + 1, room_index + 2, 1)):
                        least = next_move(least, room_index, pos, space_index)

                    if space_index > room_index + 1 and all(spaces[index] == '.' for index in range(room_index + 2, space_index, 1)):
                        least = next_move(least, room_index, pos, space_index)

            least_energy_map[key] = least

        return least_energy_map[key]

    return least_energy()


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    rooms = [
        [lines[2][3], 'D', 'D', lines[3][3]],
        [lines[2][5], 'C', 'B', lines[3][5]],
        [lines[2][7], 'B', 'A', lines[3][7]],
        [lines[2][9], 'A', 'C', lines[3][9]],
    ]

    spaces = ['.'] * 7

    print(least_energy(rooms, spaces))


solve('input-test.txt')
solve('input.txt')
