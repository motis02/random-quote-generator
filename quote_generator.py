import json
import random
from typing import Dict, List, Optional

class RandomQuoteGenerator:
    def __init__(self, data_path: str = "quotes.json"):
        """初始化名言生成器，加载本地名言库"""
        self.data_path = data_path
        self.quotes: List[Dict] = self._load_quotes()

    def _load_quotes(self) -> List[Dict]:
        """从JSON文件加载名言数据，文件不存在时返回默认内置名言"""
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"警告：未找到合法的{self.data_path}，将使用内置默认名言库")
            return [
                {"content": "生活不是等待风暴过去，而是学会在雨中跳舞。", "author": "维维安·格林", "tag": "生活"},
                {"content": "千里之行，始于足下。", "author": "老子", "tag": "励志"},
                {"content": "知识就是力量。", "author": "弗朗西斯·培根", "tag": "学习"},
                {"content": "天行健，君子以自强不息。", "author": "《周易》", "tag": "励志"},
                {"content": "世界上只有一种英雄主义，那就是看清生活的真相之后依然热爱生活。", "author": "罗曼·罗兰", "tag": "人生"}
            ]

    def get_random_quote(self, tag: Optional[str] = None) -> Dict:
        """
        随机获取一条名言
        :param tag: 可选参数，按标签筛选名言，比如"励志"、"人生"
        """
        target_quotes = self.quotes
        if tag:
            target_quotes = [q for q in self.quotes if q.get("tag") == tag]
            if not target_quotes:
                raise ValueError(f"没有找到标签为「{tag}」的名言")
        return random.choice(target_quotes)

    def add_quote(self, content: str, author: str, tag: str = "其他") -> None:
        """手动添加新名言到本地库并持久化保存"""
        new_quote = {"content": content.strip(), "author": author.strip(), "tag": tag.strip()}
        self.quotes.append(new_quote)
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(self.quotes, f, ensure_ascii=False, indent=2)
        print("新名言已成功添加到本地库~")

if __name__ == "__main__":
    generator = RandomQuoteGenerator()
    print("✨ 欢迎使用随机名言警句生成器 ✨")
    while True:
        print("\n请选择操作：")
        print("1. 生成一条随机名言")
        print("2. 按标签筛选生成名言")
        print("3. 手动添加新名言")
        print("0. 退出程序")
        choice = input("请输入选项编号：").strip()

        if choice == "1":
            quote = generator.get_random_quote()
            print(f"\n📜 今日名言：「{quote['content']}」—— {quote['author']} 【{quote['tag']}】")
        elif choice == "2":
            tag = input("请输入要筛选的标签：").strip()
            try:
                quote = generator.get_random_quote(tag=tag)
                print(f"\n📜 今日{tag}类名言：「{quote['content']}」—— {quote['author']}")
            except ValueError as e:
                print(f"❌ 错误：{e}")
        elif choice == "3":
            content = input("请输入名言内容：")
            author = input("请输入名言作者：")
            tag = input("请输入名言分类标签（可选，默认其他）：") or "其他"
            generator.add_quote(content, author, tag)
        elif choice == "0":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 输入无效，请输入正确的选项编号")
 