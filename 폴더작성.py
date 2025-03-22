import os

# 초보반 챕터 정보
beginners_chapters = [
    {"week": 1, "date": "2025-03-25", "title": "심화 1", "chapter": 6},
    {"week": 2, "date": "2025-04-01", "title": "2차원 배열", "chapter": 7},
    {"week": 3, "date": "2025-04-08", "title": "일반 수학 1", "chapter": 8},
    {"week": 4, "date": "2025-04-15", "title": "약수, 배수와 소수", "chapter": 9},
    {"week": 5, "date": "2025-04-22", "title": "기하: 직사각형과 삼각형", "chapter": 10},
    {"week": 6, "date": "2025-04-29", "title": "시간 복잡도", "chapter": 11},
    {"week": 7, "date": "2025-05-06", "title": "브루트 포스", "chapter": 12},
    {"week": 8, "date": "2025-05-13", "title": "정렬", "chapter": 13},
    {"week": 9, "date": "2025-05-20", "title": "집합과 맵", "chapter": 14},
    {"week": 10, "date": "2025-05-27", "title": "약수, 배수와 소수 2", "chapter": 15},
    {"week": 11, "date": "2025-06-03", "title": "스택, 큐, 덱", "chapter": 16},
    {"week": 12, "date": "2025-06-10", "title": "조합론", "chapter": 19},
    {"week": 13, "date": "2025-06-17", "title": "심화 2", "chapter": 20},
    {"week": 14, "date": "2025-06-24", "title": "재귀", "chapter": 21},
    {"week": 15, "date": "2025-07-01", "title": "백트래킹", "chapter": 22},
    {"week": 16, "date": "2025-07-08", "title": "동적 계획법 1", "chapter": 23},
    {"week": 17, "date": "2025-07-15", "title": "누적 합", "chapter": 24},
    {"week": 18, "date": "2025-07-22", "title": "그리디 알고리즘", "chapter": 25},
    {"week": 19, "date": "2025-07-29", "title": "분할 정복", "chapter": 26},
    {"week": 20, "date": "2025-08-05", "title": "이분 탐색", "chapter": 27},
    {"week": 21, "date": "2025-08-12", "title": "우선순위 큐", "chapter": 28},
    {"week": 22, "date": "2025-08-19", "title": "동적 계획법 2", "chapter": 29},
    {"week": 23, "date": "2025-08-26", "title": "스택 2", "chapter": 30},
    {"week": 24, "date": "2025-09-02", "title": "그래프와 순회", "chapter": 31},
    {"week": 25, "date": "2025-09-09", "title": "최단 경로", "chapter": 32}
]

# 고수반 챕터 정보 - 중복 제거
advanced_chapters = [
    {"week": 1, "date": "2025-03-25", "title": "유니온 파인드", "chapter": 36},
    {"week": 2, "date": "2025-04-01", "title": "최소 신장 트리", "chapter": 37},
    {"week": 3, "date": "2025-04-08", "title": "트리에서의 동적 계획법", "chapter": 38},
    {"week": 4, "date": "2025-04-15", "title": "기하 2", "chapter": 39},
    {"week": 6, "date": "2025-04-29", "title": "동적 계획법 3", "chapter": 40},
    {"week": 8, "date": "2025-05-13", "title": "문자열 알고리즘 1", "chapter": 41},
    {"week": 10, "date": "2025-05-27", "title": "위상 정렬", "chapter": 42},
    {"week": 11, "date": "2025-06-03", "title": "최소 공통 조상", "chapter": 43},
    {"week": 12, "date": "2025-06-10", "title": "강한 연결 요소", "chapter": 44},
    {"week": 13, "date": "2025-06-17", "title": "세그먼트 트리", "chapter": 45},
    {"week": 15, "date": "2025-07-01", "title": "스위핑", "chapter": 46},
    {"week": 16, "date": "2025-07-08", "title": "동적 계획법 4", "chapter": 47},
    {"week": 18, "date": "2025-07-22", "title": "컨벡스 헐", "chapter": 48},
    {"week": 19, "date": "2025-07-29", "title": "이분 매칭", "chapter": 49},
    {"week": 20, "date": "2025-08-05", "title": "네트워크 플로우", "chapter": 50},
    {"week": 22, "date": "2025-08-19", "title": "MCMF", "chapter": 51},
    {"week": 23, "date": "2025-08-26", "title": "어려운 구간 쿼리", "chapter": 52},
    {"week": 25, "date": "2025-09-09", "title": "더 어려운 수학", "chapter": 53}
]

def sanitize_filename(name):
    """파일 이름에 사용할 수 없는 문자 치환"""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name

def create_chapter_folders():
    """챕터별 폴더 생성"""
    # 기본 디렉토리
    os.makedirs("초보반", exist_ok=True)
    os.makedirs("고수반", exist_ok=True)
    os.makedirs("템플릿", exist_ok=True)
    
    # 초보반 챕터 폴더 생성
    for chapter in beginners_chapters:
        folder_name = f"{chapter['chapter']}_{sanitize_filename(chapter['title'])}"
        folder_path = os.path.join("초보반", folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"초보반 챕터 폴더 생성: {folder_name}")
    
    # 고수반 챕터 폴더 생성
    for chapter in advanced_chapters:
        folder_name = f"{chapter['chapter']}_{sanitize_filename(chapter['title'])}"
        folder_path = os.path.join("고수반", folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"고수반 챕터 폴더 생성: {folder_name}")

# 프로그램 실행
if __name__ == "__main__":
    create_chapter_folders()
    print("모든 챕터 폴더가 성공적으로 생성되었습니다!")