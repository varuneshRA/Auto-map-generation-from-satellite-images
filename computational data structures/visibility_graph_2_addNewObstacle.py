import pyvisgraph as vg
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class ObstaclePolygon:
    def __init__(self, x_coords, y_coords):
        # Initialize the vertices of the polygon using vg.Point objects
        self.vertices = [vg.Point(x, y) for x, y in zip(x_coords, y_coords)]

def compute_shortest_path(g,polygons, start_point, end_point):
    # Find shortest path using Dijkstra's algorithm
    shortest_path = g.shortest_path(start_point, end_point)

    return shortest_path

def plot_polygons(polygons):
    # Plot the obstacles defined by polygons
    fig, ax = plt.subplots()

    for obstacle in polygons:
        # Extract vertices of each obstacle
        vertices = [(point.x, point.y) for point in obstacle.vertices]
        # Plot each obstacle as a polygon
        poly_patch = Polygon(vertices, closed=True, edgecolor='black', fill=False)
        ax.add_patch(poly_patch)

    # Set plot properties
    ax.set_aspect('equal', 'box')
    ax.autoscale()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Polygons')
    plt.show()

def plot_shortest_path(polygons, shortest_path):
    # Plot the shortest path along with obstacles
    fig, ax = plt.subplots()

    for obstacle in polygons:
        # Plot each obstacle as a polygon
        vertices = [(point.x, point.y) for point in obstacle.vertices]
        poly_patch = Polygon(vertices, closed=True, edgecolor='black', fill=False)
        ax.add_patch(poly_patch)

    # Extract X and Y coordinates of shortest path
    shortest_path_x = [point.x for point in shortest_path]
    shortest_path_y = [point.y for point in shortest_path]
    # Plot the shortest path
    ax.plot(shortest_path_x, shortest_path_y, color='red')

    # Plot start point with a larger marker
    start_point = shortest_path[0]
    ax.plot(start_point.x, start_point.y, marker='o', markersize=5, color='green')

    # Plot end point with a larger marker
    end_point = shortest_path[-1]
    ax.plot(end_point.x, end_point.y, marker='o', markersize=5, color='blue')

    # Set plot properties
    ax.set_aspect('equal', 'box')
    ax.autoscale()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Shortest Path')
    plt.show()

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

def update_visibility_graph(g, new_obstacles):
    for obstacle in new_obstacles:
        g.update(obstacle.vertices)

if __name__ == "__main__":
    # Example input (replace with provided input)
    obstacles = read_obstacles_from_file('obstacles.txt')

    start_point = vg.Point(211, 10)
    end_point = vg.Point(407, 445)

    # Convert ObstaclePolygon objects to polygons
    polygons = [obstacle.vertices for obstacle in obstacles]

    # Construct visibility graph
    g = vg.VisGraph()
    g.build(polygons)

    # Compute shortest path
    shortest_path = compute_shortest_path(g,polygons, start_point, end_point)

    # Display obstacles
    #plot_polygons(obstacles)

    # Display shortest path
    plot_shortest_path(obstacles, shortest_path)


    # New obstacles added after creation of visibility graph
    new_obstacles = read_obstacles_from_file('new_obstacle.txt')

    #updating polygon list
    polygons=polygons + [o.vertices for o in new_obstacles]

    #updating obstacles list
    obstacles=obstacles + new_obstacles

    # Update the visibility graph with new obstacles
    #update_visibility_graph(g, obstacles)

    g = vg.VisGraph()
    g.build(polygons)

    start_point = vg.Point(211, 10)
    end_point = vg.Point(407, 445)

    # Recompute shortest path
    shortest_path = compute_shortest_path(g,polygons, start_point, end_point)

    # Display updated obstacles
    #plot_polygons(obstacles)

    # Display updated shortest path
    plot_shortest_path(obstacles + new_obstacles, shortest_path)
