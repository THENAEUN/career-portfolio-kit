# 프로젝트 구성과 순차 설치

## 시작과 설치

먼저 [Mac·Windows 환경 지침](environment-and-browser.md)으로 OS·셸과 도구를 감지한다. 아래 명령은 해당 셸에 맞게 실행하며 설치·경로·PowerShell 정책 문제를 사용자에게 떠넘기지 않고 원인을 확인해 적합한 방법을 안내한다.

현재 작업 폴더·Git 원격·변경 상태·기존 사이트/잠금 파일을 확인한다. 공용 키트 안에 사용자의 실제 사이트를 만들지 않는다. 사용자가 지정한 프로젝트 또는 키트 바깥의 새 폴더를 사용한다. 기존 앱을 파괴하거나 `create-next-app`으로 덮어쓰지 않는다.

먼저 `node --version`, `npm --version`과 기존 package.json을 확인한다. 새 앱은 실행 시점의 [Next.js 설치 문서](https://nextjs.org/docs/app/getting-started/installation)의 Node 요구사항·현재 안정 버전을 확인하고 지원되는 Node LTS를 선택한다. Node 설치가 필요하면 [공식 다운로드](https://nodejs.org/en/download)를 안내한다. 버전 숫자를 오래 고정한 지침에 의존하지 않는다.

아래는 새 폴더 `personal-site`의 npm 예시다. 디렉터리 이름은 사용자 프로젝트에 맞춘다. 기존 앱에서는 감지한 패키지 매니저와 버전을 유지한다.

```bash
npx create-next-app@latest personal-site --typescript --tailwind --eslint --app --src-dir --import-alias '@/*' --use-npm
cd personal-site
npm install gray-matter zod react-markdown remark-gfm server-only
npm run dev
```

- 생성기 추가 질문이 있으면 비개발자에게 선택을 떠넘기지 않고 확인한 목적에 맞는 기본값으로 처리한다.
- Tailwind는 생성기가 설정한 버전을 사용한다. [현행 공식 Next.js 연동](https://tailwindcss.com/docs/installation/framework-guides/nextjs)을 확인하고 Tailwind 3/4 설정을 섞지 않는다.
- Markdown 파싱은 `gray-matter`, frontmatter 검증은 `zod`, 본문 렌더링은 `react-markdown` + `remark-gfm`을 기본으로 한다. 문법 강조·아이콘·애니메이션은 필요할 때만 추가한다.
- 설치 결과와 잠금 파일을 남긴다. 실행에 실패하면 원인과 해결을 보고하고 성공한 것처럼 다음 단계로 넘어가지 않는다. Vercel CLI는 배포 단계에 필요할 때만 `npx`로 사용한다.
- 최신 Next.js API는 설치된 버전과 프로젝트의 AGENTS.md/번들 문서를 우선 확인한다. 예를 들어 비동기 `params`를 요구하는 버전은 타입과 접근 방식을 그 버전에 맞춘다.

## 권장 파일 경계

```text
personal-site/
  content/
    profile/profile.json        # 공개하기로 한 소개·경력만
    projects/                   # 선택한 프로젝트의 공개 내용
    blog/<slug>.md
  public/images/blog/<slug>/
  src/
    app/
      layout.tsx
      page.tsx
      blog/page.tsx
      blog/page/[page]/page.tsx
      blog/[slug]/page.tsx
      sitemap.ts
      robots.ts
      not-found.tsx
    components/
      site-header.tsx
      blog/article-body.tsx
      blog/article-list.tsx
      blog/archive-feed.tsx     # 무한스크롤만 client boundary
    lib/
      posts.ts                  # server-only: fs·검증·공개 필터
      post-types.ts             # 브라우저에 전달 가능한 타입만
  package.json
  <package-manager-lockfile>
```

프로젝트 공개 문서에 글 추가·로컬 실행·배포 방법을 기록한다. 별도 DB 없이 `next build`에서 글을 읽고 Vercel이 제공한다. 런타임 파일 쓰기로 글을 저장하지 않는다.

## 홈페이지와 디자인

- 대표 문구는 검증된 전문성·성과를 앞세우고 실제 프로젝트로 연결한다. PDF를 사이트 전체 화면으로 임베드하는 것으로 대신하지 않는다. PDF 다운로드는 공개 허용된 최신 파일에만 연결한다.
- 상단 내비게이션: 홈/프로젝트/소개(자료에 따라 통합 가능)/블로그. 모바일 메뉴의 열기·닫기·현재 위치·키보드 포커스를 구현한다.
- 기본 Pretendard는 키트의 `assets/fonts/PretendardVariable.woff2`를 사이트 자산에 복사하고 `next/font/local`로 로드한다. 재배포 라이선스 `LICENSE.txt`도 보존한다. 키트 밖에서 경로를 찾지 못하면 시스템 글꼴로 임시 표시하고 누락을 보고한다.
- 본문 폭 약 680~760px, 본문 약 17~18px·줄간격 약 1.7~1.8을 출발점으로 모바일과 실제 한국어 문장을 보며 조정한다. 가로로 긴 코드·표는 해당 영역에서 스크롤한다. 이미지는 원본 비율을 유지한다.
- 포커스 표시, 대비, semantic header/nav/main/article/footer, 제목 계층, reduced-motion을 지원한다. 무한스크롤 상태 변화는 `aria-live="polite"`로 짧게 전달하고 새 글이 로드돼도 포커스를 이동하지 않는다.
- 카드·장식·움직임은 내용을 돕는 범위로 제한한다. 사용자 스타일을 우선하고 토스의 글·그림·로고를 가져오지 않는다.

## SEO 구현

Next.js의 서버 렌더링/사전 생성을 사용한다. 본문 텍스트와 첫 목록을 클라이언트 fetch 뒤에만 나타나게 만들지 않는다.

- `generateStaticParams`로 공개 글과 유효한 아카이브 페이지를 생성한다. 잘못된 slug·범위 밖 페이지는 `notFound()`로 처리한다.
- `generateMetadata`로 글별 title/description/canonical/Open Graph를 구성한다. 첫 목록의 주소는 `/blog`로 통일하고 `/blog/page/1`은 리디렉션한다. 2페이지 이상은 각 페이지 자체를 canonical로 지정한다.
- `metadataBase`와 sitemap은 확정한 실제 사이트 URL을 사용한다. 로컬·미확정 도메인을 프로덕션 canonical에 넣지 않는다. 도메인을 변경하면 설정도 갱신한다.
- sitemap에 공개 홈페이지·프로젝트·글·목록을 포함하고 초안·예약 글은 제외한다. robots와 실제 페이지의 `noindex`를 확인한다. 검색 등록/순위는 보장하지 않는다.
- BlogPosting JSON-LD는 확인된 저자·제목·날짜·URL만 사용하며 직렬화할 때 `<`를 이스케이프해 script 종료 문자열 주입을 막는다. OG 이미지가 없으면 사이트의 실제 기본 이미지를 쓴다.
- Preview는 색인되지 않도록 설정하고, Production의 의도치 않은 접근 보호/noindex는 배포 후 확인한다.

공식 참고: [메타데이터](https://nextjs.org/docs/app/getting-started/metadata-and-og-images), [정적 경로 생성](https://nextjs.org/docs/app/api-reference/functions/generate-static-params).
