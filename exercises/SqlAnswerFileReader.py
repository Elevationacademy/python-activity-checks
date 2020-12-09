

class AnswersFile:

    def __init__(self, filename):
        f = open(f'{filename}.sql', 'r')
        script = f.read()
        f.close()
        self.answers = self.ParseToSections(script)

    def ParseToSections(self, script):
        separator = '--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
        return script.split(separator)

    def __getitem__(self, index):
        return self.answers[index]


TestAnswers = AnswersFile('Solution')



