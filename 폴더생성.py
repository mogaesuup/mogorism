import os
import shutil
from pathlib import Path

def create_directories(base_dir):
    """새로운 디렉토리 구조 생성"""
    new_structure = [
        "템플릿/python/01_기초",
        "템플릿/python/02_자료구조/배열", "템플릿/python/02_자료구조/연결리스트", 
        "템플릿/python/02_자료구조/스택", "템플릿/python/02_자료구조/큐와덱",
        "템플릿/python/02_자료구조/해시", "템플릿/python/02_자료구조/행렬",
        "템플릿/python/03_정렬",
        "템플릿/python/04_탐색/완전탐색/순열", "템플릿/python/04_탐색/완전탐색/조합", "템플릿/python/04_탐색/완전탐색/부분집합",
        "템플릿/python/04_탐색/이진탐색", "템플릿/python/04_탐색/투포인터",
        "템플릿/python/05_그래프/그래프탐색", "템플릿/python/05_그래프/최단경로", 
        "템플릿/python/05_그래프/최소신장트리", "템플릿/python/05_그래프/위상정렬", "템플릿/python/05_그래프/유니온파인드",
        "템플릿/python/06_트리/트리기본", "템플릿/python/06_트리/이진트리", "템플릿/python/06_트리/LCA",
        "템플릿/python/06_트리/세그먼트트리", "템플릿/python/06_트리/펜윅트리", "템플릿/python/06_트리/트라이",
        "템플릿/python/07_동적계획법/기본DP", "템플릿/python/07_동적계획법/LIS", "템플릿/python/07_동적계획법/트리DP",
        "템플릿/python/08_문자열/문자열기본", "템플릿/python/08_문자열/KMP", 
        "템플릿/python/08_문자열/라빈카프", "템플릿/python/08_문자열/아호코라식", "템플릿/python/08_문자열/기타",
        "템플릿/python/09_기하/CCW", "템플릿/python/09_기하/볼록껍질", "템플릿/python/09_기하/선형스위핑",
        "템플릿/python/10_고급/네트워크플로우/네트워크", "템플릿/python/10_고급/네트워크플로우/MCMF", 
        "템플릿/python/10_고급/네트워크플로우/이분매칭", "템플릿/python/10_고급/Lazy", 
        "템플릿/python/10_고급/SCC", "템플릿/python/10_고급/수학고급",
        "템플릿/python/11_게임이론/돌게임",
        "템플릿/cpp", "템플릿/java", "템플릿/javascript"
    ]
    
    for directory in new_structure:
        Path(os.path.join(base_dir, directory)).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def map_old_to_new():
    """기존 경로를 새 경로로 매핑"""
    mapping = {
        # 자료구조
        "템플릿/python/배열/배열모양": "템플릿/python/02_자료구조/배열",
        "템플릿/python/배열/배열회전": "템플릿/python/02_자료구조/배열",
        "템플릿/python/자료구조/연결리스트": "템플릿/python/02_자료구조/연결리스트",
        "템플릿/python/자료구조/스택": "템플릿/python/02_자료구조/스택",
        "템플릿/python/문자열/괄호": "템플릿/python/02_자료구조/스택",  # 괄호는 주로 스택으로 풀어서
        "템플릿/python/자료구조/해시": "템플릿/python/02_자료구조/해시",
        "템플릿/python/자료구조/행렬": "템플릿/python/02_자료구조/행렬",
        
        # 정렬
        "템플릿/python/정렬": "템플릿/python/03_정렬",
        
        # 탐색
        "템플릿/python/경우의수/순열": "템플릿/python/04_탐색/완전탐색/순열",
        "템플릿/python/경우의수/조합": "템플릿/python/04_탐색/완전탐색/조합",
        "템플릿/python/경우의수/부분집합": "템플릿/python/04_탐색/완전탐색/부분집합",
        "템플릿/python/이분탐색": "템플릿/python/04_탐색/이진탐색",
        "템플릿/python/트리/이진탐색": "템플릿/python/04_탐색/이진탐색",
        "템플릿/python/투포인터": "템플릿/python/04_탐색/투포인터",
        
        # 그래프
        "템플릿/python/DFS_BFS": "템플릿/python/05_그래프/그래프탐색",
        "템플릿/python/다익스트라": "템플릿/python/05_그래프/최단경로",
        "템플릿/python/벨만포드": "템플릿/python/05_그래프/최단경로",
        "템플릿/python/SPFA": "템플릿/python/05_그래프/최단경로",
        "템플릿/python/플로이드와셜": "템플릿/python/05_그래프/최단경로",
        "템플릿/python/트리/크루스칼": "템플릿/python/05_그래프/최소신장트리",
        "템플릿/python/트리/프림": "템플릿/python/05_그래프/최소신장트리",
        "템플릿/python/DAG": "템플릿/python/05_그래프/위상정렬",
        "템플릿/python/유니온파인드": "템플릿/python/05_그래프/유니온파인드",
        
        # 트리
        "템플릿/python/트리/트리기본": "템플릿/python/06_트리/트리기본",
        "템플릿/python/트리/이진트리": "템플릿/python/06_트리/이진트리",
        "템플릿/python/트리/LCA": "템플릿/python/06_트리/LCA",
        "템플릿/python/문자열/LCA": "템플릿/python/06_트리/LCA",
        "템플릿/python/트리/세그먼트트리": "템플릿/python/06_트리/세그먼트트리",
        "템플릿/python/트리/펜윅트리": "템플릿/python/06_트리/펜윅트리",
        "템플릿/python/트리/trie": "템플릿/python/06_트리/트라이",
        
        # 동적계획법
        "템플릿/python/DP/LIS": "템플릿/python/07_동적계획법/LIS",
        "템플릿/python/DP/트리DP": "템플릿/python/07_동적계획법/트리DP",
        
        # 문자열
        "템플릿/python/문자열/27866_문자와_문자열_py": "템플릿/python/08_문자열/문자열기본",
        "템플릿/python/문자열/27866_문자와_문자열_js": "템플릿/javascript/08_문자열/문자열기본",
        "템플릿/python/문자열/KMP": "템플릿/python/08_문자열/KMP",
        "템플릿/python/문자열/rabin_karp": "템플릿/python/08_문자열/라빈카프",
        "템플릿/python/문자열/aho_corasick": "템플릿/python/08_문자열/아호코라식",
        "템플릿/python/문자열/manacher.py": "템플릿/python/08_문자열/기타/manacher.py",
        "템플릿/python/문자열/접미사배열2.py": "템플릿/python/08_문자열/기타/접미사배열2.py",
        
        # 기하
        "템플릿/python/기하/ccw": "템플릿/python/09_기하/CCW",
        "템플릿/python/기하/convex_hull": "템플릿/python/09_기하/볼록껍질",
        "템플릿/python/기하/line_sweeping": "템플릿/python/09_기하/선형스위핑",
        "템플릿/python/기하/캘리퍼스": "템플릿/python/09_기하/선형스위핑",
        
        # 고급
        "템플릿/python/네트워크플로우/네트워크": "템플릿/python/10_고급/네트워크플로우/네트워크",
        "템플릿/python/네트워크플로우/MCMF": "템플릿/python/10_고급/네트워크플로우/MCMF",
        "템플릿/python/네트워크플로우/이분매칭": "템플릿/python/10_고급/네트워크플로우/이분매칭",
        "템플릿/python/트리/Lazy": "템플릿/python/10_고급/Lazy",
        "템플릿/python/트리/코사라주": "템플릿/python/10_고급/SCC",
        "템플릿/python/fft": "템플릿/python/10_고급/수학고급",
        
        # 게임이론
        "템플릿/python/돌게임": "템플릿/python/11_게임이론/돌게임",
        
        # 기타
        "템플릿/python/분할정복": "템플릿/python/04_탐색/이진탐색",
        "템플릿/python/비트마스킹": "템플릿/python/04_탐색/완전탐색/부분집합"
    }
    return mapping

