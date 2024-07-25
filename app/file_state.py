"""

This module contains the FileState class.

"""


from __future__ import annotations
import datetime


class FileState:
    """

    File state class

    """

    def __init__(self, status: str = "init"):

        self.status: str = status

        self.date_format: str = "%Y-%m-%d %H:%M:%S"

        self.__init_time: datetime = datetime.datetime.now().strftime(self.date_format)

        self._last_update: str | datetime = self.__init_time
        self._start_time: str | datetime = self.__init_time
        self._end_time: str | datetime = self.__init_time

    def datetime_to_str(self, datetime_str: str) -> str:
        return datetime.datetime.strptime(datetime_str, self.date_format).strftime(self.date_format)

    @property
    def last_update(self) -> str:
        return self._last_update

    @last_update.setter
    def last_update(self, value: str | datetime) -> None:
        self._last_update = self.datetime_to_str(value)

    @property
    def start_time(self) -> str:
        return self._start_time

    @start_time.setter
    def start_time(self, value: str | datetime) -> None:
        self._start_time = self.datetime_to_str(value)

    @property
    def end_time(self) -> str:
        return self._end_time

    @end_time.setter
    def end_time(self, value: str | datetime) -> None:
        self._end_time = self.datetime_to_str(value)

    def __update_last_update(self) -> None:
        """
        Update last update time
        :return: None
        """
        self.last_update = datetime.datetime.now().strftime(self.date_format)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        # update last update time
        self.__update_last_update()
        return setattr(self, key, value)

    def update(self, other: FileState | dict):
        """
        Update file state
        :param other:
        :return:
        """

        for key, value in vars(other).items():
            if key.startswith("_"):
                continue
            # update last update time
            self.__update_last_update()
            setattr(self, key, value)

    def __str__(self):
        return f"FileState({vars(self)})"

    def to_dict(self):
        # return only properties
        return {key: getattr(self, key) for key in dir(self) if not key.startswith("_") and not callable(getattr(self, key))}


if __name__ == "__main__":
    file_state = FileState()
    # another_file_state = FileState(status="another_status")
    # print(file_state)
    # print(file_state["status"])
    # file_state.update(another_file_state)
    # print(file_state["status"])
    print("1", type(file_state.start_time))
    file_state.start_time = datetime.datetime.now().strftime(file_state.date_format)
    print("2", type(file_state.start_time))

    print(file_state.to_dict())
