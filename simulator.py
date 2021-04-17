from time import time
from random import randint
from app import tableSimulation
import argparse
import numpy as np

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument(
    "--totalPersons",
    default=100,
    type=int,
    help="Total Persons"
)

args = parser.parse_args()


def getRandomEvent(events={1: 1, 2: 2, 3: 2, 4: 3}):
    allEvents = sorted(list(events.keys()))
    randomEvent = randint(allEvents[0], allEvents[-1])
    return (randomEvent, events[randomEvent])


def simulate(totalPersons, **kwargs):
    events = {1: 1, 2: 2, 3: 2, 4: 3}
    prices = {1: 0, 2: 10, 3: 100, 4: 150}
    eventList = []
    for i in range(totalPersons):
        event, eventTime = getRandomEvent(events)
        revenue = prices[event]
        eventList.append((event, eventTime, revenue))
    chunks = tableSimulation.chunks(eventList, 1)
    res = chunks.apply_async(queue="tableSimulation")
    start = time()
    revenue = np.sum(res.get(), axis=0)[0]
    end = time()
    totalTime = np.sum(eventList, axis=0)[1]
    print(revenue)
    print(totalTime)
    print(end - start)
    revenuePerDay = revenue * 24 * 60 / (end - start) / 10
    print(revenuePerDay)


if __name__ == "__main__":
    simulate(args.totalPersons)
