import matplotlib.pyplot as plt
#pip install matplotlib

x1 = [2, 4, 6]
y1 = [1, 5, 8]
x2 = [5, 6, 2]
y2 = [1, 3, 6]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot data on the first subplot
ax1.plot(x1, y1, label='Line 1', color='blue', linestyle='dashed', marker='o')
ax1.set_xlabel('X-AXIS')
ax1.set_ylabel('Y-AXIS')
ax1.set_title("Graph 1")
ax1.grid(True)
ax1.legend(loc='upper left', fontsize='medium')

# Add annotations to specific points
for i, (x, y) in enumerate(zip(x1, y1)):
    ax1.annotate(f'({x},{y})', (x, y), textcoords="offset points", xytext=(-10, 5), ha='center')

# Plot data on the second subplot
ax2.plot(x2, y2, label='Line 2', color='green', linestyle='dashdot', marker='s')
ax2.set_xlabel('X-AXIS')
ax2.set_ylabel('Y-AXIS')
ax2.set_title("Graph 2")
ax2.grid(True)
ax2.legend(loc='upper left', fontsize='medium')

# Adjust plot limits for the second subplot
ax2.set_xlim(0, 7)
ax2.set_ylim(0, 7)

# Save the whole figure as an image
figure_filename = 'subplots.png'
plt.savefig(figure_filename)
print(f"Subplots saved as {figure_filename}")

# Show the subplots
plt.tight_layout()
plt.show()
