# Mac·Windows 환경 준비와 브라우저 검증

이 지침은 실제 사이트를 개발할 때 적용한다. 공용 키트에 지침을 추가하는 것만으로 사용자의 컴퓨터에 도구를 설치하지 않는다.

## OS와 셸을 먼저 감지

도구가 제공하는 환경 정보를 우선 사용하고 OS·CPU 아키텍처·현재 셸·작업 경로·Node/npm/Git·사용 가능한 브라우저 도구를 확인한다. 환경이 불명확하면 아래처럼 읽기 전용 확인부터 한다. Node가 없을 수 있으므로 Node만으로 OS 감지를 시작하지 않는다.

| 환경 | 확인 예시 | 실행 방식 |
|---|---|---|
| macOS zsh/bash | `uname -s`, `uname -m`, `command -v node`, `command -v git` | 기존 셸과 설치된 패키지 매니저를 유지 |
| Windows PowerShell | `$PSVersionTable.PSVersion`, `[System.Runtime.InteropServices.RuntimeInformation]::OSDescription`, `Get-Command node,npm,git -ErrorAction SilentlyContinue` | PowerShell 문법·Windows 경로 사용 |
| WSL/Linux | `uname -s`, `/proc/version` 확인 | Windows와 WSL의 Node·node_modules를 섞지 않고 한 환경 안에서 설치·실행 |

`node --version`, `npm --version`, `git --version`을 각각 실행해 실제 실행 여부를 확인한다. Node가 있으면 `node -p "process.platform + ' ' + process.arch"`로 보조 확인한다. 경로에 공백·한글이 있어도 동작하도록 셸에 맞게 인용한다. PowerShell 5.1에서는 `&&`, Bash heredoc, `export VAR=...`를 그대로 붙여 넣지 않는다. 명령은 한 줄씩 실행하고 환경 변수는 필요한 경우 `$env:변수명` 문법을 쓴다.

## 빠진 도구만 준비

- Node는 설치할 Next.js가 지원하는 LTS를 [공식 다운로드](https://nodejs.org/en/download)에서 확인한다. 기존 버전이 호환되면 재설치하지 않는다.
- macOS는 기존 버전 관리자가 있으면 유지하고, 없으면 CPU에 맞는 공식 설치 패키지를 기본 안내한다. 이 작업을 위해 Homebrew·버전 관리자·셸 플러그인을 새로 강제 설치하지 않는다.
- Windows는 공식 Windows Installer를 기본 안내한다. 이미 신뢰할 수 있는 설치 경로/버전 관리자가 있으면 재사용한다. PowerShell에서 npm.ps1 실행 정책 오류가 나면 먼저 `npm.cmd`, `npx.cmd`로 실행한다. 시스템 ExecutionPolicy를 완화하는 것을 기본 해결책으로 삼지 않는다.
- OS 전체 설치·관리자 권한·PATH/셸 설정 변경이 필요하면 변경 내용과 이유를 설명하고 필요한 승인을 받는다. 권한이 있는 프로젝트 내부 패키지 설치와 코드 작성은 계속 진행한다. 설치 완료 후 터미널을 다시 열어 버전과 실제 경로를 재확인한다.
- Git이 없으면 로컬 개발은 가능한 범위에서 진행하고 업로드 전에 [공식 Git 설치](https://git-scm.com/downloads)를 안내한다. Git 작성자·계정 설정을 임의로 전역 변경하지 않는다.
- 기존 잠금 파일에 맞는 패키지 매니저를 쓴다. npm 예시의 `npm`/`npx`는 Windows 정책 문제 시 `npm.cmd`/`npx.cmd`로 대체 가능하다. 패키지별 OS 전용 스크립트보다 Node 스크립트·npm scripts를 사용한다.
- 로컬 서버는 사용 중인 포트를 확인하고 충돌하면 다른 포트를 선택해 브라우저/테스트 설정도 맞춘다. 다른 작업의 서버를 종료하지 않는다.

## 브라우저로 보면서 개발

사용 가능한 Playwright MCP·브라우저 자동화 도구가 있으면 로컬 사이트를 열어 관찰 → 수정 → 재확인의 반복에 사용한다. 연결 도구가 없으면 프로젝트에 Playwright Test를 추가해 검증할 수 있다. [현재 설치 요구사항](https://playwright.dev/docs/intro)과 OS 지원 범위를 확인하고 테스트에 필요한 Chromium부터 준비한다.

```text
npm install -D @playwright/test
npx playwright install chromium
```

기존 Playwright 설정이 있으면 병합하고 덮어쓰지 않는다. 브라우저 다운로드가 막히면 재시도 원인을 확인하고 이미 사용 가능한 브라우저 도구나 사용자 직접 확인으로 전환한다. 설치·네트워크·지원 OS 제약을 기록하고 코드 개발은 가능한 범위에서 이어간다. Linux 시스템 라이브러리 설치가 필요하면 `--with-deps`를 무조건 실행하지 않고 필요한 권한·변경 범위를 확인한다.

`playwright.config.ts`는 해당 프로젝트에 맞게 작성한다. 다음은 production 빌드 확인용 최소 예시다. `npm run build`를 먼저 성공시킨다. 이미 있던 임의 서버를 재사용하지 않아 production 검증과 dev 검증을 혼동하지 않는다. 포트는 빈 값으로 조정한다.

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  use: { baseURL: 'http://127.0.0.1:3100', trace: 'retain-on-failure' },
  webServer: {
    command: 'npm run start -- --hostname 127.0.0.1 --port 3100',
    url: 'http://127.0.0.1:3100',
    reuseExistingServer: false,
  },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile', use: { ...devices['Pixel 7'] } },
  ],
});
```

실제 화면에 맞는 `e2e/*.spec.ts`를 작성한 뒤 `npx playwright test`로 실행한다. 홈페이지→블로그 탭→실제 글, 제목/날짜/이미지, 모바일 메뉴, 목록 추가 로드·중복·마지막·재시도·뒤로가기, 초안 404를 확인한다. 페이지 크기를 넘는 가상 글은 임시 테스트 환경에서만 사용한다. 목록 JS 비활성 검사는 별도 context로 확인한다. 이미지 로딩 실패·console error·본문 가로 넘침도 확인한다. 클릭/스크롤 후에는 고정 sleep보다 locator·응답·상태 조건을 기다린다.

스크린샷은 홈·목록·본문을 desktop/mobile로 남기고 실제 이미지를 열어 글꼴·배치·잘림을 눈으로 확인한 뒤 수정한다. 스크린샷을 저장했다는 이유만으로 시각 검수 완료라고 하지 않는다. 보고서·스크린샷·trace에 개인 자료가 들어갈 수 있으므로 개인 QA 위치에 보관하고 공개 저장소/배포에는 넣지 않는다. 앱의 `.gitignore`에 `playwright-report/`, `test-results/`, `blob-report/` 등 사용한 출력 경로를 추가한다.

Vercel 배포 후에는 같은 핵심 흐름을 실제 반환된 URL에서 다시 확인한다. 배포 URL 검사용 설정은 로컬 webServer 없이 실제 baseURL을 사용하고, 테스트 때문에 공개 글을 수정하거나 테스트 글을 배포하지 않는다. Playwright를 실행하지 못했거나 현재 OS 하나에서만 확인했으면 그 범위를 명시한다. Mac에서 검사한 결과를 Windows 실기 검증으로 표시하지 않는다.

공식 참고: [Playwright webServer](https://playwright.dev/docs/test-webserver), [Vercel CLI](https://vercel.com/docs/cli).
