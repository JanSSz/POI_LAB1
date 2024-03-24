import numpy as np

#a.płaskiej poziomej powierzchni o ograniczonej szerokości i długości
def generate_3d_point_cloud(filename, width, length, num_points):

    # Generowanie losowych współrzędnych x, y, z
    x = np.random.uniform(0, width, num_points)
    y = np.random.uniform(0, length, num_points)
    z = np.zeros(num_points)  #płaska pozioma powierzchnia

    # łączeniówka (w 1 tablice)
    point_cloud = np.column_stack((x, y, z))
    np.savetxt(filename, point_cloud, fmt='%f', delimiter=' ')
    return point_cloud

# wybór zmiennych
filename = 'point_cloud_1.xyz'
width = 10.0  # Szerokość płaszczyzny
length = 15.0  # Długość płaszczyzny
num_points =2000  # Liczba punktów do wygenerowania
#generowanie punktow
point_cloud = generate_3d_point_cloud(filename, width, length, num_points)
print(point_cloud)

#b.płaskiej pionowej powierzchni o ograniczonej szerokości i wysokości
def generate_3d_point_cloud_vertical(filename_2, width_2, height_2, length_2, num_points_2):
    x_2 = np.random.uniform(0, width_2, num_points_2)
    y_2 = np.random.uniform(0, height_2, num_points_2)
    z_2 = np.random.uniform(0, length_2, num_points_2)
    point_cloud_2 = np.column_stack((x_2, y_2, z_2))

    np.savetxt(filename_2, point_cloud_2, fmt='%f', delimiter=' ')
    return point_cloud_2


filename_2 = 'point_cloud_2.xyz'
width_2 = 10.0  # Szerokość płaszczyzny
height_2 = 15.0  # Wysokość płaszczyzny
length_2 = 20.0  # Długość płaszczyzny
num_points_2 =2000 # Liczba punktów do wygenerowania

point_cloud_2 = generate_3d_point_cloud_vertical(filename_2, width_2, height_2, length_2, num_points_2)
print(point_cloud_2)

#c.powierzchni cylindrycznej o zadanym promieniu i ograniczonej wysokości
def generate_3d_point_cloud_cylindrical(filename_3, radius, height_3, num_points_3):
    # Generowanie losowych kątów w zakresie od 0 do 2*pi dla współrzędnej x i y
    theta = np.random.uniform(0, 2 * np.pi, num_points_3)

    # Generowanie losowych wysokości punktów w zakresie od 0 do height
    z_3 = np.random.uniform(0, height_3, num_points_3)

    # Obliczanie współrzędnych x i y na podstawie kąta i promienia
    x_3 = radius * np.cos(theta)
    y_3 = radius * np.sin(theta)

    point_cloud_3 = np.column_stack((x_3, y_3, z_3))
    np.savetxt(filename_3, point_cloud_3, fmt='%f', delimiter=' ')
    return point_cloud_3





filename_3 = 'point_cloud_3.xyz'
radius = 5.0  # Promień cylindra
height_3 = 10.0  # Wysokość cylindra
num_points_3 = 2000  # Liczba punktów do wygenerowania

point_cloud_3 = generate_3d_point_cloud_cylindrical(filename_3, radius, height_3, num_points_3)
print(point_cloud_3)