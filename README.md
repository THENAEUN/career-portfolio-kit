# Career Portfolio Kit

**첫 취업·이직·경력 전환을 준비하는 모든 지원자를 위한 공용 AI 스킬과 템플릿입니다.** 학생·신입부터 경력자까지, 실제 업무·프로젝트·연구 경험을 바탕으로 한·영 A4 이력서와 HTML·PDF 포트폴리오를 작성하고 JD에 맞춰 리뷰·수정합니다. 개발·로봇 분야에 한정하지 않으며 기획·디자인·마케팅·영업·운영 등 목표 직무에 맞게 근거와 구성을 선택합니다.

특정 개인의 경력 DB나 계정이 필요하지 않습니다. 본인의 경력 기록·기존 문서·작업 결과와 JD를 제공하면 됩니다. 개인 홈페이지·Markdown 블로그·프로젝트 README·기술 글·학술 포스터는 필요한 사람만 사용하는 추가 산출물입니다.

## 필요한 스킬 선택

| 하고 싶은 일 | 스킬 | 결과 |
|---|---|---|
| JD 기준을 세우고 작성물을 채점·검수한 뒤 2차 수정하기 | [jd-application-review](skills/jd-application-review/SKILL.md) | 고정 평가표·문서별 점수·인수조건·수정 전후 리뷰 + 갱신 HTML·PDF |
| 한·영 텍스트 중심 이력서를 만들고 PDF로 출력하기 | [html-a4-resume](skills/html-a4-resume/SKILL.md) | 한국어 HTML·PDF + 영어 HTML·PDF, 기본 4개 파일 |
| 업무·프로젝트와 본인 기여를 정리하고 첨삭받기 | [student-project-portfolio](skills/student-project-portfolio/SKILL.md) | 경험 설명·필요 시 README·보완 과제 |
| HTML로 포트폴리오를 만들고 PDF로 출력하기 | [html-pdf-portfolio](skills/html-pdf-portfolio/SKILL.md) | 회사·프로젝트별 성과 챕터의 편집 HTML + PDF, 제출 조건 우선 |
| 개인 커리어 홈페이지와 블로그를 개발하고 Vercel에 배포하기 | [career-homepage](skills/career-homepage/SKILL.md) | Next.js·React·Tailwind 반응형 사이트 + Markdown 글 + 무한스크롤 아카이브 + 배포 검증 |
| 학회 발표 형태의 A4 포스터 만들기 | [academic-a4-poster](skills/academic-a4-poster/SKILL.md) | 편집 HTML + A4 1페이지 PDF 초안 |

포스터 스킬은 Behance의 학술 포스터·타이포그래피 사례와 대학 도서관의 디자인 가이드를 참고했습니다. [레퍼런스와 확인 범위](skills/academic-a4-poster/references/design-and-references.md)를 기록했으며, 타인의 원본 이미지나 유료 템플릿은 포함하지 않습니다.

`student-project-portfolio`라는 폴더명은 기존 사용 문구와 링크 호환을 위해 유지합니다. 현재 지침은 경력자의 실무·사업·연구 경험도 다루며 학생 전용이라는 뜻은 아닙니다.

## 시작하기

1. GitHub의 **Code → Download ZIP** 또는 아래 명령으로 받습니다.

   ```bash
   git clone https://github.com/Jskim9536/career-portfolio-kit.git
   ```

