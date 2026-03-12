"""
AI Council — 专科顾问基类 (Specialist)
根据议题动态加载，每个领域继承此类定义自己的 system_prompt
"""
from core.base_role import BaseRole


SPECIALIST_PROMPTS = {
    "legal": """你是评议系统中的法律顾问。
只从法律合规角度审查方案：相关法规、潜在法律风险、合规要求。
不发表领域外的意见。""",

    "financial": """你是评议系统中的财务顾问。
只从财务角度审查：成本估算、资金风险、ROI、现金流影响。
不发表领域外的意见。""",

    "technical": """你是评议系统中的技术顾问。
只从技术可行性角度审查：实现难度、技术风险、依赖项、技术债务。
不发表领域外的意见。""",

    "ethical": """你是评议系统中的伦理顾问。
只从伦理角度审查：公平性、潜在伤害、价值观冲突、社会影响。
不发表领域外的意见。""",

    "risk": """你是评议系统中的风险顾问。
从整体风险管理角度审查：识别各类风险，评估概率和影响，提出缓解建议。
不发表领域外的意见。""",
}


class Specialist(BaseRole):
    def __init__(self, domain: str, config: dict, tools=None):
        super().__init__(config, tools)
        self.domain = domain

    @property
    def system_prompt(self) -> str:
        return SPECIALIST_PROMPTS.get(self.domain, "你是一个领域专家，请从专业角度审查方案。")

    def parse_output(self, raw_output: str) -> dict:
        return {"domain": self.domain, "opinion": raw_output}
