# Claude Code MCP 서버 문제 해결 가이드

## 🔍 문제 상황

Claude Code에서 MCP(Model Context Protocol) 서버들이 연결되지 않는 문제가 발생할 때 사용하는 해결 방법입니다.

## 📊 문제 진단

### 1. 현재 MCP 서버 상태 확인

```bash
claude mcp list
```

**예상 출력 (문제 상황)**:

```
Checking MCP server health...

context7: https://mcp.context7.com/mcp (HTTP) - ✓ Connected
playwright: npx @playwright/mcp@latest - ✗ Failed to connect
sequential-thinking: npx -y @modelcontextprotocol/server-sequential-thinking - ✗ Failed to connect
deepwiki: npx mcp-deepwiki@latest - ✗ Failed to connect
memory: npx -y @modelcontextprotocol/server-memory - ✗ Failed to connect
```

### 2. 개별 패키지 설치 상태 확인

```bash
# 각 MCP 서버 패키지가 설치되는지 확인
npx @playwright/mcp@latest --version
npx -y @modelcontextprotocol/server-sequential-thinking --version
npx mcp-deepwiki@latest --version
npx -y @modelcontextprotocol/server-memory --version
```

## 🛠️ 해결 프로세스

### Step 1: 문제가 있는 MCP 서버들 제거

```bash
# 개별 서버 제거
claude mcp remove playwright
claude mcp remove sequential-thinking
claude mcp remove deepwiki
claude mcp remove memory
```

**각 명령어 실행 시 예상 출력**:

```
Removed MCP server "playwright" from local config
File modified: /home/user/.claude.json [project: /current/project/path]
```

### Step 2: 연결 상태 재확인

```bash
claude mcp list
```

**예상 출력**:

```
Checking MCP server health...

context7: https://mcp.context7.com/mcp (HTTP) - ✓ Connected
```

### Step 3: MCP 서버들 다시 추가

```bash
# Sequential Thinking MCP 서버 추가
claude mcp add sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Memory MCP 서버 추가
claude mcp add memory -- npx -y @modelcontextprotocol/server-memory

# DeepWiki MCP 서버 추가
claude mcp add deepwiki -- npx mcp-deepwiki@latest
```

**각 명령어 실행 시 예상 출력**:

```
Added stdio MCP server sequential-thinking with command: npx -y @modelcontextprotocol/server-sequential-thinking to local config
File modified: /home/user/.claude.json [project: /current/project/path]
```

### Step 4: 최종 연결 상태 확인

```bash
claude mcp list
```

**성공 시 예상 출력**:

```
Checking MCP server health...

context7: https://mcp.context7.com/mcp (HTTP) - ✓ Connected
sequential-thinking: npx -y @modelcontextprotocol/server-sequential-thinking - ✓ Connected
memory: npx -y @modelcontextprotocol/server-memory - ✓ Connected
deepwiki: npx mcp-deepwiki@latest - ✓ Connected
```

## 🧪 연결 테스트

### Context7 MCP 테스트

Claude Code에서 다음과 같이 테스트:

```bash
# Context7 라이브러리 검색 테스트
mcp__context7__resolve-library-id nuxt
```

### Sequential Thinking MCP 테스트

```bash
# 체계적 사고 과정을 위한 도구 사용
mcp__sequential-thinking__sequentialthinking "복잡한 문제를 단계별로 분석해보자"
```

## 📝 주요 MCP 서버 설명

| 서버명                  | 기능                      | 연결 방식 |
| ----------------------- | ------------------------- | --------- |
| **context7**            | 최신 라이브러리 문서 검색 | HTTP      |
| **sequential-thinking** | 체계적 사고 과정 지원     | stdio     |
| **memory**              | 대화 컨텍스트 관리        | stdio     |
| **deepwiki**            | 위키피디아 검색           | stdio     |

## 🚫 Playwright MCP 관리 (중요!)

> ⚠️ **프로젝트 정책**: 이 프로젝트에서는 Playwright MCP를 사용하지 않습니다. 실수로 설치된 경우 즉시 제거해야 합니다.

### Playwright MCP 제거 방법 (권장)

