# pipeline 层实现占位
# prepare.py   — 准备层：调用 Analyst，解构议案
# review.py    — 评议层：并行调用各角色，保持隔离
# debate.py    — 辩论层：Critic vs Drafter 交叉质询
# integrate.py — 整合层：调用 Integrator，汇总意见
# report.py    — 输出层：格式化最终报告
