"""
AI Council — 批驳官 (Critic)
职责：专职找漏洞、风险点、逻辑矛盾
原则：找不到问题视为失职
"""

from core.base_role import BaseRole
from core.models import Opinion
import json


CRITIC_SYSTEM_PROMPT = """你是一个评议系统中的批驳官。

你的唯一职责是：找出当前方案的问题、漏洞、风险和逻辑矛盾。

严格规则：
1. 你必须提出至少3个有实质内容的异议，找不到问题视为失职
2. 每条异议必须说明：问题是什么、为什么是问题、可能导致什么后果
3. 不允许说"这个方案看起来不错"之类的赞许——这不是你的职责
4. 异议必须基于逻辑或事实，不能无中生有
5. 按严重程度排序输出（最严重的问题排第一）

你看不到其他角色的意见，只基于当前提供的方案内容进行审查。

输出格式（严格JSON）：
{
  "issues": [
    {
      "title": "问题标题",
      "content": "详细描述",
      "severity": 1-5,
      "confidence": 0.0-1.0,
      "evidence": ["依据1", "依据2"]
    }
  ],
  "overall_assessment": "总体风险评估（1-2句话）"
}"""


class Critic(BaseRole):

    @property
    def system_prompt(self) -> str:
        return CRITIC_SYSTEM_PROMPT

    def build_input(self, draft: str, case_context: str) -> str:
        return f"""请审查以下方案，找出所有问题：

=== 议案背景 ===
{case_context}

=== 待审查方案 ===
{draft}

请严格按照你的职责输出批驳意见。"""

    def parse_output(self, raw_output: str) -> list[Opinion]:
        try:
            data = json.loads(raw_output)
            opinions = []
            for issue in data.get("issues", []):
                opinions.append(Opinion(
                    role="critic",
                    content=issue["content"],
                    severity=issue.get("severity", 3),
                    confidence=issue.get("confidence", 0.7),
                    rebuttable=True,
                    evidence=issue.get("evidence", [])
                ))
            return opinions
        except json.JSONDecodeError:
            # 降级处理：返回原始文本作为单条意见
            return [Opinion(
                role="critic",
                content=raw_output,
                severity=3,
                confidence=0.5,
                rebuttable=True
            )]
