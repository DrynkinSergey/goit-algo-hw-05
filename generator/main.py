from typing import Callable, Generator
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."


def generator_numbers(text: str) -> Generator[float, None, None]:
    """Generator numbers from text

    Args:
        text (str): text for search float nums

    Yields:
        float: return value from generator
    """
    split_text = text.split()
    numbers = ([float(char)
                for char in split_text if '.' in char and char[-1] != '.'])
    for num in numbers:
        yield num


def sum_profit(text: str, generator_numbers: Callable[[str], Generator[float, None, None]]):
    """Calculate sum from text

    Args:
        text (str): Text where numbers have indent left and right and use period as separator
        generator_numbers (Collable): _description_

    Returns:
        _type_: _description_
    """
    result = 0
    for i in generator_numbers(text):
        result += i
    return result


total = sum_profit(text, generator_numbers)

print(f'Total amount {total}')
