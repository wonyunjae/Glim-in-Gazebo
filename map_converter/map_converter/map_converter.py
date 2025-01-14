import numpy as np
from pcl_helper import pcl_to_ros
from nav_msgs.msg import OccupancyGrid

def pointcloud_to_occupancy_grid(cloud, resolution=0.05):
    # 포인트 클라우드를 2D 그리드로 투영
    x_points = cloud[:, 0]
    y_points = cloud[:, 1]
    z_points = cloud[:, 2]
    
    # 바닥에서 일정 높이 범위 내의 포인트만 사용
    mask = (z_points > 0.0) & (z_points < 1.7)  # 예: 10cm~50cm 높이
    
    # 그리드 맵 생성
    x_min, x_max = np.min(x_points), np.max(x_points)
    y_min, y_max = np.min(y_points), np.max(y_points)
    
    grid_size_x = int((x_max - x_min) / resolution)
    grid_size_y = int((y_max - y_min) / resolution)
    
    grid = np.zeros((grid_size_x, grid_size_y))
    
    # 포인트를 그리드에 투영
    for x, y in zip(x_points[mask], y_points[mask]):
        grid_x = int((x - x_min) / resolution)
        grid_y = int((y - y_min) / resolution)
        if 0 <= grid_x < grid_size_x and 0 <= grid_y < grid_size_y:
            grid[grid_x, grid_y] = 100  # 장애물 표시
            # 장애물 주변에 팽창 효과 적용
            kernel_size = 3
            half_kernel = kernel_size // 2
            for i in range(max(0, grid_x - half_kernel), min(grid_size_x, grid_x + half_kernel + 1)):
                for j in range(max(0, grid_y - half_kernel), min(grid_size_y, grid_y + half_kernel + 1)):
                    if grid[i, j] == 0:  # 빈 공간인 경우에만
                        grid[i, j] = 50  # 장애물 주변 영역 표시