```bash
# Playwright MCP 서버 제거
claude mcp remove playwright

# 연결 상태 확인
claude mcp list
```

**제거 성공 시 예상 출력**:

```
Removed MCP server "playwright" from local config
File modified: /home/user/.claude.json [project: /current/project/path]
```

### Playwright MCP 설치 방법 (비권장 - 참고용만)

```bash
# ⚠️ 주의: 이 프로젝트에서는 사용 금지
claude mcp add playwright -- npx @playwright/mcp@latest
```

### Playwright MCP 완전 제거 (문제 해결 시)

```bash
# 1. MCP 서버에서 제거
claude mcp remove playwright

# 2. npx 캐시 정리
rm -rf ~/.npm/_npx/@playwright*

# 3. npm 캐시 정리
npm cache clean --force

# 4. 연결 상태 재확인
claude mcp list
```

### 왜 Playwright MCP를 사용하지 않는가?

1. **프로젝트 요구사항**: 문서 사이트이므로 브라우저 자동화 불필요
2. **번들 크기**: 8.8MB → 2-3MB 경량화 목표에 부합하지 않음
3. **복잡성**: 불필요한 의존성으로 인한 관리 부담
4. **대안**: 필요시 다른 테스팅 도구 사용 권장

## 🚨 문제 해결 팁

### 1. 권한 문제 해결

```bash
# npm 권한 문제가 있을 경우
npm config set prefix ~/.local
```

### 2. Node.js 버전 확인

```bash
node --version
# v20+ 권장
```

### 3. 네트워크 연결 확인

```bash
# Context7 HTTP 서버 연결 테스트
curl -I https://mcp.context7.com/mcp
```

### 4. 설정 파일 확인

```bash
# Claude 설정 파일 위치 확인
ls -la ~/.claude.json
```

## 🔄 완전 초기화 (마지막 수단)

모든 방법이 실패할 경우:

```bash
# 1. 모든 MCP 서버 제거
claude mcp remove context7
claude mcp remove sequential-thinking
claude mcp remove memory
claude mcp remove deepwiki

# 2. 설정 캐시 정리
rm -rf ~/.npm/_npx
npm cache clean --force

# 3. Claude Code 재시작
# 터미널을 완전히 종료하고 다시 시작

# 4. MCP 서버 다시 추가
claude mcp add --transport http context7 https://mcp.context7.com/mcp
claude mcp add sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
claude mcp add memory -- npx -y @modelcontextprotocol/server-memory
claude mcp add deepwiki -- npx mcp-deepwiki@latest
```

## 🌐 개인 설정으로 MCP 서버 설치 (Global Configuration)

새로운 프로젝트에서도 동일한 MCP 서버들을 자동으로 사용하려면 개인(전역) 설정으로 설치할 수 있습니다.

### 전역 MCP 서버 설치

```bash
# Context7 MCP 서버 (전역 설치)
claude mcp add --global context7 --transport http https://mcp.context7.com/mcp

# Sequential Thinking MCP 서버 (전역 설치)
claude mcp add --global sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Memory MCP 서버 (전역 설치)
claude mcp add --global memory -- npx -y @modelcontextprotocol/server-memory

# DeepWiki MCP 서버 (전역 설치)
claude mcp add --global deepwiki -- npx mcp-deepwiki@latest
```

### 전역 설정 확인

```bash
# 전역 MCP 서버 목록 확인
claude mcp list --global
```

**성공 시 예상 출력**:

```
Global MCP servers:

context7: https://mcp.context7.com/mcp (HTTP) - ✓ Connected
sequential-thinking: npx -y @modelcontextprotocol/server-sequential-thinking - ✓ Connected
memory: npx -y @modelcontextprotocol/server-memory - ✓ Connected
deepwiki: npx mcp-deepwiki@latest - ✓ Connected
```

### 프로젝트별 vs 전역 설정 비교

| 설정 타입      | 명령어                           | 적용 범위       | 설정 파일 위치           |
| -------------- | -------------------------------- | --------------- | ------------------------ |
| **프로젝트별** | `claude mcp add <name>`          | 현재 프로젝트만 | `<project>/.claude.json` |
| **전역**       | `claude mcp add --global <name>` | 모든 프로젝트   | `~/.claude.json`         |

