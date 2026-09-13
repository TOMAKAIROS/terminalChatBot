# Task 1: Garage Maintenance Logger

## Goal
Build a text-based program that records maintenance done on my Subaru during one session.

## Requirements
- Print a welcome message.
- Repeatedly ask: “What maintenance did you complete? Type history, count, or quit.”
- Remove extra spaces from the beginning and end of input.
- Convert input to lowercase.

## Commands
- `history` — print the recorded maintenance entries.
- `count` — print how many entries have been added.
- `quit` — print a goodbye message and stop.

## Recording Maintenance
- Blank input should prompt the user to enter something.
- Any other input should be saved to the history and increase the count.
- Commands and blank input must never be saved or counted.

## Confirmation Function
Create a function that receives maintenance text and returns:
- `oil change` → “Fresh oil. Recorded.”
- `tire rotation` → “Tires rotated. Recorded.”
- Anything else → “Maintenance recorded.”

## Rules
- Use only the concepts covered in my earlier example.
- Keep history and count available between loop repetitions.
- Data does not need to survive after the program closes.

## Test
Enter these inputs in order:
1. `oil change`
2. A blank answer
3. `washed car`
4. `history`
5. `count`

Expected result: History contains only `oil change` and `washed car`.
The count is exactly 2.

## Status
Not started.