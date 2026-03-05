import click
import json
from rich.console import Console
from rich.table import Table
from .core import RosettaStone
from .adapters.factory import AdapterFactory
from .exceptions import UnsupportedProviderError

console = Console()


@click.group()
def main():
    """GPT Rosetta Stone - 统一的大模型 API 参数转换工具"""
    pass


@main.command()
@click.option("--target", "-t", required=True, help="目标提供商 (openai/ernie/qwen)")
@click.option("--input", "-i", "input_file", type=click.File("r"), help="输入 JSON 文件")
@click.option("--data", "-d", help="直接传入 JSON 字符串")
def convert(target, input_file, data):
    """转换请求参数"""
    try:
        if input_file:
            request_data = json.load(input_file)
        elif data:
            request_data = json.loads(data)
        else:
            console.print("[red]错误: 必须提供 --input 或 --data 参数[/red]")
            return

        converter = RosettaStone(target_provider=target)
        result = converter.convert_request(request_data)

        console.print(f"[green]✓ 成功转换为 {target} 格式[/green]")
        console.print_json(data=result)

    except UnsupportedProviderError as e:
        console.print(f"[red]错误: {e}[/red]")
    except Exception as e:
        console.print(f"[red]错误: {e}[/red]")


@main.command()
@click.option("--provider", "-p", required=True, help="提供商名称 (openai/ernie/qwen)")
def show_mapping(provider):
    """显示参数映射表"""
    try:
        adapter = AdapterFactory.get_adapter(provider)
        mapping = adapter.get_parameter_mapping()

        table = Table(title=f"{provider.upper()} 参数映射表")
        table.add_column("标准参数", style="cyan")
        table.add_column("目标参数", style="green")

        for std_param, target_param in mapping.items():
            table.add_row(std_param, target_param)

        console.print(table)

    except UnsupportedProviderError as e:
        console.print(f"[red]错误: {e}[/red]")


if __name__ == "__main__":
    main()
