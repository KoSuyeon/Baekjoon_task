def coordinate_compression(coords):
    # 좌표를 값과 원래 인덱스와 함께 저장
    indexed_coords = list(enumerate(coords))
    sorted_coords = sorted(indexed_coords, key=lambda x: x[1])
    
    compressed = {}
    current_rank = 0
    # 압축 좌표 매핑 생성
    for i, (index, value) in enumerate(sorted_coords):
        if i == 0 or sorted_coords[i-1][1] != value:
            compressed[value] = current_rank
            current_rank += 1

    result = [compressed[coords[i]] for i in range(len(coords))]
    return result


N = int(input())
coords = list(map(int, input().split()))
compressed_coords = coordinate_compression(coords)
print(' '.join(map(str, compressed_coords)))

"""
def compress_coordinates(coords):
    # 좌표를 정렬하여 고유한 순위를 부여
    sorted_c = sorted(set(coords))
    # 좌표와 그 압축된 인덱스를 매핑
    compress_map = {value: idx for idx, value in enumerate(sorted_c)}
    # 원래 좌표에 매핑된 인덱스로 반환
    return [compress_map[x] for x in coords]
"""
