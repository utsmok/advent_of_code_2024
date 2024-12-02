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
def __(determine_answers, parse_input):
    day = 1
    col_1, col_2 = parse_input(day)
    answer_1_str, answer_2_str = determine_answers(col_1, col_2)
    return answer_1_str, answer_2_str, col_1, col_2, day


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
def __(Path, __file__, pp):
    def parse_input(day: int) -> tuple[list[int], list[int]]:
        """
        Parse the input file and return the data in a suitable format for this question.

        Parameters
        ----------
        day: int
            The day of the puzzle, ranging from 1 to 31.

        Returns
        -------
        tuple[list[int], list[int]]
            A tuple containing two lists of integers, each containing the numbers from one of the columns.
        """

        base_dir = Path(__file__).parent
        day_dir = base_dir / Path(f'{day:02d}')
        input_file = day_dir / Path(f'input.txt')

        num_parser = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))
        parsed_results = pp.OneOrMore(num_parser).parse_file(input_file)

        col_1 = []
        col_2 = []
        for i in range(0, len(parsed_results), 2):
            col_1.append(parsed_results[i])
            col_2.append(parsed_results[i+1])
        return col_1, col_2
    return (parse_input,)


@app.cell
def __():
    def determine_answers(col_1:list[int], col_2:list[int]) -> tuple[str,str]:
        """
        Calculates the answers to both parts of the puzzle, and then returns them as formatted strings.

        Parameters
        ----------
        col_1 : list[int], col_2 : list[int]
            Two lists of integers, representing the two columns of numbers
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

        answer_1 = determine_answer_1(col_1, col_2)
        answer_2 = determine_answer_2(col_1, col_2.copy()) # Use a copy as input to avoid destroying the original list
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
