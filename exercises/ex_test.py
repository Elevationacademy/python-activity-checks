from importlib.machinery import SourceFileLoader
import os
import pytest
import unittest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))
evaluation_loc = os.path.join(__location__, 'src', 'exercises.py')

# get find_movies_by_dur_range
find_movies_by_dur_range = SourceFileLoader("find_movies_by_dur_range",
                                            evaluation_loc).load_module().find_movies_by_dur_range
# get find_movies_by_year_and_genre
find_movies_by_year_and_genre = SourceFileLoader("find_movies_by_dur_range",
                                                 evaluation_loc).load_module().find_movies_by_year_and_genre

# get find_num_of_movies_by_actors
find_num_of_movies_by_actors = SourceFileLoader("find_movies_by_dur_range",
                                                evaluation_loc).load_module().find_num_of_movies_by_actors
# get count_movies_by_genres
count_movies_by_genres = SourceFileLoader("find_movies_by_dur_range",
                                          evaluation_loc).load_module().count_movies_by_genres


# TESTS
class TestEx1(unittest.TestCase):
    def test1_ex1(self):
        assert find_movies_by_dur_range(80, 90) == ['Madagascar: Escape 2 Africa', 'Madagascar', 'Big Nothing',
                                                    'Ice Age'], f"Exercise 1 - accept to receive ['Madagascar: Escape 2 Africa', 'Madagascar', 'Big Nothing', 'Ice Age'] when searching for movies between 80 to 90 minutes, but received '{find_movies_by_dur_range(80, 90)}' instead"
        assert find_movies_by_dur_range(0,
                                        60) == [], f"Exercise 1 - accept to receive [] when searching for movies between 0 to 60 minutes, but received '{find_movies_by_dur_range(0, 60)}' instead"
        assert find_movies_by_dur_range(118, 120) == ['Looper', 'The Beach', 'Match Point', 'American History X',
                                                    'Birdman or (The Unexpected Virtue of Ignorance)'], f"Exercise 1 - accept to receive ['Looper', 'The Beach', 'Match Point', 'American History X', 'Birdman or (The Unexpected Virtue of Ignorance)'] when searching for movies between 118 to 120 minutes, but received '{find_movies_by_dur_range(118, 120)}' instead"
class TestEx2(unittest.TestCase):
    def test_ex2(self):
        assert find_movies_by_year_and_genre(2002, "Animation") == [
            'Ice Age'], f"Exercise 2 - accept to receive ['Ice Age'] when searching for movies with year of 2002 and genre of Animation, but received '{find_movies_by_year_and_genre(2002, 'Animation')}' instead"
        assert find_movies_by_year_and_genre(2003, "History") == [
            'The Last Samurai'], f"Exercise 2 - accept to receive ['The Last Samurai'] when searching for movies with year of 2003 and genre of History, but received '{find_movies_by_year_and_genre(2003, 'History')}' instead"
        assert find_movies_by_year_and_genre(1974, "Mystery") == [
            'Chinatown'], f"Exercise 2 - accept to receive ['Chinatown'] when searching for movies with year of 2003 and genre of History, but received '{find_movies_by_year_and_genre(1974, 'Mystery')}' instead"
class TestEx3(unittest.TestCase):
    def test_ex3(self):
        assert find_num_of_movies_by_actors([
            "John Lithgow"]) == 2, f"Exercise 3 - accept to receive 2 when searching for number of movies with John Lithgow, but received '{find_num_of_movies_by_actors(['John Lithgow'])}' instead"
        assert find_num_of_movies_by_actors([
            "Robert De Niro"]) == 4, f"Exercise 3 - accept to receive 2 when searching for number of movies with Robert De Niro, but received '{find_num_of_movies_by_actors(['Robert De Niro'])}' instead"
        assert find_num_of_movies_by_actors(["David Schwimmer",
                                            "Simon Pegg"]) == 1, f"Exercise 3 - accept to receive 1 when searching for number of movies with David Schwimmer and Simon Pegg, but received '{find_num_of_movies_by_actors(['David Schwimmer', 'Simon Pegg'])}' instead"
class TestEx4(unittest.TestCase):
    def test_ex4(self):
        try:
            assert count_movies_by_genres()[
                    "Comedy"] == 36, f"Exercise 4 - accept to receive a dictionary containing a key of 'Comedy' with value of 36 when invoking count_movies_by_genres, but received '{count_movies_by_genres()}' instead"
            assert count_movies_by_genres()[
                    "Thriller"] == 26, f"Exercise 4 - accept to receive a dictionary containing a key of 'Thriller' with value of 26 when invoking count_movies_by_genres, but received '{count_movies_by_genres()}' instead"
            assert count_movies_by_genres()[
                    "Horror"] == 2, f"Exercise 4 - accept to receive a dictionary containing a key of 'Horror' with value of 2 when invoking count_movies_by_genres, but received '{count_movies_by_genres()}' instead"
        except:
            assert False, "An error occure while running a test on count_movies_by_genres function"



















