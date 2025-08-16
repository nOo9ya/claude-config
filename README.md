# Claude 설정 공유

## 📂 설정 파일 비교

### settings.json vs .claude.json

- **settings.json**: Claude Code의 기본 사용자 설정 파일
  - 권한 설정 (permissions)
  - 피드백 상태 (feedbackSurveyState)
  - 기본 모드 설정 (defaultMode)
  - 권한 스킵 설정 (dangerouslySkipPermissions)

- **.claude.json**: MCP 서버 및 고급 기능 설정 파일
  - MCP 서버 연결 설정 (mcpServers)
  - 훅(hooks) 설정
  - MCP JSON 서버 활성화/비활성화 설정
  - 고급 워크플로우 설정

## 📋 개요

이 저장소는 여러 PC에서 동일한 Claude CLI 설정을 공유하기 위한 설정 파일들을 관리합니다.

## ✅ 글로벌 verbose 설정 확인

현재 글로벌 설정에서 `verbose` 모드가 활성화되어 있습니다:

```bash
# 글로벌 verbose 설정 완료
claude config set -g verbose true
```

이제 `claude code` 명령어를 실행할 때마다 자동으로 `--verbose` 모드가 활성화됩니다.

## 🔍 추가 확인 방법

```bash
# 현재 글로벌 설정 확인
claude config list -g

# 특정 설정값만 확인
claude config get -g verbose
```

## 📁 포함된 파일들

### 핵심 설정 파일들
- `global-config.json`: 글로벌 설정 (verbose 모드 포함)
- `settings.json`: 권한 및 기본 설정
- `agents/`: 커스텀 에이전트 설정 파일들
- `.gitmessage.txt`: Git 커밋 메시지 템플릿
- `.claude/hooks/`: 자동화 훅 스크립트 파일들

### 에이전트 목록
- `backend-api-reliability-expert.md`
- `code-refactoring-specialist.md`
- `devops-infrastructure-expert.md`
- `educational-guidance-mentor.md`
- `frontend-accessibility-expert.md`
- `performance-optimizer.md`
- `security-threat-modeling-expert.md`
- `system-architect.md`
- `technical-documentation-expert.md`

## 🚀 새 환경에서 설정 적용

### 1. 저장소 클론
```bash
git clone git@github.com:nOo9ya/claude-config.git
cd claude-config
```

### 2. 설정 파일 복사
```bash
# Claude 설정 디렉토리 확인
ls ~/.claude

# 기존 설정 백업 (옵션)
cp ~/.claude/settings.json ~/.claude/settings.json.backup

# 새 설정 적용
cp settings.json ~/.claude/
cp .claude.json ~/.claude/
cp -r agents ~/.claude/
cp -r .claude/hooks ~/.claude/

# 훅 스크립트 실행 권한 설정
chmod +x ~/.claude/hooks/add_agent_context.py

# 글로벌 설정 적용
claude config set -g verbose true
```

### 3. Git 커밋 메시지 템플릿 설정
```bash
# 커밋 메시지 템플릿으로 .gitmessage.txt 설정
git config commit.template ./.gitmessage.txt

# 글로벌로 설정하려면 (모든 저장소에 적용)
git config --global commit.template ~/.gitmessage.txt
```

### 4. 설정 확인
```bash
# 설정이 올바르게 적용되었는지 확인
claude config list -g
claude config list

# Git 템플릿 설정 확인
git config commit.template
```

## 📋 제외된 파일들

다음 파일들은 개인 정보 또는 세션별 데이터이므로 공유하지 않습니다:
- `.credentials.json` (인증 정보)
- `projects/` (프로젝트별 설정)
- `shell-snapshots/` (세션 스냅샷)
- `statsig/` (통계 데이터)
- `todos/` (할 일 목록)
- `ide/` (IDE 관련 설정)

## 🔄 설정 동기화

설정을 변경했을 때 저장소에 반영하는 방법:

```bash
# 변경된 설정 확인
claude config list -g > global-config.json
cp ~/.claude/settings.json .
cp -r ~/.claude/agents .

# Git 템플릿 파일도 함께 복사 (글로벌 설정 시)
cp ~/.gitmessage.txt .

# 변경사항 커밋 (템플릿이 설정되어 있으면 자동으로 적용됨)
git add .
git commit
git push
```

## 🤖 자동 서브 에이전트 선택 기능

### 개요
`.claude/hooks/add_agent_context.py` 스크립트는 사용자의 프롬프트를 분석하여 자동으로 적절한 서브 에이전트를 권장하는 기능입니다.

### 지원하는 서브 에이전트
- `code-refactoring-specialist`: 코드 리팩토링 및 개선
- `system-architect`: 시스템 아키텍처 설계
- `technical-documentation-expert`: 기술 문서화
- `performance-optimizer`: 성능 최적화
- `educational-guidance-mentor`: 교육 및 학습 지원
- `devops-infrastructure-expert`: DevOps 및 인프라
- `security-threat-modeling-expert`: 보안 분석 및 위협 모델링
- `backend-api-reliability-expert`: 백엔드 API 및 신뢰성
- `frontend-accessibility-expert`: 프론트엔드 및 접근성

### 작동 방식
1. 사용자가 프롬프트를 입력하면 자동으로 키워드를 분석
2. 한국어/영어 키워드를 기반으로 적절한 에이전트 선택
3. 복잡한 작업인 경우에만 에이전트 사용을 권장
4. 권장 에이전트와 설명을 자동으로 표시

### 설정 요구사항
⚠️ **중요**: 훅 스크립트는 실행 권한이 필요합니다.
```bash
chmod +x ~/.claude/hooks/add_agent_context.py
```

## ⚠️ 주의사항

- 개인 인증 정보는 절대 커밋하지 마세요
- 프로젝트별 설정은 각 환경에서 별도 관리하세요
- 에이전트 설정 변경 시 다른 PC에서도 동기화해주세요
- 훅 스크립트 복사 시 반드시 실행 권한을 설정하세요