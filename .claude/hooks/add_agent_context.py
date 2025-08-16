#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

import json
import sys
import re
from datetime import datetime

# 서브 에이전트 자동 선택 규칙 (MCP_TROUBLESHOOTING.md 기반)
AGENT_RULES = {
    "code-refactoring-specialist": {
        "keywords": [
            # 영어
            "refactor", "clean up", "improve code", "technical debt",
            # 한글
            "리팩토링", "코드 정리", "코드 개선", "기술부채", "정리해줘"
        ],
        "description": "코드 리팩토링 및 개선"
    },
    "system-architect": {
        "keywords": [
            # 영어
            "architecture", "design", "scalability", "microservices",
            # 한글
            "아키텍처", "설계", "구조 설계", "확장성", "마이크로서비스", "시스템 설계"
        ],
        "description": "시스템 아키텍처 설계"
    },
    "technical-documentation-expert": {
        "keywords": [
            # 영어
            "documentation", "API docs", "README", "user guide",
            # 한글
            "문서화", "문서 작성", "가이드", "사용법", "매뉴얼", "API 문서"
        ],
        "description": "기술 문서화"
    },
    "performance-optimizer": {
        "keywords": [
            # 영어
            "performance", "slow", "optimization", "bottleneck",
            # 한글
            "성능", "최적화", "느려", "병목", "속도 개선", "빠르게"
        ],
        "description": "성능 최적화"
    },
    "educational-guidance-mentor": {
        "keywords": [
            # 영어
            "explain", "learn", "understand", "how does", "tutorial",
            # 한글
            "설명해줘", "배우고 싶어", "이해하고 싶어", "어떻게", "튜토리얼", "가르쳐줘"
        ],
        "description": "교육 및 학습 지원"
    },
    "devops-infrastructure-expert": {
        "keywords": [
            # 영어
            "deployment", "CI/CD", "infrastructure", "monitoring",
            # 한글
            "배포", "인프라", "모니터링", "서버 관리", "운영", "인프라 구축"
        ],
        "description": "DevOps 및 인프라"
    },
    "security-threat-modeling-expert": {
        "keywords": [
            # 영어
            "security", "vulnerability", "threat", "secure",
            # 한글
            "보안", "취약점", "보안 검사", "안전하게", "보안 분석", "위협"
        ],
        "description": "보안 분석 및 위협 모델링"
    },
    "backend-api-reliability-expert": {
        "keywords": [
            # 영어
            "API", "endpoint", "database", "server", "reliability",
            # 한글
            "API", "엔드포인트", "데이터베이스", "서버", "백엔드", "신뢰성"
        ],
        "description": "백엔드 API 및 신뢰성"
    },
    "frontend-accessibility-expert": {
        "keywords": [
            # 영어
            "component", "responsive", "accessibility", "UI", "UX",
            # 한글
            "컴포넌트", "반응형", "접근성", "UI", "UX", "사용자 인터페이스"
        ],
        "description": "프론트엔드 및 접근성"
    }
}

def analyze_prompt_for_agent(prompt: str) -> tuple[str, str] | None:
    """프롬프트를 분석하여 적절한 서브 에이전트를 찾습니다."""
    prompt_lower = prompt.lower()
    
    # 각 에이전트의 키워드를 검사
    for agent_name, config in AGENT_RULES.items():
        for keyword in config["keywords"]:
            # 한글의 경우 단어 경계가 명확하지 않으므로 단순 포함 검사
            if keyword.lower() in prompt_lower:
                return agent_name, config["description"]
    
    return None

def should_use_agent(prompt: str) -> bool:
    """복잡한 작업인지 판단하여 서브 에이전트 사용 여부를 결정합니다."""
    # 단순한 질문 패턴
    simple_patterns = [
        r'^(what|how|when|where|why|who)\s+is\s+',  # "what is", "how is" 등
        r'^\w+\s*\?',  # 단어 하나 + 물음표
        r'^(yes|no)\s*',  # 예/아니오
    ]
    
    prompt_lower = prompt.lower().strip()
    
    for pattern in simple_patterns:
        if re.match(pattern, prompt_lower):
            return False
    
    # 복잡한 작업 키워드
    complex_keywords = [
        "implement", "create", "build", "develop", "design",
        "구현", "만들어", "생성", "개발", "설계"
    ]
    
    for keyword in complex_keywords:
        if keyword.lower() in prompt_lower:
            return True
    
    # 기본적으로 중간 길이 이상이면 서브 에이전트 사용
    return len(prompt.split()) >= 2

def main():
    try:
        # stdin에서 JSON 입력 읽기
        stdin_content = sys.stdin.read().strip()
        if not stdin_content:
            sys.exit(0)
            
        input_data = json.loads(stdin_content)
        prompt = input_data.get('prompt', '')
        
        if not prompt:
            sys.exit(0)
        
        # 적절한 서브 에이전트 찾기
        agent_match = analyze_prompt_for_agent(prompt)
        
        
        if agent_match and should_use_agent(prompt):
            agent_name, description = agent_match
            
            # 서브 에이전트 사용 권장 컨텍스트 출력
            print(f"🤖 **자동 에이전트 선택**: {description}")
            print(f"📋 **권장 에이전트**: `{agent_name}`")
            print(f"🕒 **분석 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print()
            print("💡 **안내**: 이 작업에 특화된 서브 에이전트를 사용하는 것을 권장합니다.")
            print("---")
        
        sys.exit(0)
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()