# Claude 설정 공유

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
cp -r agents ~/.claude/

# 글로벌 설정 적용
claude config set -g verbose true
```

### 3. 설정 확인
```bash
# 설정이 올바르게 적용되었는지 확인
claude config list -g
claude config list
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

# 변경사항 커밋
git add .
git commit -m "설정 업데이트"
git push
```

## ⚠️ 주의사항

- 개인 인증 정보는 절대 커밋하지 마세요
- 프로젝트별 설정은 각 환경에서 별도 관리하세요
- 에이전트 설정 변경 시 다른 PC에서도 동기화해주세요