"""
AI Council — 主入口
"""
import argparse
import yaml
import uuid
from core.models import CouncilCase


def load_config(config_path: str = "config/default.yaml") -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="AI Council 多角色评议系统")
    parser.add_argument("--topic", type=str, required=True, help="待评议的议题")
    parser.add_argument("--config", type=str, default="config/default.yaml", help="配置文件路径")
    args = parser.parse_args()

    config = load_config(args.config)

    case = CouncilCase(
        case_id=str(uuid.uuid4())[:8],
        raw_input=args.topic
    )

    print(f"\n=== AI Council 评议系统启动 ===")
    print(f"议题：{args.topic}")
    print(f"案例ID：{case.case_id}")
    print("\n流程尚未实现，请参考 pipeline/ 目录下各层实现。")


if __name__ == "__main__":
    main()
