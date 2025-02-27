"""
Visibility Road Map Planner
author: Atsushi Sakai (@Atsushi_twi)
"""



import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))


class Geometry:

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    @staticmethod
    def is_seg_intersect(p1, q1, p2, q2):

        def on_segment(p, q, r):
            if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
                    (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
                return True
            return False

        def orientation(p, q, r):
            val = (float(q.y - p.y) * (r.x - q.x)) - (
                    float(q.x - p.x) * (r.y - q.y))
            if val > 0:
                return 1
            if val < 0:
                return 2
            return 0

        # Find the 4 orientations required for
        # the general and special cases
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if (o1 != o2) and (o3 != o4):
            return True
        if (o1 == 0) and on_segment(p1, p2, q1):
            return True
        if (o2 == 0) and on_segment(p1, q2, q1):
            return True
        if (o3 == 0) and on_segment(p2, p1, q2):
            return True
        if (o4 == 0) and on_segment(p2, q1, q2):
            return True

        return False

"""

Dijkstra Search library

author: Atsushi Sakai (@Atsushi_twi)

"""

import matplotlib.pyplot as plt
import math
import numpy as np

class DijkstraSearch:
    class Node:
        """
        Node class for dijkstra search
        """

        def __init__(self, x, y, cost=None, parent=None, edge_ids=None):
            self.x = x
            self.y = y
            self.cost = cost
            self.parent = parent
            self.edge_ids = edge_ids

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent)

    def __init__(self, show_animation):
        self.show_animation = show_animation

    def search(self, sx, sy, gx, gy, node_x, node_y, edge_ids_list):
        """
        Search shortest path

        s_x: start x positions [m]
        s_y: start y positions [m]
        gx: goal x position [m]
        gx: goal x position [m]
        node_x: node x position
        node_y: node y position
        edge_ids_list: edge_list each item includes a list of edge ids
        """

        start_node = self.Node(sx, sy, 0.0, -1)
        goal_node = self.Node(gx, gy, 0.0, -1)
        current_node = None

        open_set, close_set = dict(), dict()
        open_set[self.find_id(node_x, node_y, start_node)] = start_node

        while True:
            if self.has_node_in_set(close_set, goal_node):
                print("goal is found!")
                goal_node.parent = current_node.parent
                goal_node.cost = current_node.cost
                break
            elif not open_set:
                print("Cannot find path")
                break

            current_id = min(open_set, key=lambda o: open_set[o].cost)
            current_node = open_set[current_id]

            # Remove the item from the open set
            del open_set[current_id]
            # Add it to the closed set
            close_set[current_id] = current_node

            # expand search grid based on motion model
            for i in range(len(edge_ids_list[current_id])):
                n_id = edge_ids_list[current_id][i]
                dx = node_x[n_id] - current_node.x
                dy = node_y[n_id] - current_node.y
                d = math.hypot(dx, dy)
                node = self.Node(node_x[n_id], node_y[n_id],
                                 current_node.cost + d, current_id)

                if n_id in close_set:
                    continue
                # Otherwise if it is already in the open set
                if n_id in open_set:
                    if open_set[n_id].cost > node.cost:
                        open_set[n_id] = node
                else:
                    open_set[n_id] = node

        # generate final course
        rx, ry = self.generate_final_path(close_set, goal_node)

        return rx, ry

    @staticmethod
    def generate_final_path(close_set, goal_node):
        rx, ry = [goal_node.x], [goal_node.y]
        parent = goal_node.parent
        while parent != -1:
            n = close_set[parent]
            rx.append(n.x)
            ry.append(n.y)
            parent = n.parent
        rx, ry = rx[::-1], ry[::-1]  # reverse it
        return rx, ry

    def has_node_in_set(self, target_set, node):
        for key in target_set:
            if self.is_same_node(target_set[key], node):
                return True
        return False

    def find_id(self, node_x_list, node_y_list, target_node):
        for i, _ in enumerate(node_x_list):
            if self.is_same_node_with_xy(node_x_list[i], node_y_list[i],
                                         target_node):
                return i
        return None

    @staticmethod
    def is_same_node_with_xy(node_x, node_y, node_b):
        dist = np.hypot(node_x - node_b.x,
                        node_y - node_b.y)
        return dist <= 0.1

    @staticmethod
    def is_same_node(node_a, node_b):
        dist = np.hypot(node_a.x - node_b.x,
                        node_a.y - node_b.y)
        return dist <= 0.1


