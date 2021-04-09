import random
from dataclasses import dataclass
from typing import List


@dataclass
class Element:
    weight: float


class Container:

    def __init__(self):
        self.available_space: float = 1
        self.elements: List[int] = []

    def put_element(self, element):
        self.available_space -= element.weight
        self.elements.append(element)

    def __repr__(self):
        return f'Container: {self.available_space}; elements: {self.elements}'


def next_fit(elements: list) -> (int, list):
    containers = [Container()]

    for element in elements:
        container = containers[-1]

        if container.available_space < element.weight:
            containers.append(Container())
            container = containers[-1]

        container.put_element(element)

    return len(containers), containers


def first_fit(elements: list) -> (int, list):
    containers = [Container()]

    for element in elements:
        for container in containers:
            if container.available_space > element.weight:
                container.put_element(element)
                break

        if element not in container.elements:
            containers.append(Container())
            container = containers[-1]
            container.put_element(element)

    return len(containers), containers


def best_fit(elements: list) -> (int, list):
    containers = [Container()]

    for element in elements:
        best_container_index, min_available_space = None, 1

        for container_index, container in enumerate(containers):
            if container.available_space > element.weight:
                if container.available_space - element.weight < min_available_space:
                    min_available_space = container.available_space - element.weight
                    best_container_index = container_index

        if best_container_index is None:
            containers.append(Container())
            container = containers[-1]
            container.put_element(element)

        else:
            container = containers[best_container_index]
            container.put_element(element)

    return len(containers), containers


def first_fit_decreasing(elements: list) -> (int, list):
    elements.sort(key=lambda element: element.weight, reverse=True)
    return first_fit(elements)


if __name__ == '__main__':
    NUM_OF_ELEMENTS = 10_000
    elements_to_pack = [Element(random.random()) for _ in range(NUM_OF_ELEMENTS)]
    print(f'Next Fit. Num of containers: {next_fit(elements_to_pack)[0]}')
    print(f'First Fit. Num of containers: {first_fit(elements_to_pack)[0]}')
    print(f'Best Fit. Num of containers: {best_fit(elements_to_pack)[0]}')
    print(f'First Fit Decreasing. Num of containers: {first_fit_decreasing(elements_to_pack)[0]}')
