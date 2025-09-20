import matplotlib.pyplot as plt

def visualize(result, chart_type="bar", output_path="assets/chart.png"):
    if hasattr(result, "plot"):
        result.plot(kind=chart_type)
        plt.savefig(output_path)
        plt.close()
        return output_path
    return None
