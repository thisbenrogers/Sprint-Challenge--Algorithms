class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def pickup_item(self):
        self._item = self._position

    def holding(self):
        return self._item

    def length(self):
        return len(self._list)

    def left_child(self, root_index):
        return (2 * root_index) + 1

    def right_child(self, root_index):
        return (2 * root_index) + 2

    def heapify(self, arr, heap_size, root_index):

        # ! Breaks rule
        largest = root_index

        if self.left_child(root_index) < heap_size and arr[self.left_child(root_index)] > arr[largest]:
            largest = self.left_child(root_index)
        if self.right_child(root_index) < heap_size and arr[self.right_child(root_index)] > arr[largest]:
            largest = self.right_child(root_index)
        if largest != root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            self.heapify(arr, heap_size, largest)


    def heap_sort(self, arr):
        for i in range(self.length(), -1, -1):
            self.heapify(arr, self.length(), i)
        for i in range(self.length() - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


    def sort(self):
        """
        Sort the robot's list.
        """
        return self.heap_sort(self._list)
        """ 

        *
        *   Initially, I felt like this needed a merge sort,
        *   it really felt like the way to do this efficiently
        *
        *   The 'light' boolean made me think of the terrible bubble sort,
        *   which I implemented briefly to no avail
        *
        *   I also implemented a merge-in-place that also took way too long
        *
        *   I am currently implementing heap sort that's based mostly on helper functions
        * 
        *   I am not sure about how these rules are supposed to work together:
        *       You may NOT store any variables. (=)
        *       You may NOT access any instance variables directly. (self._anything)
        *       You may define robot helper methods, as long as they follow all the rules.
        *

        """



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)