from typing import Any, Union, TypeAlias
from abc import ABC, abstractmethod


LogEntry: TypeAlias = dict[str, str]

NumericData: TypeAlias = Union[int, float]
NumericInput: TypeAlias = Union[NumericData, list[NumericData]]

TextInput: TypeAlias = Union[str, list[str]]

LogInput: TypeAlias = Union[LogEntry, list[LogEntry]]


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.storage) == 0:
            raise IndexError("No data stored")

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
                self.total_processed += 1

                self.storage.append(
                    (
                        self.total_processed,
                        str(data[i])
                    )
                )

                i += 1
        else:
            self.total_processed += 1

            self.storage.append(
                (
                    self.total_processed,
                    str(data)
                )
            )


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
                self.total_processed += 1

                self.storage.append(
                    (
                        self.total_processed,
                        data[i]
                    )
                )

                i += 1
        else:
            self.total_processed += 1

            self.storage.append(
                (
                    self.total_processed,
                    data
                )
            )


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

                self.total_processed += 1

                self.storage.append(
                    (
                        self.total_processed,
                        d["log_level"] + ": " + d["log_message"]
                    )
                )

                i += 1
        else:
            self.total_processed += 1

            self.storage.append(
                (
                    self.total_processed,
                    data["log_level"] + ": " + data["log_message"]
                )
            )


print("=== Code Nexus - Data Processor ===")


num = NumericProcessor()

print("\nTesting Numeric Processor...")

print("Trying to validate input '42':", num.validate(42))

print("Trying to validate input 'Hello':", num.validate("Hello"))

print("Test invalid ingestion of string 'foo' without prior validation:")

try:
    num.ingest("foo")  # type: ignore[arg-type]
except Exception as e:
    print("Got exception:", e)

print("Processing data:", [1, 2, 3, 4, 5])

num.ingest([1, 2, 3, 4, 5])

print("Extracting 3 values...")

i = 0
while i < 3:
    rank, value = num.output()

    print("Numeric value " + str(i) + ":", value)

    i += 1


txt = TextProcessor()

print("\nTesting Text Processor...")

print("Trying to validate input '42':", txt.validate(42))

txt.ingest(
    ["Hello", "Nexus", "World"]
)

print("Processing data:", ["Hello", "Nexus", "World"])

print("Extracting 1 value...")

rank, value = txt.output()

print("Text value 0:", value)


log = LogProcessor()

print("\nTesting Log Processor...")

print("Trying to validate input 'Hello':", log.validate("Hello"))

logs = [
    {
        "log_level": "NOTICE",
        "log_message": "Connection to server"
    },
    {
        "log_level": "ERROR",
        "log_message": "Unauthorized access!!"
    }
]

print("Processing data:", logs)

log.ingest(logs)

print("Extracting 2 values...")

i = 0
while i < 2:
    rank, value = log.output()

    print("Log entry " + str(i) + ":", value)

    i += 1