### 전역 설정의 장단점

**장점**:

-   ✅ 새 프로젝트마다 MCP 서버 재설치 불필요
-   ✅ 일관된 개발 환경 유지
-   ✅ 설정 관리 단순화

**단점**:

-   ❌ 프로젝트별 커스터마이징 제한
-   ❌ 특정 프로젝트에서 불필요한 MCP 로딩

### 전역 MCP 서버 관리

```bash
# 특정 전역 MCP 서버 제거
claude mcp remove --global <server-name>

# 모든 전역 MCP 서버 제거 (주의!)
claude mcp remove --global context7
claude mcp remove --global sequential-thinking
claude mcp remove --global memory
claude mcp remove --global deepwiki

# 전역 설정 파일 직접 확인
cat ~/.claude.json
```

### 권장 설정 전략

1. **기본 MCP 서버들은 전역 설치**:

    - context7, sequential-thinking, memory, deepwiki

2. **프로젝트별 특수 요구사항만 로컬 설치**:

    - 특정 프로젝트에만 필요한 MCP 서버

3. **새 프로젝트 시작 시**:

    ```bash
    # 전역 설정 확인
    claude mcp list --global

    # 프로젝트별 추가 설정 필요시
    claude mcp add project-specific-server -- <command>
    ```

## 🤖 서브 에이전트 자동 실행 설정

Claude Code에서 작업 타입에 따라 서브 에이전트를 자동으로 실행하도록 설정하는 방법입니다.

### CLAUDE.md 파일에 자동화 지침 추가

프로젝트 루트에 `CLAUDE.md` 파일을 생성하고 다음 지침을 추가:

```markdown
## 🛠 서브 에이전트 자동 실행 규칙

### 작업 타입별 자동 서브 에이전트 선택

Claude는 다음 키워드나 작업 패턴을 감지하면 자동으로 해당 서브 에이전트를 실행해야 함:

1. **코드 리팩토링**:

    - 영어: `refactor`, `clean up`, `improve code`, `technical debt`
    - 한글: `리팩토링`, `코드 정리`, `코드 개선`, `기술부채`, `정리해줘`
    - 자동 실행: `code-refactoring-specialist`

2. **시스템 아키텍처**:

    - 영어: `architecture`, `design`, `scalability`, `microservices`
    - 한글: `아키텍처`, `설계`, `구조 설계`, `확장성`, `마이크로서비스`, `시스템 설계`
    - 자동 실행: `system-architect`

3. **기술 문서화**:

    - 영어: `documentation`, `API docs`, `README`, `user guide`
    - 한글: `문서화`, `문서 작성`, `가이드`, `사용법`, `매뉴얼`, `API 문서`
    - 자동 실행: `technical-documentation-expert`

4. **성능 최적화**:

    - 영어: `performance`, `slow`, `optimization`, `bottleneck`
    - 한글: `성능`, `최적화`, `느려`, `병목`, `속도 개선`, `빠르게`
    - 자동 실행: `performance-optimizer`

5. **교육/학습**:

    - 영어: `explain`, `learn`, `understand`, `how does`, `tutorial`
    - 한글: `설명해줘`, `배우고 싶어`, `이해하고 싶어`, `어떻게`, `튜토리얼`, `가르쳐줘`
    - 자동 실행: `educational-guidance-mentor`

6. **DevOps/인프라**:

    - 영어: `deployment`, `CI/CD`, `infrastructure`, `monitoring`
    - 한글: `배포`, `인프라`, `모니터링`, `서버 관리`, `운영`, `인프라 구축`
    - 자동 실행: `devops-infrastructure-expert`

7. **보안 분석**:

    - 영어: `security`, `vulnerability`, `threat`, `secure`
    - 한글: `보안`, `취약점`, `보안 검사`, `안전하게`, `보안 분석`, `위협`
    - 자동 실행: `security-threat-modeling-expert`

8. **백엔드 API**:

    - 영어: `API`, `endpoint`, `database`, `server`, `reliability`
    - 한글: `API`, `엔드포인트`, `데이터베이스`, `서버`, `백엔드`, `신뢰성`
    - 자동 실행: `backend-api-reliability-expert`

9. **프론트엔드/UI**:
    - 영어: `component`, `responsive`, `accessibility`, `UI`, `UX`
    - 한글: `컴포넌트`, `반응형`, `접근성`, `UI`, `UX`, `사용자 인터페이스`
    - 자동 실행: `frontend-accessibility-expert`

### 자동 실행 우선순위

-   복잡한 작업일수록 서브 에이전트 사용 우선
-   단순한 질문이나 1-2단계 작업은 직접 처리
-   불확실할 때는 서브 에이전트 사용
```

