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
def __(answer_1_str, answer_2_str, day, mo):
    mo.md(f"""
    # Advent of Code 2024, Day {day}
    [Description](https://adventofcode.com/2024/day/{day})
    ### Solution 1

    {answer_1_str}

    ### Solution 2

    {answer_2_str}

    """)
    return


@app.cell
def __(determine_answers, parse_input):
    day = 2
    data = parse_input(day)
    answer_1_str, answer_2_str = determine_answers(data)
    return answer_1_str, answer_2_str, data, day


@app.cell
def __(Path, __file__, pp):
    def parse_input(day: int) -> list[list[int]]:
        """
        Parse the input file and return the data in a suitable format for this question.

        Parameters
        ----------
        day: int
            The day of the puzzle, ranging from 1 to 31.

        Returns
        -------
        list[list[int]]:
            A list containing each report. Each report is a list of ints. 
        """

        base_dir = Path(__file__).parent
        day_dir = base_dir / Path(f'{day:02d}')
        input_file = day_dir / Path(f'input.txt')
        line_parser = pp.OneOrMore(pp.Word(pp.nums).setParseAction(lambda t: int(t[0])))
        multi_line_parser = pp.OneOrMore(line_parser)
        parsed_results = multi_line_parser.parse_file(input_file)

        print(len(parsed_results))
        print(parsed_results)
        return parsed_results
    return (parse_input,)


@app.cell
def __():
    def determine_answers(data: list[list[int]]) -> tuple[str,str]:
        """
        Calculates the answers to both parts of the puzzle, and then returns them as formatted strings.

        Parameters
        ----------
        data: list[list[int]]
            list containing each report. Each report is a list of ints
        Returns
        -------
        tuple[str,str]
            A tuple containing two strings with the answers to the first and second parts of the puzzle.
        """

        def determine_answer_1(data: list[list[int]]) -> int:
            safe_report_count: int = 0 
            return safe_report_count

        def determine_answer_2(data: list[list[int]]) -> int:
            unknown = 0
            return unknown

        answer_1 = determine_answer_1(data)
        answer_2 = determine_answer_2(data) 
        answer_1_str = f"""
        --algorithm 1--

        --answer 1 explain-- is **{answer_1}**. 
        """
        answer_2_str = f"""
        --algorithm 2--
        --answer 2 explain-- **{answer_2}**."""    
        return answer_1_str, answer_2_str
    return (determine_answers,)


if __name__ == "__main__":
    app.run()
