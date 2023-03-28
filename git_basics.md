## 1. git 시작하기

- git 저장소 생성
  - `git init`
  - 숨김 파일 .git 에 버전 정보 저장됨

- 사용자 등록 (최초 커밋 전 필요)
  - `git config --global user.name <name>`
  - `git config --global user.email <email@email.com>`
  - `git config --global -l` : 등록된 사용자 확인

- 커밋
  - `git commit -m <message>`
  - staging area의 모든 내용 깃 저장소에 업데이트 with 메세지
  - staging area 비어 있으면 commit 할 내용 없음
  - `git add`
  - 커밋할 내용 일단 저장(staging area)
    - `git add .`
    - 현 위치 모든 파일 staging area에 저장

- 구조
  - 실제 폴더
    - 파일 저장되어 있음
  - 로컬 git 저장소
    - working directory
      - 커밋하면 여기에 저장되어 변경사항 추적, 관리
    - commits
      - 커밋한 기록과 메세지 저장됨
    - staging area 
      - 커밋할 내용 임시 저장
      - 커밋하면 여기의 내용이 우선 working directory에 저장
      - `git restore --staged <file>` : staged된 파일 취소

- 상태 확인
  - `git status`
  - 마지막 커밋 이후 변경사항 있는지 확인
  - No commits yet : staging area 비어있음
  - Changes not staged for commit : 파일의 변경사항 있지만 staging area에 저장 안됨
    - modfied : 파일명
  - Untracked files : 깃에서 변경사항을 추적하지 못하고 있는 파일
    - add 필요

- 로그 확인
  - `git log`
  - 현 저장소의 변경사항 모두 출력
  - q로 종료
  - `git log --oneline` : 주요 내용만 출력

</br>

## 2. github 연동

- 깃허브 연동
  - `git remote add origin <깃허브 저장소 주소>`
    - 원격 저장소 연결 별명(alias) origin
  - `git remote -v`
    - 원격으로 연결한 저장소 확인
  - `git push origin master`
    - 원격 git의 origin 브랜치에 로컬 git의 master 브랜치 동기화
  - readme 추가 (로컬에서 해서 업로드하는게 나음)
  - 하나의 github repo에는 하나의 로컬 git 만 대응 가능
      - 하나의 로컬 git은 여러 github repo에 연결 가능(origin 대신 다른 이름으로 연결)
  
- 로컬에서 작업하고 github 업로드하는 흐름  
  1. 로컬에서 작업, 저장
  2. `git add .` : 로컬 git의 staging area에 add
  3. `git commit -m <message>` : 로컬 git에 commit
  4. `git push origin master` : github에 업로드
      - `git push -u origin master` 한번 했으면 이후에는 `git push`만 해도 됨
      - -u : local의 master라는 브랜치를 github의 origin repo의 master 브랜치에 연결

- github 저장소 로컬로 가져오기
  - `git clone <github repo 주소> <clone할 경로(생략 가능)>`
    - clone할 경로 생략하면 현 경로에 github repo명과 같은 폴더가 생성됨
    - 현 경로 자체에 clone하려면 경로 . 
    - 해당 폴더는 github repo와 연결되어 있음 (git remote -v 로 확인)
  - 로컬 git A -> github A1 -> 로컬 git A2 인 상태
  - `git pull origin master`
    - A2에서 A1로 커밋, 푸쉬 한 후
    - A에서 해당 명령어 입력하면 A, A1, A2 모두 동기화 됨
    - git log로 확인하면 A, A2 동일함

- 커밋 메세지 수정
  - `git commit --amend`
    - 되도록 push 전에
  - vim 에디터 나옴
    - i 입력 -> 편집 모드
    - 커밋 메세지 수정 후 esc
    - :wq(+enter) -> 저장 후 종료
  - git commit -m 다음에 message 안 남기면 vim 창에서 입력

- git으로 관리하지 않을 파일 설정
  - git init 직후에 설정해야 함
  - `touch .gitignore` -> 숨김 파일로 생성(ls -a 로 확인 가능)
  - `start .gitignore`로 실행(메모장)
  - git으로 관리하지 않을 파일명 입력하고 저장 (폴더도 가능)
  - git status로 확인
  - [gitignore.io](gitignore.io) 에서 운영체제, 언어 등에 맞춘 .ignore 파일 생성 가능

</br>

## 3. 서로 다른 로컬 git에서 github로 푸쉬했을 때

- 별 문제 없는 경우 (conflict 없음)
  - 나중의 push에 문제 생김
  - 나중에 push한 로컬에서 pull하면 merge 하겠냐는 vim 창 나옴
  - :wq로 종료하면 자연스럽게 merge
  - `git log --oneline --graph`로 commit이 어떻게 갈라졌는지 확인
  - 이후 다시 pull, 다른 로컬에서 push 하면 동기화 완료

- 같은 파일을 다른 로컬에서 수정한 경우 (conflict)
  - 나중 push에 문제 생김
  - pull 하면 결과 메세지에 'Auto-merging'이라고 뜸
  - git status 찍어보면 현 브랜치가 master|MERGING
  - conflict 발생한 파일 `code .`으로 vs code에서 확인
  - 수정 내역 비교하고 반영할 것 선택 -> 저장
  - add -> commit -> push
  - 다른 로컬에서 pull로 받아와서 동기화


- 코랩에서 깃허브 업로드
  - 파일 - GitHub 사본 저장
  - 저장소, commit 메세지 설정
  - 이후 로컬에서 다시 pull까지


## GitHub 특강

- commit하면 Git은 현 staging area에 있는 데이터의 스냅샷 저장

- head vs master
  - head는 현재의 commit을 참조, 기본적으로 master를 참조
  - master는 branch의 마지막 commit을 참조
  
- checkout은 head를 바꿈
  - `git checkout commit_id`
    - head가 해당 commit을 참조
  - `git checkout master`
    - master가 head를 참조하게 변경
