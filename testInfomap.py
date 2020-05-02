from infomap import Infomap

# Command line flags can be added as a string to Infomap
im = Infomap("--two-level --directed")

# Add weight as optional third argument
im.add_link(0, 1)
im.add_link(0, 2)
im.add_link(0, 3)
im.add_link(1, 0)
im.add_link(1, 2)
im.add_link(2, 1)
im.add_link(2, 0)
im.add_link(3, 0)
im.add_link(3, 4)
im.add_link(3, 5)
im.add_link(4, 3)
im.add_link(4, 5)
im.add_link(5, 4)
im.add_link(5, 3)

# Run the Infomap search algorithm to find optimal modules
im.run()

print(f"Found {im.num_top_modules} modules with codelength: {im.codelength}")

print("Result")
print("\n#node module")
for node in im.tree:
    if node.is_leaf:
        print(node.node_id, node.module_id)