show_animation = True


class VisibilityRoadMap:

    def __init__(self, expand_distance, do_plot=False):
        self.expand_distance = expand_distance
        self.do_plot = do_plot

    def planning(self, start_x, start_y, goal_x, goal_y, obstacles):

        nodes = self.generate_visibility_nodes(start_x, start_y,
                                               goal_x, goal_y, obstacles)

        road_map_info = self.generate_road_map_info(nodes, obstacles)

        if self.do_plot:
            self.plot_road_map(nodes, road_map_info)
            plt.pause(1.0)

        rx, ry = DijkstraSearch(show_animation).search(
            start_x, start_y,
            goal_x, goal_y,
            [node.x for node in nodes],
            [node.y for node in nodes],
            road_map_info
        )

        return rx, ry

    def generate_visibility_nodes(self, start_x, start_y, goal_x, goal_y,
                                  obstacles):

        # add start and goal as nodes
        nodes = [DijkstraSearch.Node(start_x, start_y),
                 DijkstraSearch.Node(goal_x, goal_y, 0, None)]

        # add vertexes in configuration space as nodes
        for obstacle in obstacles:

            cvx_list, cvy_list = self.calc_vertexes_in_configuration_space(
                obstacle.x_list, obstacle.y_list)

            for (vx, vy) in zip(cvx_list, cvy_list):
                nodes.append(DijkstraSearch.Node(vx, vy))

        if self.do_plot:
            for node in nodes:
                plt.plot(node.x, node.y, "xr")

        return nodes

    def calc_vertexes_in_configuration_space(self, x_list, y_list):
        x_list = x_list[0:-1]
        y_list = y_list[0:-1]
        cvx_list, cvy_list = [], []

        n_data = len(x_list)

        for index in range(n_data):
            offset_x, offset_y = self.calc_offset_xy(
                x_list[index - 1], y_list[index - 1],
                x_list[index], y_list[index],
                x_list[(index + 1) % n_data], y_list[(index + 1) % n_data],
            )
            cvx_list.append(offset_x)
            cvy_list.append(offset_y)

        return cvx_list, cvy_list

    def generate_road_map_info(self, nodes, obstacles):

        road_map_info_list = []

        for target_node in nodes:
            road_map_info = []
            for node_id, node in enumerate(nodes):
                if np.hypot(target_node.x - node.x,
                            target_node.y - node.y) <= 0.1:
                    continue

                is_valid = True
                for obstacle in obstacles:
                    if not self.is_edge_valid(target_node, node, obstacle):
                        is_valid = False
                        break
                if is_valid:
                    road_map_info.append(node_id)

            road_map_info_list.append(road_map_info)

        return road_map_info_list

    @staticmethod
    def is_edge_valid(target_node, node, obstacle):

        for i in range(len(obstacle.x_list) - 1):
            p1 = Geometry.Point(target_node.x, target_node.y)
            p2 = Geometry.Point(node.x, node.y)
            p3 = Geometry.Point(obstacle.x_list[i], obstacle.y_list[i])
            p4 = Geometry.Point(obstacle.x_list[i + 1], obstacle.y_list[i + 1])

            if Geometry.is_seg_intersect(p1, p2, p3, p4):
                return False

        return True

    def calc_offset_xy(self, px, py, x, y, nx, ny):
        p_vec = math.atan2(y - py, x - px)
        n_vec = math.atan2(ny - y, nx - x)
        offset_vec = math.atan2(math.sin(p_vec) + math.sin(n_vec),
                                math.cos(p_vec) + math.cos(
                                    n_vec)) + math.pi / 2.0
        offset_x = x + self.expand_distance * math.cos(offset_vec)
        offset_y = y + self.expand_distance * math.sin(offset_vec)
        return offset_x, offset_y

    @staticmethod
    def plot_road_map(nodes, road_map_info_list):
        for i, node in enumerate(nodes):
            for index in road_map_info_list[i]:
                plt.plot([node.x, nodes[index].x],
                         [node.y, nodes[index].y], "-b")


