import os

def print_directory_tree(root_dir, prefix=""):
    """
    주어진 디렉토리의 트리 구조를 출력합니다.
    
    Args:
        root_dir (str): 출력할 루트 디렉토리 경로
        prefix (str): 현재 줄에 사용할 접두사
    """
    # 디렉토리 내 모든 항목 가져오기
    items = sorted(os.listdir(root_dir))
    
    # 각 항목에 대해 처리
    for i, item in enumerate(items):
        # 전체 경로 생성
        path = os.path.join(root_dir, item)
        
        # 마지막 항목인지 확인
        is_last = i == len(items) - 1
        
        # 적절한 분기 기호 선택
        if is_last:
            branch = "└── "
            new_prefix = prefix + "    "
        else:
            branch = "├── "
            new_prefix = prefix + "│   "
        
        # 항목 출력 (디렉토리인 경우 이름 뒤에 / 추가)
        if os.path.isdir(path):
            print(f"{prefix}{branch}{item}/")
            # 재귀적으로 하위 디렉토리 출력
            print_directory_tree(path, new_prefix)
        else:
            print(f"{prefix}{branch}{item}")

def main():
    """
    현재 디렉토리 구조를 렌더링합니다.
    """
    root_dir = "."  # 현재 디렉토리를 기준으로
    print(f"{os.path.basename(os.path.abspath(root_dir))}/")
    print_directory_tree(root_dir)

if __name__ == "__main__":
    main()