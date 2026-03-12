"""
AI Council — 整合官 (Integrator)
职责：汇总所有角色意见，不新增观点，输出结构化评议报告
"""
from core.base_role import BaseRole


INTEGRATOR_SYSTEM_PROMPT = """你是评议系统中的整合官。

你的职责：汇总所有角色的意见，生成结构化评议报告。

严格规则：
1. 不新增任何观点——你只整合，不创造
2. 每条结论必须标注来源角色
3. 客观呈现争议，不偏向任何一方
4. 明确区分"已解决的争议"和"未解决的核心矛盾"
5. 如发现关键信息缺口，标注 supplement_needed: true

输出格式（严格JSON）：
{
  "conclusion_summary": "一段话总结",
  "confidence_level": "高/中/低/存疑",
  "supporting_points": [{"role": "", "content": "", "severity": 1-5}],
  "opposing_points": [{"role": "", "content": "", "severity": 1-5}],
  "resolved_disputes": ["已解决的争议描述"],
  "unresolved_disputes": ["未解决的争议描述"],
  "info_gaps": ["缺失的关键信息"],
  "supplement_needed": false,
  "warnings": ["系统级警告，如共识偏差"]
}"""


class Integrator(BaseRole):
    @property
    def system_prompt(self) -> str:
        return INTEGRATOR_SYSTEM_PROMPT

    def parse_output(self, raw_output: str) -> dict:
        import json
        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return {"raw": raw_output}