class ObstaclePolygon:

    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list

        self.close_polygon()
        self.make_clockwise()

    def make_clockwise(self):
        if not self.is_clockwise():
            self.x_list = list(reversed(self.x_list))
            self.y_list = list(reversed(self.y_list))

    def is_clockwise(self):
        n_data = len(self.x_list)
        eval_sum = sum([(self.x_list[i + 1] - self.x_list[i]) *
                        (self.y_list[i + 1] + self.y_list[i])
                        for i in range(n_data - 1)])
        eval_sum += (self.x_list[0] - self.x_list[n_data - 1]) * \
                    (self.y_list[0] + self.y_list[n_data - 1])
        return eval_sum >= 0

    def close_polygon(self):
        is_x_same = self.x_list[0] == self.x_list[-1]
        is_y_same = self.y_list[0] == self.y_list[-1]
        if is_x_same and is_y_same:
            return  # no need to close

        self.x_list.append(self.x_list[0])
        self.y_list.append(self.y_list[0])

    def plot(self):
        plt.plot(self.x_list, self.y_list, "-k")

def read_obstacles_from_file(file_path):
    obstacles = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Check if line is not empty
                coords = line.split(',')
                x_coords = [int(coord) for coord in coords[::2]]
                y_coords = [int(coord) for coord in coords[1::2]]
                obstacles.append(ObstaclePolygon(x_coords, y_coords))
    return obstacles



def update_obstacles(old_obstacles, new_obstacles):
    all_obstacles = old_obstacles + new_obstacles

    for new_obstacle in new_obstacles:
        new_nodes = []
        for i in range(len(new_obstacle.x_list)):
            new_node = DijkstraSearch.Node(new_obstacle.x_list[i], new_obstacle.y_list[i])
            new_node.edge_ids = []  # Initialize edge_ids for new nodes
            new_nodes.append(new_node)

        for new_node in new_nodes:
            for old_obstacle in old_obstacles:
                for i in range(len(old_obstacle.x_list)):
                    p1 = Geometry.Point(new_node.x, new_node.y)
                    p2 = Geometry.Point(old_obstacle.x_list[i], old_obstacle.y_list[i])
                    p3 = Geometry.Point(old_obstacle.x_list[(i + 1) % len(old_obstacle.x_list)],
                                        old_obstacle.y_list[(i + 1) % len(old_obstacle.y_list)])
                    if not Geometry.is_seg_intersect(p1, p2, p3, p2):
                        # Add edge between new node and old obstacle node
                        new_node.edge_ids.append(len(all_obstacles) + i)
                        # Update the old obstacle node's edge list
                        all_obstacles[i].edge_ids.append(len(old_obstacles) + len(new_nodes) + i)
                    else:
                        # If edge intersects with new obstacle, remove the edge
                        if len(new_node.edge_ids) > 0:
                            new_node.edge_ids.pop()
                            all_obstacles[i].edge_ids.pop()

    return all_obstacles


def main():
    print(__file__ + " start!!")

    # start and goal position
    sx, sy = 344, 122  # [m]
    gx, gy = 406.0, 444.0  # [m]

    expand_distance = 5  # [m]

    # Read old obstacles from file
    old_obstacles = read_obstacles_from_file('obstacles.txt')

    # Read new obstacles from file
    new_obstacles = read_obstacles_from_file('new_obstacle.txt')

    # Update obstacles
    all_obstacles = update_obstacles(old_obstacles, new_obstacles)

    # Plan and plot visibility graph before update
    rx_before, ry_before = VisibilityRoadMap(expand_distance, do_plot=True).planning(sx, sy, gx, gy, old_obstacles)

    # Plan and plot visibility graph after update
    rx_after, ry_after = VisibilityRoadMap(expand_distance, do_plot=True).planning(sx, sy, gx, gy, all_obstacles)

    # Plot start and goal positions
    plt.plot(sx, sy, "or")
    plt.plot(gx, gy, "ob")

    # Plot obstacles
    for ob in all_obstacles:
        ob.plot()

    # Plot legend
    plt.legend(['Start', 'Goal', 'Obstacles'])

    plt.axis("equal")
    plt.show()

if __name__ == '__main__':
    main()

