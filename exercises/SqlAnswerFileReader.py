import os

class AnswersFile:
    def __init__(self, filename):
        f = open(f'{os.path.dirname(__file__)}/{filename}.sql', 'r')
        script = f.read()
        f.close()
        self.answers = self.ParseToSections(script)

    def ParseToSections(self, script):
        answers_prefix = '---------------------------------------------------- Begin Exercise ----------------------------------------------------'
        answers_postfix = '----------------------------------------------------- End Exercise -----------------------------------------------------'
        separator = '--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
        return script.split(answers_prefix)[1].split(answers_postfix)[0].split(separator)

    def __getitem__(self, index):
        for a in self.answers:
            if f"Exercise {index} Answer" in a:
                return a
        return None

TestAnswers = AnswersFile('Solution')



