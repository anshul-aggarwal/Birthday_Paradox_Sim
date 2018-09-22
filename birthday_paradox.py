import numpy
import matplotlib.pylab as plt

no_of_simulations = 1000

milestone_probabilities = [25, 50, 75, 90, 99]
milestone_current = 0

def birthday_paradox(no_of_people, simulations):
    global milestone_probabilities, milestone_current

    same_birthday_two_people = 0

    #For simplicity, we assume that there are 365 days in all years.
    for sim in range(simulations):
        birthdays = numpy.random.choice(365, no_of_people, replace=True)
        unique_birthdays = set(birthdays)
        if len(unique_birthdays) < no_of_people:
            same_birthday_two_people += 1

    success_fraction = same_birthday_two_people/simulations

    if milestone_current < len(milestone_probabilities) and success_fraction*100 > milestone_probabilities[milestone_current]:
        print("P(Two people sharing birthday in a room with " + str(no_of_people) + " people) = " + str(success_fraction))
        milestone_current += 1

    return success_fraction


def main():
    day = []
    success = []
    for i in range(1, 366):
        day.append(i)
        success.append(birthday_paradox(i, no_of_simulations))

    plt.plot(day, success)
    plt.show()


main()