def copy_files(base_dir, mapping):
    """파일을 새 구조로 복사"""
    for old_path, new_path in mapping.items():
        old_dir = os.path.join(base_dir, old_path)
        new_dir = os.path.join(base_dir, new_path)
        
        if not os.path.exists(old_dir):
            print(f"Warning: Source directory doesn't exist: {old_dir}")
            continue
            
        # 디렉토리가 파일이면 파일 복사
        if old_path.endswith('.py'):
            os.makedirs(os.path.dirname(new_dir), exist_ok=True)
            try:
                shutil.copy2(old_dir, new_dir)
                print(f"Copied file: {old_dir} -> {new_dir}")
            except Exception as e:
                print(f"Error copying file {old_dir}: {e}")
        else:
            # 디렉토리 내 모든 파일 복사
            try:
                for item in os.listdir(old_dir):
                    src_item = os.path.join(old_dir, item)
                    dst_item = os.path.join(new_dir, item)
                    
                    if os.path.isfile(src_item):
                        if not os.path.exists(new_dir):
                            os.makedirs(new_dir)
                        
                        # .vscode 폴더 내용은 복사하지 않음
                        if '.vscode' not in src_item:
                            shutil.copy2(src_item, dst_item)
                            print(f"Copied file: {src_item} -> {dst_item}")
            except Exception as e:
                print(f"Error copying directory {old_dir}: {e}")

def main():
    # 현재 작업 디렉토리를 기준으로 경로 설정
    base_dir = os.getcwd()
    
    print("Step 1: Creating new directory structure...")
    create_directories(base_dir)
    
    print("\nStep 2: Mapping old directories to new structure...")
    mapping = map_old_to_new()
    
    print("\nStep 3: Copying files to new structure...")
    copy_files(base_dir, mapping)
    
    print("\nMigration completed!")
    print("Note: The original files have not been deleted. Once you verify everything is correct, you can delete them manually.")

if __name__ == "__main__":
    main()