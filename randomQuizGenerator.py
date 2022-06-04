import pprint
import random
import capitals

capitals = capitals.capitals


# Generate 35 quize files.
for quizNum in range(35):
    quizFile = open ('quizes\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile =  open('answers\capitalsquiz_answer%s.txt' % (quizNum +1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDates:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states, making a question for each
    for questionNum in range(50):
        # Get right and wrong answer
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
