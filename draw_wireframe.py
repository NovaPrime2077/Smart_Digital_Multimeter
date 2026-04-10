import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# make dir
os.makedirs('docs', exist_ok=True)

# setup fig
fig, ax = plt.subplots(figsize=(4, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.axis('off')

# draw shell
case = patches.Rectangle((0.5, 0.5), 9, 19, fill=False, edgecolor='black', lw=3)
lcd = patches.Rectangle((1, 1.5), 8, 17, fill=True, color='#f8f9fa')
ax.add_patch(case)
ax.add_patch(lcd)

# draw title
ax.text(5, 17.5, 'smart digital multimeter', fontsize=14, fontweight='bold', ha='center')
ax.hlines(16.5, 1, 9, colors='black', lw=1)

# draw box
box = patches.Rectangle((1.5, 12), 7, 3, fill=True, color='#cce7ff', ec='#007bff', lw=2)
ax.add_patch(box)
ax.text(5, 13.5, '9.85 kΩ', fontsize=22, fontweight='bold', ha='center', color='black')

# draw tabs
ax.text(3, 10, 'R', fontsize=11, fontweight='bold', color='#007bff', ha='center')
ax.text(5, 10, 'C', fontsize=11, color='gray', ha='center')
ax.text(7, 10, 'L', fontsize=11, color='gray', ha='center')

# draw text
ax.text(5, 7.5, 'scale: 3\n(max: 10 kΩ)', fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=1, edgecolor='gray'))

# draw bot
ax.text(5, 4, 'connected', fontsize=10, ha='center', color='green')

# save pic
path = os.path.join('docs', 'app_wireframe.png')
plt.tight_layout()
plt.savefig(path, dpi=300)