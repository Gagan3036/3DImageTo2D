import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt

def load_3d_image(file_path):
    # Load 3D image (point cloud data) using PyVista
    mesh = pv.read(file_path)
    return mesh

def preprocess_point_cloud(mesh):
    # Preprocess the point cloud (e.g., downsampling)
    mesh = mesh.decimate_pro(0.5)  # Reduce to 50% of the original points
    return mesh

def project_to_2d(mesh):
    # Extract points from the mesh
    points = mesh.points
    # Project 3D points to 2D by discarding the Z coordinate
    points_2d = points[:, :2]
    return points_2d

def render_floor_plan(points_2d):
    # Render 2D floor plan using Matplotlib
    plt.scatter(points_2d[:, 0], points_2d[:, 1], s=1)
    plt.title('2D Floor Plan')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.show()

def main(file_path):
    mesh = load_3d_image(file_path)
    mesh = preprocess_point_cloud(mesh)
    points_2d = project_to_2d(mesh)
    render_floor_plan(points_2d)

if __name__ == "__main__":
    # Replace with your 3D image file path
    file_path = r"C:\Users\gagan\Desktop\3DImageTo2D\Axle shaft.ply"
    main(file_path)
