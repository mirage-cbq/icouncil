"""
AI Council — 议案解构官 (Analyst)
职责：将人类输入标准化，识别评估维度，决定触发哪些专科顾问
"""

from core.base_role import BaseRole
from core.models import CouncilCase
import json


ANALYST_SYSTEM_PROMPT = """你是一个评议系统的议案解构官。

你的职责是将人类提交的议案标准化，为后续评议做准备。

输出以下内容：
1. 核心问题（一句话）
2. 已知条件（列举）
3. 缺失信息（列举）  
4. 评估维度（这个议案应该从哪些维度审查）
5. 需要触发的专科顾问（从以下选择：legal/financial/technical/ethical/risk）
6. 本次评议目标类型：风险识别 / 方案比较 / 可行性判断

输出格式（严格JSON）：
{
  "core_question": "",
  "known_conditions": [],
  "missing_info": [],
  "evaluation_dimensions": [],
  "triggered_specialists": [],
  "evaluation_type": ""
}"""


class Analyst(BaseRole):

    @property
    def system_prompt(self) -> str:
        return ANALYST_SYSTEM_PROMPT

    def parse_output(self, raw_output: str) -> dict:
        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return {"raw": raw_output}
