import marimo

__generated_with = "0.9.27"
app = marimo.App(width="medium")


@app.cell
def __():
    # Import standard set of packages

    import marimo as mo
    import pyparsing as pp
    import polars as pl
    import numpy as np
    from pathlib import Path
    return Path, mo, np, pl, pp


@app.cell
def __():
    # Import additional packages
    return


@app.cell
def __(mo):
    # Setup things
    day_select = mo.ui.dropdown(
        options=[str(i) for i in range(32)], value="1", label="Which day?"
    )
    day_select
    return (day_select,)


@app.cell
def __(mo):
    part_select = mo.ui.switch(label='Part 2?')
    part_select
    return (part_select,)


@app.cell
def __(
    day_select,
    determine_answer,
    dir_setup,
    mo,
    parse_input,
    part_select,
    pp,
):
    day = int(day_select.value)
    part = 2 if part_select.value else 1
    base_dir, day_dir, input_file, description_file, description_text = dir_setup(day, part)
    pp.ParserElement.enablePackrat()
    parsed_input = parse_input(input_file)
    mo.md(f"""
    # Advent of Code 2024, Day {day}, Part {part}

    ## Description

    {description_text}

    ## Input file

    The input file is located at {input_file}. Some example parsed data:

    {parsed_input[0][:10]}

    ## Solution

    {determine_answer(input_file)}
    """)
    return (
        base_dir,
        day,
        day_dir,
        description_file,
        description_text,
        input_file,
        parsed_input,
        part,
    )


@app.cell
def __(Path, Tuple, __file__):
    def dir_setup(day: int, part: int) -> Tuple[Path, Path, Path, Path, str]:
        """
        Setup the environment for the given day and part of the puzzle.
        This includes setting the input file path, the description file path, and enabling packrat parsing.

        Parameters
        ----------
        day : int
            The day of the puzzle, ranging from 1 to 31.
        part : int
            The part of the puzzle, either 1 or 2.

        Returns
        -------
        Tuple[Path, Path, Path, Path, str]
            A tuple containing the base directory, the day directory, the input file path, the description file path, and the description text.
        """
        base_dir = Path(__file__).parent
        day_dir = base_dir / Path(f'{day:02d}')
        input_file = day_dir / Path(f'input_{part}.txt')
        description_file = day_dir / Path(f'description_{part}.txt')
        description_text = description_file.read_text()
        return base_dir, day_dir, input_file, description_file, description_text
    return (dir_setup,)


@app.cell
def __(Path, pp):
    # Parse input
    def parse_input(input_file: Path) -> tuple[list[int], list[int]]:
        """
        Parse the input file and return the data in a suitable format for this question.

        Parameters
        ----------
        input_file : Path
            The path to the input file, which should be a .txt file containing the input data.

        Returns
        -------
        tuple[list[int], list[int]]
            A tuple containing two lists of integers. The first list contains the first numbers in each pair, and the second list contains the second numbers in each pair
        """

        integer = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))
        line_parser = integer + pp.OneOrMore(pp.White()) + integer

        parsed_results = pp.OneOrMore(line_parser).parse_file(input_file)
        first_numbers = []
        second_numbers = []
        for i in range(0, len(parsed_results), 3):
            first_numbers.append(parsed_results[i])
            # i+1 is the whitespace
            second_numbers.append(parsed_results[i+2])

        return first_numbers, second_numbers
    return (parse_input,)


@app.cell
def __(Any, parse_input):
    def determine_answer(input_file: Any) -> str:
        col_1, col_2 = parse_input(input_file)
        col_1.sort()
        col_2.sort()

        # 2. Iterate over pairs, calculate distance between each pair, sum all distances
        total_dist = 0
        for num_1, num_2 in zip(col_1, col_2):
            total_dist += abs(num_1 - num_2)
        answer = f"The sum of distances between the pairs is {total_dist}!"
        return answer
    return (determine_answer,)


if __name__ == "__main__":
    app.run()
