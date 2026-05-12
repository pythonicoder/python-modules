from abc import ABC, abstractmethod
from typing import Any, Protocol, TypeAlias, Union


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
            raise Exception("No data stored")

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


class ExportPlugin(Protocol):
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVPlugin:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:

        i = 0

        out = ""

        while i < len(data):
            out += data[i][1]

            if i < len(data) - 1:
                out += ","

            i += 1

        print("CSV Output:")
        print(out)


class JSONPlugin:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:

        i = 0

        out = "{"

        while i < len(data):
            rank = data[i][0] - 1
            value = data[i][1]

            out += (
                '"item_' +
                str(rank) +
                '": "' +
                value +
                '"'
            )

            if i < len(data) - 1:
                out += ", "

            i += 1

        out += "}"

        print("JSON Output:")
        print(out)


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

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin
    ) -> None:

        i = 0

        while i < len(self.processors):
            p = self.processors[i]

            exported: list[tuple[int, str]] = []

            n = 0

            while n < nb and len(p.storage) > 0:
                exported.append(p.output())

                n += 1

            if len(exported) > 0:
                plugin.process_output(exported)

            i += 1


print("=== Code Nexus - Data Pipeline ===")


stream = DataStream()

print("\nInitialize Data Stream...\n")

stream.print_processors_stats()


num = NumericProcessor()
txt = TextProcessor()
log = LogProcessor()

print("\nRegistering Processors")

stream.register_processor(num)
stream.register_processor(txt)
stream.register_processor(log)


batch1 = [
    "Hello world",
    [3.14, -1, 2.71],
    [
        {
            "log_level": "WARNING",
            "log_message": "Telnet access! Use ssh instead"
        },
        {
            "log_level": "INFO",
            "log_message": "User wil is connected"
        }
    ],
    42,
    ["Hi", "five"]
]

print("\nSend first batch of data on stream:", batch1)

stream.process_stream(batch1)

stream.print_processors_stats()


print("\nSend 3 processed data from each processor to a CSV plugin:\n")

csv = CSVPlugin()

stream.output_pipeline(3, csv)

stream.print_processors_stats()


batch2 = [
    21,
    ["I love AI", "LLMs are wonderful", "Stay healthy"],
    [
        {
            "log_level": "ERROR",
            "log_message": "500 server crash"
        },
        {
            "log_level": "NOTICE",
            "log_message": "Certificate expires in 10 days"
        }
    ],
    [32, 42, 64, 84, 128, 168],
    "World hello"
]

print("\nSend another batch of data:", batch2)

stream.process_stream(batch2)

stream.print_processors_stats()


print("\nSend 5 processed data from each processor to a JSON plugin:\n")

json = JSONPlugin()

stream.output_pipeline(5, json)

stream.print_processors_stats()
