import marimo

__generated_with = "0.9.27"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pyparsing as pp
    from pathlib import Path
    return Path, mo, pp


@app.cell
def __(determine_answers, mo, parse_input, pp, setup):
    day = 1
    input_file, description_text_1, description_text_2  = setup(day)
    pp.ParserElement.enablePackrat()
    parsed_input = parse_input(input_file)
    answer_1, answer_2 = determine_answers(input_file)

    mo.md(f"""
    # Advent of Code 2024, Day {day}

    {description_text_1}

    ### Solution

    {answer_1}

    {description_text_2}

    ### Solution

    {answer_2}

    """)
    return (
        answer_1,
        answer_2,
        day,
        description_text_1,
        description_text_2,
        input_file,
        parsed_input,
    )


@app.cell
def __(Path, Tuple, __file__):
    def setup(day: int) -> Tuple[Path, Path, Path, Path, str]:
        """
        Setup the environment for the puzzles for the given day.
        This includes getting the input file path and retrieving the description text.

        Parameters
        ----------
        day : int
            The day of the puzzle, ranging from 1 to 31.
        Returns
        -------
        tuple[Path, str, str]
            A tuple containing the Path to the input file, and the description text for the first and second parts of the puzzle.
        """
        base_dir = Path(__file__).parent
        day_dir = base_dir / Path(f'{day:02d}')
        input_file = day_dir / Path(f'input.txt')
        if not input_file.exists():
            raise FileNotFoundError(f"No input file found in {day_dir}")
        description_file_1 = day_dir / Path(f'description_1.txt')
        description_text_1 = description_file_1.read_text()
        description_file_2 = day_dir / Path(f'description_2.txt')
        description_text_2 = description_file_2.read_text()
        return input_file, description_text_1, description_text_2
    return (setup,)


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
        line_parser = integer + integer
        parsed_results = pp.OneOrMore(line_parser).parse_file(input_file)

        col_1 = []
        col_2 = []
        for i in range(0, len(parsed_results), 2):
            col_1.append(parsed_results[i])
            col_2.append(parsed_results[i+1])

        return col_1, col_2
    return (parse_input,)


@app.cell
def __(Path, parse_input):
    def determine_answers(input_file: Path) -> tuple[str,str]:
        """
        Calculates the answers to both parts of the puzzle, and then returns them as formatted strings.

        Parameters
        ----------
        input_file : Path
            The path to the input file, which should be a .txt file containing the input data.

        Returns
        -------
        tuple[str,str]
            A tuple containing two strings with the answers to the first and second parts of the puzzle.
        """

        def determine_answer_1(col_1: list[int], col_2: list[int]) -> int:
            col_1.sort()
            col_2.sort()
            total_dist = 0
            for num_1, num_2 in zip(col_1, col_2):
                total_dist += abs(num_1 - num_2)
            return total_dist

        def determine_answer_2(col_1: list[int], col_2: list[int]) -> int:
            total_sim = 0
            for num in col_1:
                while num in col_2:
                    total_sim += num
                    col_2.remove(num)
            return total_sim

        col_1, col_2 = parse_input(input_file)
        answer_1 = determine_answer_1(col_1, col_2)
        answer_2 = determine_answer_2(col_1, col_2)
        answer_1_str = f"""
        For each pair of numbers, add the absolute difference between them to the total distance.

        The sum of distances between the pairs is **{answer_1}**. 
        """
        answer_2_str = f"""
        For each occurence of a number from col_1 in col_2, add that number to the total similarity.

        The sum of similarities is **{answer_2}**."""    
        return answer_1_str, answer_2_str
    return (determine_answers,)


if __name__ == "__main__":
    app.run()
