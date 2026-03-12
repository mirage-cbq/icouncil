"""
AI Council — 起草官 (Drafter)
职责：在议案基础上补全细节，形成完整可评估的方案版本
视角：建设性，不主动找缺陷
"""
from core.base_role import BaseRole


DRAFTER_SYSTEM_PROMPT = """你是一个评议系统中的起草官。

你的职责是：基于输入的议案，补全细节，形成一个完整、具体、可被评估的方案。

规则：
1. 建设性视角——你的任务是把方案写完整，不是挑毛病
2. 对于缺失信息，给出合理的假设并说明
3. 方案要具体可操作，避免模糊表述
4. 明确列出方案的关键前提和假设条件

输出格式：
- 方案概述（1段）
- 关键步骤（列举）
- 核心假设（列举）
- 预期效果"""

class Drafter(BaseRole):
    @property
    def system_prompt(self) -> str:
        return DRAFTER_SYSTEM_PROMPT

    def parse_output(self, raw_output: str) -> dict:
        return {"draft": raw_output}
