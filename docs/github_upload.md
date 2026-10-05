# GitHub 업로드 안내

압축을 풀고 jeonju-notebook-project 폴더에서 시작하세요.

## Git으로 올리기

GitHub에서 빈 저장소를 만든 후 아래 YOUR_NAME/YOUR_REPOSITORY를 본인 저장소로 바꾸세요.

```bash
git init
git add .
git commit -m "Add Jeonju recycling site selection analysis"
git branch -M main
git remote add origin https://github.com/YOUR_NAME/YOUR_REPOSITORY.git
git push -u origin main
```

## 웹에서 파일 올리기

README.md, requirements.txt, index.html, src/, notebooks/, data/processed/, results/, docs/를 올리세요. 발표 자료는 포함하지 않았습니다.
data/raw/의 데이터는 제외하세요. 웹 업로드는 .gitignore를 해석하지 않습니다.

## 다른 사람이 재실행하는 경우

저장소만 복제하면 raw 원본은 없으므로 실행에 필요한 원본을 추가로 배치해야 합니다.
이번 ZIP을 별도 다운로드 자료로 제공하면 압축 내부 data/raw/를 복사해 사용할 수 있습니다.
원본 목록과 출처는 data_sources.md를 참고하세요.
입력 자료의 배포 권한을 확인한 뒤 별도 다운로드 자료를 공개하세요.
