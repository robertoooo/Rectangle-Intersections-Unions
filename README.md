# Rectangle & Intersection & Unions

Find the intersection between 2D rectangles and calculate the union.
The program will calculate the first unions to the n:th unions.

## Contents

1. Clone the repository
2. Create a virtual environment in the root folder (opt)

```sh
virtualenv mypython
source venv/scripts/activate
```

3. Install the requirements

```sh
pip install -r requriements
```

4. Run the main.py file pointing at the file of rectangles

```sh
py main.py <path to output file>
py main.py ./input.json #Run the example file
py main.py <path to input file> > <path to output file> #Point STDO to a file instead of console.

```

### Run the automated unit tests locally using pytest

The test will automatically run when pushing to development or when master makes a pull request from development.

```sh
pytest
```

## Example of Input/Output

The input JSON file:

```json
{
  "rects": [
    { "x": -100, "y": 100, "delta_x": 250, "delta_y": 80 },
    { "x": 120, "y": 20, "delta_x": 250, "delta_y": 150 },
    { "x": 140, "y": 10, "delta_x": 250, "delta_y": 100 },
    { "x": 160, "y": -140, "delta_x": 350, "delta_y": 190 }
  ]
}
```

The output:

```txt
Input:
        1: Rectangle at (-100,100), delta_x=250, delta_y=80.
        2: Rectangle at (120,20), delta_x=250, delta_y=150.
        3: Rectangle at (140,10), delta_x=250, delta_y=100.
        4: Rectangle at (160,-140), delta_x=350, delta_y=190.
Intersections:
        1: Between rectangle 1 and 2 at (120,100), delta_x=30, delta_y=70.
        2: Between rectangle 1 and 3 at (140,100), delta_x=10, delta_y=10.
        3: Between rectangle 2 and 3 at (140,20), delta_x=230, delta_y=90.
        4: Between rectangle 2 and 4 at (160,20), delta_x=210, delta_y=30.
        5: Between rectangle 3 and 4 at (160,10), delta_x=230, delta_y=40.
        6: Between rectangle 1 2 and 3 at (140,100), delta_x=10, delta_y=10.
        7: Between rectangle 2 3 and 4 at (160,20), delta_x=210, delta_y=30.
```
