
# Starships Info

This Python script uses the Star Wars API (SWAPI) to fetch data about Starships that are less than a certain length.

## Requirements

The script uses the following Python libraries:

- `requests` for making HTTP requests.
- `argparse` for handling command line arguments.
- `tabulate` for pretty-printing the output in tabular format.

You can install these with pip:

```bash
pip install requests argparse tabulate
```

## Usage

To run the script, use the following command:

```bash
python fetch_starships.py --max_length 50 --max_results 20
```

You can customize the `max_length` and `max_results` parameters to suit your needs.

- `max_length` is the maximum length of the starships. The script will fetch starships that are shorter than this length.
- `max_results` is the maximum number of starships to fetch.

If you don't provide these arguments, the script will use the defaults (25 meters for `max_length` and 11 for `max_results`).

The script outputs the data in a table with two columns: "Starship Name" and "Length (m)".

## Example

Here is an example of how to run the script and what the output might look like:

```bash
python fetch_starships.py --max_length 25 --max_results 50
```

Output:

```
+--------------------------+--------------+
| Starship Name            |   Length (m) |
+==========================+==============+
| Jedi starfighter         |          8   |
+--------------------------+--------------+
| TIE Advanced x1          |          9.2 |
+--------------------------+--------------+
| A-wing                   |          9.6 |
+--------------------------+--------------+
| Naboo fighter            |         11   |
+--------------------------+--------------+
| X-wing                   |         12.5 |
+--------------------------+--------------+
| Y-wing                   |         14   |
+--------------------------+--------------+
| Solar Sailer             |         15.2 |
+--------------------------+--------------+
| B-wing                   |         16.9 |
+--------------------------+--------------+
| Theta-class T-2c shuttle |         18.5 |
+--------------------------+--------------+
| Imperial shuttle         |         20   |
+--------------------------+--------------+
| Slave 1                  |         21.5 |
+--------------------------+--------------+

Total starships found: 11
```

This indicates that the script found 11 starships that are less than 25 meters long. The starships are listed in ascending order of length.
