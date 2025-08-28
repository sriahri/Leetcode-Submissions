class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(destination, start), max(start, destination)
        return min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))