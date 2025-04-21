# 러스트 알고리즘 템플릿 사용법

## 로컬에서 실행

```bash
cd 템플릿/rust
cargo run --bin line_intersection
```

## 백준 제출 방법

1. 로컬 테스트용 코드를 주석 처리합니다:
```rust
// 로컬 테스트는 아래 주석 해제 (백준 제출 시 주석 처리)
// std::fs::File::open("geometry/input.txt").map(|f| std::io::BufReader::new(f).lines());
```

2. 코드를 백준에 그대로 복사/붙여넣기하세요.

## 새 알고리즘 추가

1. 새 `.rs` 파일을 해당 카테고리 폴더에 추가
2. `Cargo.toml`에 다음 항목 추가:

```toml
[[bin]]
name = "알고리즘명" 
path = "카테고리/파일명.rs"
``` 