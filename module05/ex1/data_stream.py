from abc import ABC, abstractmethod
from typing import Any, TypeAlias, Union


LogEntry: TypeAlias = dict[str, str]

NumericInput: TypeAlias = Union[
    int,
    float,
    list[Union[int, float]]
]

TextInput: TypeAlias = Union[
    str,
    list[str]
]

LogInput: TypeAlias = Union[
    LogEntry,
    list[LogEntry]
]


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> str:
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            i = 0

            while i < len(data):
                if not isinstance(data[i], (int, float)):
                    return False

                i += 1

            return True

        return False

    def ingest(self, data: NumericInput) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            i = 0

            while i < len(data):
                self.storage.append(str(data[i]))
                self.total_processed += 1
                i += 1
        else:
            self.storage.append(str(data))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            i = 0

            while i < len(data):
                if not isinstance(data[i], str):
                    return False

                i += 1

            return True

        return False

    def ingest(self, data: TextInput) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            i = 0

            while i < len(data):
                self.storage.append(data[i])
                self.total_processed += 1
                i += 1
        else:
            self.storage.append(data)
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate_log(self, log: Any) -> bool:
        if not isinstance(log, dict):
            return False

        for key, value in log.items():
            if not isinstance(key, str):
                return False

            if not isinstance(value, str):
                return False

        return True

    def validate(self, data: Any) -> bool:
        if self.validate_log(data):
            return True

        if isinstance(data, list):
            i = 0

            while i < len(data):
                if not self.validate_log(data[i]):
                    return False

                i += 1

            return True

        return False

    def ingest(self, data: LogInput) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, list):
            i = 0

            while i < len(data):
                d = data[i]

                self.storage.append(
                    d["log_level"] + ": " + d["log_message"]
                )

                self.total_processed += 1
                i += 1
        else:
            self.storage.append(
                data["log_level"] + ": " + data["log_message"]
            )

            self.total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(
        self,
        proc: DataProcessor
    ) -> None:
        self.processors.append(proc)

    def process_stream(
        self,
        stream: list[Any]
    ) -> None:

        i = 0

        while i < len(stream):
            item = stream[i]

            handled = False

            j = 0

            while j < len(self.processors):
                p = self.processors[j]

                if p.validate(item):
                    p.ingest(item)
                    handled = True
                    break

                j += 1

            if not handled:
                print(
                    "DataStream error - Can't process element in stream:",
                    item
                )

            i += 1

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if len(self.processors) == 0:
            print("No processor found, no data")
            return

        i = 0

        while i < len(self.processors):
            p = self.processors[i]

            print(
                type(p).__name__ + ": total",
                p.total_processed,
                "items processed, remaining",
                len(p.storage),
                "on processor"
            )

            i += 1


print("=== Code Nexus - Data Stream ===")


stream = DataStream()

print("\nInitialize Data Stream...")

stream.print_processors_stats()


num = NumericProcessor()

print("\nRegistering Numeric Processor")

stream.register_processor(num)


batch1 = [
    "Hello world",
    [3.14, -1, 2.71],
    [
        {
            'log_level': 'WARNING',
            'log_message': 'Telnet access!!'
        },
        {
            'log_level': 'INFO',
            'log_message': 'User is connected'
        }
    ],
    42,
    ['Hi', 'five']
]

print("\nSend first batch of data on stream:", batch1)

stream.process_stream(batch1)

stream.print_processors_stats()


print("\nRegistering other processors")

txt = TextProcessor()
log = LogProcessor()

stream.register_processor(txt)
stream.register_processor(log)

print("Send the same batch again")

stream.process_stream(batch1)

stream.print_processors_stats()


print(
    "\nConsume some elements from data processors:"
    " Numeric 3, Text 2, Log 1"
)

num.output()
num.output()
num.output()

txt.output()
txt.output()

log.output()

stream.print_processors_stats()