### Claude Code 설정 파일 활용

`~/.claude.json` 또는 프로젝트별 `.claude.json`에 hooks 추가:

```json
{
    "mcp_servers": {
        // ... MCP 서버 설정
    },
    "hooks": {
        "user-prompt-submit-hook": {
            "command": "echo '🤖 작업 타입을 분석하여 적절한 서브 에이전트를 자동 선택합니다.'",
            "enabled": true
        }
    },
    "auto_agents": {
        "enabled": true,
        "rules": [
            {
                "keywords": [
                    "refactor",
                    "clean up",
                    "improve code",
                    "리팩토링",
                    "코드 정리",
                    "정리해줘"
                ],
                "agent": "code-refactoring-specialist"
            },
            {
                "keywords": [
                    "architecture",
                    "design",
                    "scalability",
                    "아키텍처",
                    "설계",
                    "시스템 설계"
                ],
                "agent": "system-architect"
            },
            {
                "keywords": [
                    "documentation",
                    "API docs",
                    "README",
                    "문서화",
                    "문서 작성",
                    "가이드"
                ],
                "agent": "technical-documentation-expert"
            },
            {
                "keywords": [
                    "performance",
                    "slow",
                    "optimization",
                    "성능",
                    "최적화",
                    "느려",
                    "빠르게"
                ],
                "agent": "performance-optimizer"
            },
            {
                "keywords": [
                    "explain",
                    "learn",
                    "understand",
                    "설명해줘",
                    "가르쳐줘",
                    "어떻게"
                ],
                "agent": "educational-guidance-mentor"
            }
        ]
    }
}
```

### 환경 변수를 통한 자동화

```bash
# ~/.bashrc 또는 ~/.zshrc에 추가
export CLAUDE_AUTO_AGENTS=true
export CLAUDE_DEFAULT_THINKING=sequential-thinking
export CLAUDE_AUTO_CONTEXT7=true

# 프로젝트별 설정
cd /your/project
echo 'export CLAUDE_PROJECT_AGENTS="code-refactoring-specialist,system-architect"' >> .env
```

### 실행 시 자동화 확인

```bash
# Claude Code 시작 시 자동화 설정 확인
claude --verbose

# 특정 작업에서 서브 에이전트 강제 실행
claude "refactor this code" --agent code-refactoring-specialist
```

### 자동화 문제 해결

**문제**: 서브 에이전트가 자동으로 실행되지 않음

```bash
# 1. 설정 파일 확인
cat ~/.claude.json | grep -A 10 "auto_agents"

# 2. hooks 설정 확인
cat ~/.claude.json | grep -A 5 "hooks"

# 3. Claude Code 버전 확인 (최신 버전 필요)
claude --version

# 4. 설정 리로드
claude config reload
```

### 수동 서브 에이전트 실행 (백업 방법)

자동화가 작동하지 않을 때 수동으로 실행:

```bash
# 명령어에서 직접 지정
claude "help me refactor this code" --use-agent code-refactoring-specialist

# 대화 중 서브 에이전트 호출
# "다음 작업에 code-refactoring-specialist 에이전트를 사용해줘"
```

## ✅ 성공 지표

-   `claude mcp list`에서 모든 서버가 `✓ Connected` 상태
-   Context7에서 라이브러리 검색 가능
-   Sequential thinking으로 체계적 사고 과정 실행 가능
-   Memory로 대화 기록 관리 가능
-   DeepWiki로 위키피디아 검색 가능

---

**작성일**: 2025-08-07  
**버전**: 1.0.0  
**테스트 환경**: WSL2, Node.js v20+, Claude Code 1.0.70+
