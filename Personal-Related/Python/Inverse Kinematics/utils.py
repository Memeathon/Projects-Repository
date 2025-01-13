import math

def get_rect_corners(start, end, width):
    # Calculate the angle of the line from start to end
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)  # angle in radians
    print("atan2:", math.degrees(angle))

    # Half width for each side of the line
    half_width = width / 2

    # Perpendicular angle for the width
    perp_angle = angle + math.pi / 2

    # Compute offsets from the line center for the width
    offset_x = half_width * math.cos(perp_angle)
    offset_y = half_width * math.sin(perp_angle)

    # Define four corners of the rectangle
    top_left = (start[0] - offset_x, start[1] - offset_y)
    top_right = (end[0] - offset_x, end[1] - offset_y)
    bottom_right = (end[0] + offset_x, end[1] + offset_y)
    bottom_left = (start[0] + offset_x, start[1] + offset_y)

    return [top_left, top_right, bottom_right, bottom_left]

def getKneeJointCoords(root, endpoint, UPPER_LEG_LENGTH, LOWER_LEG_LENGTH, natural = True):
    HipToAnkleDistance = math.sqrt((endpoint[0]-root[0])**2 + (endpoint[1]-root[1])**2)
    HipRad = math.acos(max(-1, min(1, ((UPPER_LEG_LENGTH**2 + HipToAnkleDistance**2 - LOWER_LEG_LENGTH**2) / (2 * UPPER_LEG_LENGTH * HipToAnkleDistance)))))
    HipTheta = math.atan2(endpoint[1] - root[1], endpoint[0] - root[0])

    print(HipTheta)

    CounterClockwiseKnee = (root[0] + UPPER_LEG_LENGTH * math.cos(HipTheta + HipRad), root[1] + UPPER_LEG_LENGTH * math.sin(HipTheta + HipRad))
    ClockwiseKnee = (root[0] + UPPER_LEG_LENGTH * math.cos(HipTheta - HipRad), root[1] + UPPER_LEG_LENGTH * math.sin(HipTheta - HipRad))
    return CounterClockwiseKnee, ClockwiseKnee