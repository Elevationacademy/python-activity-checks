import os
import json
from subprocess import Popen, PIPE
import pytest
import unittest

# getting locations
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))
src_loc = os.path.join(__location__, 'src')
selected_movies_loc = os.path.join(__location__, 'src', 'selected_movies.json')

# delete selected_movies.json file if it was pushed to the repo by the student
try:
    os.remove(selected_movies_loc)
except:
    pass

# run exercise1 file that should create a selected_movies.json file
process = Popen(['python', 'exercise1.py'], stdout=PIPE, text=True, cwd=src_loc)
stdout, stderr = process.communicate()

class TestEx1(unittest.TestCase):
    def test_exercise1(self):
        try:
            with open(selected_movies_loc, 'r') as m:
                selected_movies = json.load(m)
        except:
            # Asserting that there isn't a selected_movies.json file
            assert False, "Exercise 1 - expected for a selected_movies.json file to be created in src folder, but the file is missing"

        # Calculate average score of selected_movies.json
        target_average_score = 361 / 4
        actual_average_score = 0
        for movie in selected_movies:
            try:
                actual_average_score += int(movie["score"])
            except:
                assert False, f"Could not calculate average of selected_movies' score. Make sure there is a 'score' key in each dictionary of selected_movies"
        actual_average_score /= 4

        # Check for length of selected_movies.json
        assert len(
            selected_movies) == 4, f"Expected selected_movies.json to be of length of 4, but received length of {len(selected_movies)} instead"

        # Check for average score of selected_movies.json
        assert actual_average_score == target_average_score, f"Expected the average score of selected_movies.json to be {target_average_score}, but received '{actual_average_score}' instead"

        # Check if the actor Robert De Niro included in all of selected_movies.json
        is_de_niro = True
        no_de_niro_count = 0
        for movie in selected_movies:
            if not "De Niro" in movie["actors"]:
                is_de_niro = False
                no_de_niro_count+=1
        assert is_de_niro, f"Expected all the movies in selected_movies.json to include Robert De Niro movies, but received {no_de_niro_count} movies without him as an actor"