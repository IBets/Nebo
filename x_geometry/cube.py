size = 0.5

cub_vertices = [
    -size, size, size,
    size, size, size,
    size, -size, size,
    -size, -size, size,

    size, size, -size,
    -size, size, -size,
    -size, -size, -size,
    size, -size, -size,

    -size, size, -size,
    size, size, -size,
    size, size, size,
    -size, size, size,

    size, -size, -size,
    -size, -size, -size,
    -size, -size, size,
    size, -size, size,

    -size, size, -size,
    -size, size, size,
    -size, -size, size,
    -size, -size, -size,

    size, size, size,
    size, size, -size,
    size, -size, -size,
    size, -size, size]

cub_tex_coord = [
    0.0, 1.0,
    1.0, 1.0,
    1.0, 0.0,
    0.0, 0.0,

    0.0, 1.0,
    1.0, 1.0,
    1.0, 0.0,
    0.0, 0.0,

    0.0, 1.0,
    1.0, 1.0,
    1.0, 0.0,
    0.0, 0.0,

    0.0, 1.0,
    1.0, 1.0,
    1.0, 0.0,
    0.0, 0.0,

    0.0, 1.0,
    1.0, 1.0,
    1.0, 0.0,
    0.0, 0.0,

    0.0, 1.0,
    1.0, 1.0,
    1.0, 0.0,
    0.0, 0.0]

cub_normal = [
    0.0, 0.0, 1.0,
    0.0, 0.0, 1.0,
    0.0, 0.0, 1.0,
    0.0, 0.0, 1.0,

    0.0, 0.0, -1.0,
    0.0, 0.0, -1.0,
    0.0, 0.0, -1.0,
    0.0, 0.0, -1.0,

    0.0, 1.0, 0.0,
    0.0, 1.0, 0.0,
    0.0, 1.0, 0.0,
    0.0, 1.0, 0.0,

    0.0, -1.0, 0.0,
    0.0, -1.0, 0.0,
    0.0, -1.0, 0.0,
    0.0, -1.0, 0.0,

    -1.0, 0.0, 0.0,
    -1.0, 0.0, 0.0,
    -1.0, 0.0, 0.0,
    -1.0, 0.0, 0.0,

    1.0, 0.0, 0.0,
    1.0, 0.0, 0.0,
    1.0, 0.0, 0.0,
    1.0, 0.0, 0.0]

cub_indices = [
    0, 3, 1, 1, 3, 2,
    4, 7, 5, 5, 7, 6,
    8, 11, 9, 9, 11, 10,
    12, 15, 13, 13, 15, 14,
    16, 19, 17, 17, 19, 18,
    20, 23, 21, 21, 23, 22]