2. Claude·Codex 등 파일을 읽고 편집할 수 있는 AI 에이전트에서 폴더를 열고, [시작 문구](START-HERE.md)로 필요한 `SKILL.md`와 연결된 참고 문서를 읽도록 요청합니다. 채팅만 사용하는 경우 해당 지침·템플릿을 첨부합니다. 폴더를 받았다고 전역 설치나 자동 로드가 되는 것은 아닙니다.
3. JD, 경력 기록, 기존 이력서·포트폴리오, 기획서·분석·운영 결과·디자인·연구·코드 등 본인 자료를 제공합니다. GitHub 계정이나 코드가 없는 직무도 사용할 수 있습니다. 공개할 수 없는 자료는 이 저장소에 올리지 않고 개인 작업 공간에서 사용합니다.
4. AI가 자료를 읽고 부족한 사실을 질문하면 답합니다. 없는 수치와 결과를 만들지 않습니다.
5. 문서 제작은 HTML을 브라우저에서 열고 수정한 뒤 PDF로 저장하고 출력도 확인합니다. 홈페이지 제작은 [웹사이트 시작 문구](START-HERE.md#개인-홈페이지와-markdown-블로그)를 사용해 별도 프로젝트에서 설치·개발·검증하고, 요청한 범위에서 Vercel로 배포합니다.

이 저장소를 받는 것만으로 전역 스킬이 설치되지는 않습니다. 설치 없이 파일의 지침을 읽도록 요청해 사용할 수 있습니다.

## JD 기준 → 작성 → 리뷰 → 2차 업데이트

JD가 있으면 이력서·포트폴리오 제작 전에 **필수요건·주요업무·우대사항별 배점과 인수조건**을 만들고 같은 지원 건에서 공유합니다. 초안을 만든 뒤 리뷰 스킬이 문서별 점수와 근거를 확인하고 제작 스킬을 적용해 v2 HTML·PDF를 다시 만듭니다. 수정 전후에는 같은 평가 기준을 사용합니다.

기본 배점은 필수요건 35, 주요업무 25, 우대사항 10, 개인 기여·결과 15, 전달력 10, 정보·구성 완결성 5점입니다. JD에 맞춰 작성 전에 조정하며, 기본 인수조건은 모든 문서 80점 이상·필수/주요업무 각각 75% 이상과 별도 자격·품질 게이트 충족입니다. **실제 합격 확률을 뜻하는 점수가 아닙니다.** 맞춤법·한영 일치·정본 사실 대조·기밀/개인정보·회사/직무·PDF 출력도 검수합니다. 명시 필수 자격 부족이나 확인하지 못한 사실은 높은 점수로 덮지 않습니다.

리뷰·근거표는 개인 QA 폴더에 두고, 지원 문서에는 평가 점수나 내부 피드백을 넣지 않습니다. 공개 키트에는 실제 지원자 자료를 올리지 않습니다. 산식·문서 범위·파일 해시를 검산하는 `score_review.py`는 표준 라이브러리만 사용하며, 내용 판단·기밀 탐지·시각 검수를 대신하지 않습니다. [기준 작성](skills/jd-application-review/references/jd-criteria.md)과 [채점 JSON·인수조건](skills/jd-application-review/references/rubric-and-report.md)을 참고하세요.

채점기 자체의 가상 자료 테스트는 `python3 -m unittest discover -s tests -v`로 실행합니다. 이 테스트 통과가 실제 지원서의 검수 완료를 뜻하지는 않습니다.

## 템플릿과 예시

- [한국어 이력서 HTML](skills/html-a4-resume/assets/resume-ko.html), [영어 이력서 HTML](skills/html-a4-resume/assets/resume-en.html): A4 세로 1페이지 시작 템플릿. 학생·신입은 1페이지, 경력자는 기본 1~2페이지로 조정합니다. 한국어는 명사형, 영어는 동사 중심 불릿으로 작성하며 두 언어의 사실을 대조합니다.
- [프로젝트 전체 목록](templates/PROJECT-INVENTORY.md): 모든 경험을 빠짐없이 연결합니다.
- [지원자 사전 질문지](templates/CANDIDATE-INTAKE.md): 경력·직무와 관계없이 사용하는 기본 입력. [학생용 보조 질문지](templates/STUDENT-INTAKE.md), [프로젝트 README](templates/PROJECT-README.md)는 해당할 때 사용합니다.
- [포트폴리오 HTML](skills/html-pdf-portfolio/assets/portfolio.html): 표지·Summary·회사/프로젝트 간지·핵심 성과·수상·학력/역량·채용 가치 마무리의 18페이지 작성 예시. [챕터 구성 지침](skills/html-pdf-portfolio/references/chapter-structure.md)에 따라 없는 항목은 삭제하고 실제 사례량에 맞춥니다.
- [포트폴리오 디자인 첨삭 기준](skills/html-pdf-portfolio/references/design-review.md): 밝은 배경·큰 결론·실제 근거·선택적 벤토 구성. `design-taste-frontend`의 문서에 맞는 원칙을 적용하며 해당 스킬이 없어도 사용할 수 있습니다.
- [프로젝트 한 페이지 기준](skills/html-pdf-portfolio/references/project-onepager.md): **검증된 성과를 먼저 보여주는 명사형 제목**, 회사→프로젝트 계층, 문제·내 역할 / 해결·판단 / 성과·조건을 정리합니다. 실제 이미지 비율·가독성에 맞춰 왼쪽·오른쪽·가운데 전체 너비 배치를 선택합니다.
- [A4 포스터 HTML](skills/academic-a4-poster/assets/poster.html): 2열 구조의 학술형 초안.
- [템플릿 PDF 예시](examples/): 실제 지원자 실적이 아닌 구조·출력 확인용입니다.
- [미니 실험 가이드](MINI-PROJECTS.md): 로봇·자율주행 학습자에게 맞는 선택형 보완 과제입니다. 모든 직무·경력자가 수행할 필수 단계가 아닙니다.

전체 경험은 개인 목록에 정리하고 PDF에는 대표 사례를 선별합니다. 공개 가능한 기술 프로젝트는 필요하면 GitHub에 연결합니다. A4 포스터는 초안 규격이며 대형 출력은 행사 규격에 맞춰 별도로 조판합니다.

포트폴리오 디자인 전에는 **원하는 테마색과 Summary 벤토 팔레트**를 확인합니다. 색상 코드·참고 이미지·스타일 가이드를 주면 맞춰 적용하고, 기존 자료에 선호가 있으면 다시 묻지 않습니다. 별도 선호가 없으면 기본 팔레트를 선택할 수 있습니다. 템플릿의 파란색은 예시이며 모든 지원자에게 고정된 색상이 아닙니다.

## 글꼴·글자 크기와 바로 쓸 수 있는 HTML

이력서와 포트폴리오에는 [Pretendard Variable 폰트와 라이선스](assets/fonts/README.md)가 포함돼 있습니다. 템플릿의 상대 경로로 읽으므로 글꼴 설치·외부 CDN 연결이 필요하지 않습니다. HTML만 따로 복사하지 않고 아래 도구로 폰트와 라이선스를 함께 준비하세요. 기존 파일을 덮어쓰지 않으므로 새 버전 폴더를 지정합니다.

실제 파일: [PretendardVariable.woff2](assets/fonts/PretendardVariable.woff2), [원본 라이선스](assets/fonts/LICENSE.txt). 버전·출처·SHA-256은 [폰트 안내](assets/fonts/README.md)에 기록돼 있습니다.

```bash
python3 tools/prepare_documents.py output/application/v1 --kind all
```

`resume-ko.html`, `resume-en.html`, `portfolio.html`과 `assets/fonts/`가 생성됩니다. 실제 자료로 HTML을 편집한 뒤 각각 PDF로 출력합니다. 이력서만 필요하면 `--kind resume`, 포트폴리오만 필요하면 `--kind portfolio`를 사용합니다.

```text
output/application/v1/
  resume-ko.html
  resume-en.html
  portfolio.html
  assets/fonts/
    PretendardVariable.woff2
    LICENSE.txt
    README.md
```

HTML을 공유하거나 다른 컴퓨터로 옮길 때는 **이 폴더 전체**를 전달합니다. 에이전트는 폰트 로드 완료 후 각 HTML과 같은 내용의 PDF를 만듭니다. 출력 PDF를 읽는 사람에게 별도 폰트 설치를 요구하지 않도록 실제 PDF의 글자와 포함된 글리프를 확인합니다.

| 템플릿 | CSS 적용 기본값 |
|---|---|
| A4 이력서 | 이름 23pt, 직무·섹션 11pt, 본문 10pt, 보조 9pt, 본문 줄간격 1.45 |
| 1600×900 포트폴리오 | 표지 제목 72px, 페이지 제목 60px, 본문 28px, 보조 22px, 캡션 18px |

내용에 맞게 조정하되 글자를 줄여 정보를 억지로 넣지 않습니다. 실제 폰트 로드·PDF 글리프·잘림·줄바꿈을 확인합니다. 템플릿은 작성 안내 예시이며 실제 지원자의 경험이 아닙니다.

## PDF 출력

가장 간단한 방법은 브라우저의 **인쇄 → PDF 저장**입니다. 폰트 로드를 기다리고 배경 그래픽을 포함하며 머리글·바닥글을 끕니다. 포트폴리오는 HTML의 16:9 사용자 지정 크기, 이력서·포스터는 A4인지 확인합니다.

Python과 Chrome·Chromium·Edge가 있다면 자동 출력도 가능합니다. 자동 설치는 하지 않습니다.

```bash
python3 tools/export_pdf.py output/application/v1/resume-ko.html output/application/v1/resume-ko.pdf
python3 tools/export_pdf.py output/application/v1/resume-en.html output/application/v1/resume-en.pdf
python3 tools/export_pdf.py output/application/v1/portfolio.html output/application/v1/portfolio.pdf
```

포스터가 필요한 경우 별도로 `python3 tools/export_pdf.py skills/academic-a4-poster/assets/poster.html output/poster.pdf`를 사용합니다.

Windows에서는 설치 환경에 따라 `python3` 대신 `python` 또는 `py`를 사용합니다. 브라우저를 찾지 못하면 `--browser`로 실행 파일 경로를 지정합니다. 기존 결과를 덮어쓸 때만 `--overwrite`를 사용합니다. 외부 웹 폰트·이미지가 있는 문서는 로드 상태를 별도로 확인하세요.

`pypdf`가 있는 Python 환경에서는 다음으로 페이지 수·규격·텍스트·링크 주석을 확인할 수 있습니다. 검사가 통과해도 모든 페이지의 시각 검토가 필요합니다.

```bash
python3 tools/check_pdf.py output/application/v1/resume-ko.pdf --kind resume
python3 tools/check_pdf.py output/application/v1/resume-en.pdf --kind resume
python3 tools/check_pdf.py output/application/v1/portfolio.pdf --kind portfolio
```

이력서 스킬은 위 템플릿을 복사해 실제 자료로 편집한 **한국어 HTML·PDF와 영어 HTML·PDF를 함께 전달**합니다. 위 명령은 템플릿 출력 확인용이며 개인 이력서 작성 자체를 대신하지 않습니다. `--kind resume`는 기본 1~2페이지의 A4 세로 문서를 확인합니다. 제출 조건상 더 긴 이력서는 `--max-pages`로 한도를 지정하고, 이름 등 추출 확인은 `--require-text`, 링크 주석 확인은 `--require-uri`로 지정합니다.

포트폴리오 검사는 기본 최대 30페이지이며 제출 조건에 맞게 `--kind portfolio --max-pages N`을 지정할 수 있습니다. 분량을 채우기 위해 없는 회사·프로젝트·성과·수상을 만들지 않습니다.

## 공개 자료의 범위

이 저장소에는 공용 지침·빈 템플릿·안내용 예시·라이선스가 포함된 공용 폰트를 둡니다. 실제 지원자의 이력서·연락처·회사 기밀·비공개 자료·개별 피드백은 개인 저장소나 허가된 공간에서 관리합니다. 타인의 코드·데이터·그림을 사용하면 원본 출처와 해당 라이선스를 확인합니다.

완성된 지원 문서의 사실과 공개 가능 범위는 본인 및 필요한 검토자가 확인해야 합니다. 자동 검사 결과와 실제 확인 범위는 [검증 기록](VALIDATION.md)에 남깁니다.
