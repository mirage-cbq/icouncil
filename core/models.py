"""
AI Council — 核心数据结构定义
所有角色和流程层共用这些数据结构，保证信息流向的一致性
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class ConfidenceLevel(Enum):
    HIGH = "高"
    MEDIUM = "中"
    LOW = "低"
    DISPUTED = "存疑"


class StageStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    CONVERGED = "converged"       # 已收敛
    PARTIAL = "partial"           # 部分收敛
    DEADLOCK = "deadlock"         # 僵局
    COMPLETED = "completed"


@dataclass
class Opinion:
    """单条意见"""
    role: str                         # 来源角色
    content: str                      # 意见内容
    severity: int                     # 重要程度 1-5
    confidence: float                 # 置信度 0-1
    rebuttable: bool = True           # 是否允许被质询
    domain: Optional[str] = None      # 所属领域（专科顾问用）
    evidence: list[str] = field(default_factory=list)  # 支撑依据


@dataclass
class DebateRound:
    """一轮辩论记录"""
    round_number: int
    challenge: str          # 质询内容
    challenger: str         # 质询方
    response: str           # 回应内容
    respondent: str         # 回应方
    new_evidence_added: bool = False   # 是否引入了新论据


@dataclass
class CouncilCase:
    """一次完整评议的上下文，贯穿整个流程"""
    case_id: str
    raw_input: str                          # 人类原始输入

    # 准备层输出
    core_question: str = ""
    known_conditions: list[str] = field(default_factory=list)
    missing_info: list[str] = field(default_factory=list)
    evaluation_dimensions: list[str] = field(default_factory=list)
    triggered_specialists: list[str] = field(default_factory=list)

    # 评议层输出（各角色独立，按角色名存储）
    draft: str = ""
    opinions: list[Opinion] = field(default_factory=list)

    # 辩论层记录
    debate_rounds: list[DebateRound] = field(default_factory=list)
    debate_status: StageStatus = StageStatus.PENDING

    # 整合层输出
    resolved_disputes: list[str] = field(default_factory=list)
    unresolved_disputes: list[str] = field(default_factory=list)
    supplement_requested: bool = False
    supplement_count: int = 0

    # 最终报告
    conclusion_summary: str = ""
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEDIUM
    supporting_points: list[Opinion] = field(default_factory=list)
    opposing_points: list[Opinion] = field(default_factory=list)
    info_gaps: list[str] = field(default_factory=list)

    # 元信息
    status: StageStatus = StageStatus.PENDING
    warnings: list[str] = field(default_factory=list)   # 系统级警告（如共识预警）
