import matplotlib.pyplot as plt

def create_simple_graph():
    # Example data
    categories = ['Category A', 'Category B', 'Category C']
    values = [10, 15, 5]

    # Create a bar graph
    plt.bar(categories, values, color='blue')

    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Simple Bar Graph')

    # Show the graph
    plt.show()

if __name__ == "__main__":
    create_simple_graph()
